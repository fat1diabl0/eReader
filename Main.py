import wx, os, random
import cv2
import CameraScreen
import LandingScreen
import ImportScreen
from collections import OrderedDict
from backend import googleOCR
import Settings
import SettingsData
import PyPDF2
from Shortcuts import clsShortCuts

class MainWindow( wx.Frame ):
    def __init__( self ):
        wx.Frame.__init__(self, None, -1, 'Envision Reader', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX)
        self.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        size = wx.Display( ).GetClientArea( )
        width_window = size.GetWidth( )
        height_window = size.GetHeight( )
        self.SetMinSize( wx.Size( 0.75 * width_window, 0.75 * height_window ) )
        self.SetPosition( wx.Point( 0.125 *width_window, 0.125 * height_window ) )
        self.icons_folder = os.path.join( os.getcwd( ), 'Assets' )
        self.min_width_menu = 250
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.CreateMenu( )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.landingPanel = LandingScreen.LandingPanel(self)   
        bSizer3.Add( self.landingPanel, 0, wx.ALL | wx.EXPAND, 5 )         

        self.cameraPanel = CameraScreen.CameraPanel(self)   
        bSizer3.Add( self.cameraPanel, 0, wx.ALL | wx.EXPAND, 5 )

        self.importPanel = ImportScreen.ImportPanel(self)   
        bSizer3.Add( self.importPanel, 0, wx.ALL | wx.EXPAND, 5 )

        self.landingPanel.Hide()           
        self.importPanel.Hide()        
        self.cameraPanel.Show()

        self.cameraPanel.StartLiveWebcamFeed()

        self.SetSizer( bSizer3 )
        self.Layout()
        self.Centre( wx.BOTH )   

        self.Bind(wx.EVT_CLOSE, self.onClose)    

        settingsFilePath = os.path.join(os.getcwd(),"Settings.dat")
        if os.path.exists(settingsFilePath):
            with open(settingsFilePath,'r') as f:
                lines = f.readlines()
                for l in lines:
                    fields = l.split(':')
                    if fields[0] == "OCRMethod":
                        SettingsData.OCRMethod = fields[1].strip()              

        self.SetShortCut() 

    def CreateMenu( self ):
        menu_bar = wx.MenuBar( )

        file_menu = wx.Menu( )
        menu_item = wx.MenuItem( file_menu,wx.ID_OPEN, text = "&Import",kind = wx.ITEM_NORMAL )

        file_menu.Append( menu_item )
        menu_item = wx.MenuItem( file_menu,wx.ID_SAVEAS, text = "&Export",kind = wx.ITEM_NORMAL )
        file_menu.Append( menu_item )
        menu_item = wx.MenuItem( file_menu,wx.ID_EXIT, text = "&Quit",kind = wx.ITEM_NORMAL )
        file_menu.Append( menu_item )
        menu_bar.Append( file_menu, '&File' )

        navigation_menu = wx.Menu( )
        self.bookmarkID = wx.NewId()
        menu_item = wx.MenuItem( navigation_menu,self.bookmarkID, text = "&Bookmark",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )

        self.headingID = wx.NewId()
        menu_item = wx.MenuItem( navigation_menu,self.headingID, text = "H&eadings",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_item = wx.MenuItem( navigation_menu,wx.ID_FIND, text = "&Find",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_bar.Append( navigation_menu, '&Navigation' )

        help_menu = wx.Menu( )
        self.settingsID = wx.NewId()
        menu_item = wx.MenuItem( help_menu,self.settingsID, text = "&Settings",kind = wx.ITEM_NORMAL )
        help_menu.Append( menu_item )
        self.manualID = wx.NewId()
        menu_item = wx.MenuItem( help_menu,self.manualID, text = "&Manual",kind = wx.ITEM_NORMAL )
        help_menu.Append( menu_item )
        menu_item = wx.MenuItem( help_menu,wx.ID_HELP, text = "&Report a Bug",kind = wx.ITEM_NORMAL )
        help_menu.Append( menu_item )

        menu_bar.Append( help_menu, '&Help' )

        self.SetMenuBar( menu_bar )
        
        self.Bind( wx.EVT_MENU, self.HandleMenuItem )

    def HandleMenuItem( self, evt ):
        menu_id = evt.GetId( )
        if menu_id == wx.ID_OPEN:
            self.onImport(evt)
        elif menu_id == wx.ID_SAVEAS:
            self.importPanel.ExportText(evt)
        elif menu_id == wx.ID_EXIT:
            self.onClose(evt)
        elif menu_id == wx.ID_NEW:
            self.importPanel.NavigateText(evt)
        elif menu_id == wx.ID_FIND:
            self.importPanel.onFindShortCut(evt)
        elif menu_id == self.settingsID:
            self.importPanel.Settings(evt)
        elif menu_id == self.manualID:
            dlg = clsShortCuts(self)
            dlg.Show()           
        elif menu_id == wx.ID_HELP:
            wx.MessageBox( 'Help' )
        elif menu_id == self.bookmarkID:
            self.importPanel.onBookmarkShortCut(evt)
        elif menu_id == self.headingID:
            wx.MessageBox( 'Headings' )         

    def onClose( self, evt ):
        if self.cameraPanel.IsShown():
            self.cameraPanel.objWebCamFeed.release()

        if self.importPanel.IsShown():
            if len(self.importPanel.dictBookmarkData.keys()) > 0:

                ret = wx.MessageBox("You have created bookmark. Do you want to save?",style=wx.YES_NO)
                if ret == 2:
                    evt.Veto()
                    self.importPanel.ExportText(evt)
                    return
                else:
                    self.DestroyLater()

        self.DestroyLater()        

    def SetShortCut(self):
        importID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onImport, id=importID)

        findID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.importPanel.onFindShortCut, id=findID)

        bookmarkID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.importPanel.onBookmarkShortCut, id=bookmarkID)

        takePhoteID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.cameraPanel.TakePhoto, id=takePhoteID)

        doneID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.cameraPanel.Done, id=doneID)

        timerID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.cameraPanel.SetTimer, id=timerID)

        settingsID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.importPanel.Settings, id=settingsID)

        exportID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.importPanel.ExportText, id=exportID)

        navigationID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.importPanel.NavigateText, id=navigationID)                

        deleteID = wx.NewId()
        self.Bind(wx.EVT_MENU, self.importPanel.DeleteText, id=deleteID)                
                        
        entries = [wx.AcceleratorEntry() for i in range(10)]

        entries[0].Set(SettingsData.ctrlKey, ord(SettingsData.Import), importID)
        entries[1].Set(SettingsData.ctrlKey, ord(SettingsData.FindReplace), findID)
        entries[2].Set(SettingsData.ctrlKey, ord(SettingsData.Bookmarks), bookmarkID)
        entries[3].Set(SettingsData.ctrlKey, SettingsData.TakePhoto, takePhoteID)
        entries[4].Set(SettingsData.ctrlKey, ord(SettingsData.Done), doneID)
        entries[5].Set(SettingsData.ctrlKey, ord(SettingsData.Timer), timerID)
        entries[6].Set(SettingsData.ctrlKey, ord(SettingsData.SettingsDialog), settingsID)
        entries[7].Set(SettingsData.ctrlKey, ord(SettingsData.Export), exportID)
        entries[8].Set(SettingsData.ctrlKey, ord(SettingsData.Navigation), navigationID)
        entries[9].Set(SettingsData.normalKey, SettingsData.Delete, deleteID)

        accel = wx.AcceleratorTable(entries)
        self.SetAcceleratorTable(accel)        

    def onImport( self, evt ):
        if self.cameraPanel.IsShown() or self.landingPanel.IsShown():
            self.dictImgOCR = OrderedDict()

            img_wildcard = "PNG and JPG files (*.png;*.jpg)|*.png;*.jpg |PDF Files (*.PDF) | *.PDF"
            image_dlg = wx.FileDialog( self, "Open Image File", wildcard=img_wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
            
            if image_dlg.ShowModal() == wx.ID_OK:
                
                lstSelectedFiles = image_dlg.GetPaths( )

                lstImages = []
                fname,fext = os.path.splitext(lstSelectedFiles[0])
                if fext == '.pdf':
                    fPath = os.path.dirname(fname)
                    lstImages = self.GetImagesFromPDF(lstSelectedFiles,fPath)
                    #print(lstImages)
                    if lstImages is None:
                        return
                else:
                    lstImages = lstSelectedFiles

                if len(lstImages) > 0:
                    #perform Google OCR
                    
                    for img in lstImages:
                        # imgOCRText = googleOCR.performGoogleOCR(img)
                        # print(img)
                        # print(SettingsData.OCRMethod)
                        if SettingsData.OCRMethod == "Google":
                            imgOCRText = googleOCR.performGoogleOCR(img)
                            # print(imgOCRText)    
                        else:
                            imgOCRText = self.OCRByOmniPageMethod(img)
                            # print(imgOCRText)

                        imgName = os.path.splitext(os.path.basename(img))[0]
                        self.dictImgOCR[imgName] = imgOCRText

                else:
                    for pdf in lstSelectedFiles:
                        objPdf = PyPDF2.PdfFileReader(open(pdf, "rb"))
                        noOfPages = objPdf.numPages
                        for page in objPdf.pages: 
                            pageText = page.extractText()
                            
                            while True:
                                no = random.randint(1,200)
                                if no not in self.dictImgOCR.keys():
                                    self.dictImgOCR[str(no)] = pageText
                                    break
                                else:
                                    continue

                    
                if self.cameraPanel.IsShown():
                    self.cameraPanel.Hide()
                if self.landingPanel.IsShown():
                    self.landingPanel.Hide()

                self.importPanel.Show()
                self.importPanel.LoadHTMLPage()
                self.Layout()
            
            image_dlg.Destroy( )            

    def GetAllImageFiles(self):

        d = OrderedDict()

        workDir = os.path.join(os.getcwd(),"pics")

        if os.path.exists(workDir):
            lstAllPNGFiles = [file for file in os.listdir(workDir) if file.endswith('.png')]

            if(len(lstAllPNGFiles) > 0):
                max_count = 100 / len(lstAllPNGFiles)
                val = 0
                
                for p in lstAllPNGFiles:
                    val = val + max_count
                    self.gauge.SetValue(val)
                    imgName = p.split('.')[0]
                    imgFullPath = os.path.join(workDir,p)
                    if imgName not in d.keys():
                        imgOCRText = googleOCR.performGoogleOCR(imgFullPath)
                        #print(imgOCRText)
                        d[imgName] = imgOCRText

                self.gauge.SetValue(0)

            if SettingsData.IsSaveImages == "No":
                shutil.rmtree(workDir)

        return d

    def GetImagesFromPDF(self,lstSelectedFiles,filePath):
        try:
            lstImages = []
            
            for pdf in lstSelectedFiles:
                objPdf = PyPDF2.PdfFileReader(open(pdf, "rb"))
                
                noOfPages = objPdf.numPages
                
                for page in objPdf.pages: 

                    if '/XObject' in page['/Resources']:
                        xObject = page['/Resources']['/XObject'].getObject()

                    for obj in xObject:
                        if xObject[obj]['/Subtype'] == '/Image':
                            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                            data = xObject[obj].getData()
                            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                                mode = "RGB"
                            else:
                                mode = "P"
                    
                            if '/Filter' in xObject[obj]:
                                if xObject[obj]['/Filter'] == '/FlateDecode':
                                    img = Image.frombytes(mode, size, data)
                                    fname = obj[1:] + ".png"
                                    fullFilePath = os.path.join(filePath,fname)
                                    img.save(fullFilePath)
                                    lstImages.append(fullFilePath)
                                elif xObject[obj]['/Filter'] == '/DCTDecode':
                                    fname = obj[1:] + ".jpg"
                                    fullFilePath = os.path.join(filePath,fname)
                                    img = open(fullFilePath, "wb")
                                    img.write(data)
                                    img.close()
                                    lstImages.append(fullFilePath)
                            else:
                                img = Image.frombytes(mode, size, data)
                                fname = obj[1:] + ".png"
                                fullFilePath = os.path.join(filePath,fname)
                                img.save(fullFilePath)
                                lstImages.append(fullFilePath)

            return lstImages
        except :
            return lstImages

    def OCRByOmniPageMethod(self,strInput):
        strOutput = os.path.join(os.getcwd(),'output.txt')
        # strOutput = os.path.join(os.getcwd(),'output.xml')

        os.system('python OCR-mod-Command.py ' + "\"" + strInput + "\"" + ' ' + "\"" + strOutput +"\"")

        with open(strOutput,'r') as f:
            strText = f.read()
            # print(strText.encode("utf-8"))

        os.remove(strOutput)        

        return strText


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow()
    frame.Maximize( )
    frame.Show()
    app.MainLoop()
