import wx, os
import cv2
import CameraScreen
import LandingScreen
import ImportScreen
from collections import OrderedDict
from backend import googleOCR
import SettingsData

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
        self.landingPanel.Hide()   

        self.importPanel = ImportScreen.ImportPanel(self)   
        bSizer3.Add( self.importPanel, 0, wx.ALL | wx.EXPAND, 5 )
        self.importPanel.Hide()        

        self.cameraPanel = CameraScreen.CameraPanel(self)   
        bSizer3.Add( self.cameraPanel, 0, wx.ALL | wx.EXPAND, 5 )
        self.cameraPanel.Show()

        self.SetSizer( bSizer3 )
        self.Layout()
        self.Centre( wx.BOTH )   

        self.SetShortCut() 

    def CreateMenu( self ):
        menu_bar = wx.MenuBar( )

        file_menu = wx.Menu( )
        menu_item = wx.MenuItem( file_menu,wx.ID_OPEN, text = "&Import",kind = wx.ITEM_NORMAL )

        file_menu.Append( menu_item )
        menu_item = wx.MenuItem( file_menu,wx.ID_ADD, text = "Export",kind = wx.ITEM_NORMAL )
        file_menu.Append( menu_item )
        menu_item = wx.MenuItem( file_menu,wx.ID_EXIT, text = "Quit",kind = wx.ITEM_NORMAL )
        file_menu.Append( menu_item )
        menu_bar.Append( file_menu, '&File' )

        navigation_menu = wx.Menu( )
        menu_item = wx.MenuItem( navigation_menu,wx.ID_ANY, text = "&Bookmark",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_item = wx.MenuItem( navigation_menu,wx.ID_ANY, text = "Headings",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_item = wx.MenuItem( navigation_menu,wx.ID_ANY, text = "&Find",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_bar.Append( navigation_menu, '&Navigation' )

        help_menu = wx.Menu( )
        menu_item = wx.MenuItem( help_menu,wx.ID_HELP, text = "Manual",kind = wx.ITEM_NORMAL )
        help_menu.Append( menu_item )
        menu_item = wx.MenuItem( help_menu,wx.ID_HELP, text = "Report a Bug",kind = wx.ITEM_NORMAL )
        help_menu.Append( menu_item )

        menu_bar.Append( help_menu, '&Help' )

        self.SetMenuBar( menu_bar )
        
        self.Bind( wx.EVT_MENU, self.HandleMenuItem )

    def HandleMenuItem( self, evt ):
        menu_id = evt.GetId( )
        if menu_id == wx.ID_OPEN:
            self.onImport(evt)
        elif menu_id == wx.ID_ADD:
            self.importPanel.ExportText(evt)
            # wx.MessageBox( 'Export to PDF/HTML/RTF' )
        elif menu_id == wx.ID_EXIT:
            self.Close()
        elif menu_id == wx.ID_NEW:
            wx.MessageBox( 'Navigation' )
        elif menu_id == wx.ID_ANY:
            wx.MessageBox( 'Navigation Options' )
        elif menu_id == wx.ID_HELP:
            wx.MessageBox( 'Help' )

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
                        
        entries = [wx.AcceleratorEntry() for i in range(9)]

        entries[0].Set(SettingsData.Key, ord(SettingsData.Import), importID)
        entries[1].Set(SettingsData.Key, ord(SettingsData.FindReplace), findID)
        entries[2].Set(SettingsData.Key, ord(SettingsData.Bookmarks), bookmarkID)
        entries[3].Set(SettingsData.Key, SettingsData.TakePhoto, takePhoteID)
        entries[4].Set(SettingsData.Key, ord(SettingsData.Done), doneID)
        entries[5].Set(SettingsData.Key, ord(SettingsData.Timer), timerID)
        entries[6].Set(SettingsData.Key, ord(SettingsData.SettingsDialog), settingsID)
        entries[7].Set(SettingsData.Key, ord(SettingsData.Export), exportID)
        entries[8].Set(SettingsData.Key, ord(SettingsData.Navigation), navigationID)

        accel = wx.AcceleratorTable(entries)
        self.SetAcceleratorTable(accel)        

    def onImport( self, evt ):
        if self.cameraPanel.IsShown() or self.landingPanel.IsShown():
            self.dictImgOCR = OrderedDict()

            img_wildcard = "PNG and GPG files (*.png;*.jpg)|*.png;*.jpg |PDF Files (*.PDF) | *.PDF"
            image_dlg = wx.FileDialog( self, "Open Image File", wildcard=img_wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
            
            if image_dlg.ShowModal( ) == wx.ID_OK:
                
                if self.cameraPanel.vc.isOpened(): 
                    self.cameraPanel.vc.release()  
                    cv2.destroyAllWindows()

                lstSelectedFiles = image_dlg.GetPaths( )

                lstImages = []
                IsPDFSelected = False
                fname,fext = os.path.splitext(lstSelectedFiles[0])
                if fext == '.pdf':
                    IsPDFSelected = True
                    fPath = os.path.dirname(fname)
                    lstImages = self.GetImagesFromPDF(lstSelectedFiles,fPath)
                    #print(lstImages)
                    if lstImages is None:
                        return
                else:
                    lstImages = lstSelectedFiles

                if len(lstImages) > 0:
                    #perform Google OCR
                    
                    max_count = 100 / len(lstImages)
                    val = 0
                    for img in lstImages:
                        val = val + max_count
                        imgOCRText = googleOCR.performGoogleOCR(img)
                        #print(imgOCRText)
                        imgName = os.path.splitext(os.path.basename(img))[0]
                        self.dictImgOCR[imgName] = imgOCRText

                        if IsPDFSelected:
                            os.remove(img)

                    
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
            print("Not Supported PDF File - PyPDF2 Error")

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow()
    frame.Maximize( )
    frame.Show()
    app.MainLoop()