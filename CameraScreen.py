# -*- coding: utf-8 -*-

import wx, os
import cv2
import time
import threading
import LandingScreen
from models import WebcamFeed
from ImportScreen import *
from collections import OrderedDict
import SettingsData
from backend import googleOCR
import shutil
import SettingsData
import PyPDF2
from PIL import Image

class CameraPanel( wx.Panel ):
    def __init__( self, parent ):
        #wx.Panel.__init__(self, parent, -1, 'Envision Reader', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX)
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )        

        self.parent_frame = parent

        self.BuildInterface()
        self.Layout()

    def BuildInterface( self ):
        main_sizer = wx.BoxSizer( wx.HORIZONTAL )
        right_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_panelVideo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panelVideo.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        right_sizer.Add(self.m_panelVideo, 1, wx.EXPAND |wx.ALL, 5)

        left_sizer = wx.BoxSizer( wx.VERTICAL )
        left_sizer.SetMinSize( self.parent_frame.min_width_menu, 200 )
        main_sizer.Add( left_sizer )
        main_sizer.Add( right_sizer, 1, wx.EXPAND )

        #back button
        panel = wx.Panel( self, -1 )
        panel.SetBackgroundColour( wx.BLACK )
        back_btn_sizer = wx.BoxSizer( wx.HORIZONTAL )
        st_txt_back = wx.StaticText( panel, -1, 'Back', style = wx.ALIGN_CENTRE_HORIZONTAL )
        # panel.Bind( wx.EVT_LEFT_DOWN, self.onClose )
        st_txt_back.Bind( wx.EVT_LEFT_DOWN, self.onBack )
        st_txt_back.SetForegroundColour( wx.WHITE )
        font_back = st_txt_back.GetFont( )
        font_back.SetPointSize( 15 )
        st_txt_back.SetFont( font_back )
        back_btn_sizer.Add( st_txt_back, 1, wx.TOP | wx.BOTTOM, 25 )
        panel.SetSizer( back_btn_sizer )
        left_sizer.Add( panel, 0, wx.EXPAND )

        buttons = [
            [ 'Add Photo Icon.png', 'TAKE PHOTO', self.TakePhoto ],
            [ 'Done Icon.png', 'DONE', self.Done ],
            [ 'Set Timer Icon.png', 'SET TIMER', self.SetTimer ]
        ]

        for img_path, label, func in buttons:
            #image button
            btn_txt = wx.StaticText( self, -1, label )
            img = wx.Image( os.path.join( self.parent_frame.icons_folder, img_path ), wx.BITMAP_TYPE_PNG )
            bmp = img.ConvertToBitmap( )
            btn = wx.BitmapButton( self, -1, bmp, style=wx.NO_BORDER)
            btn.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
            btn.SetBackgroundColour( wx.BLACK )
            btn.Bind( wx.EVT_BUTTON, func )
            left_sizer.Add( btn, 0, wx.TOP | wx.ALIGN_CENTER, 60 )

            #label button
            #btn_txt = wx.StaticText( self, -1, label )
            btn_txt.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
            btn_txt.SetForegroundColour( wx.WHITE )
            font = btn_txt.GetFont( )
            font.SetPointSize( 15 )
            btn_txt.SetFont( font )
            left_sizer.Add( btn_txt, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10 )
        self.SetSizer( main_sizer )
        self.Layout( )

    def StartLiveWebcamFeed( self ):
        # self.noOfCam = self.getConnectedCams()
        camId = 0
        #print(self.noOfCam)
        # if(self.noOfCam > 1):
        #     camId = 0

        self.objWebCamFeed = WebcamFeed(camId)
        if not self.objWebCamFeed.has_webcam():
            print ('Webcam has not been detected.')
            self.Close()           

        """ Creates a 30 fps timer for the update loop """
        self.timer = wx.Timer(self)
        self.timer.Start(1000./30.)
        self.Bind(wx.EVT_TIMER, self.onUpdate, self.timer)
        self.updating = False
        
        """ Bind custom paint events """
        self.m_panelVideo.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)              
        self.m_panelVideo.Bind(wx.EVT_PAINT, self.onPaint)
        
        """ App states """
        self.STATE_RUNNING = 1
        self.STATE_CLOSING = 2
        self.state = self.STATE_RUNNING   

    """ Main Update loop that calls the Paint function """
    def onUpdate(self, event):
        if self.state == self.STATE_RUNNING:
            # fw, fh = self.m_panelVideo.GetSize()
            # x, y = self.m_panelVideo.GetPosition()
            # print(str(fw) + "---" + str(fh))
            # print(str(x) + "---" + str(y))
            # r = wx.Rect(x,y,fw,fh)
            # self.Refresh(rect = r)           
            self.m_panelVideo.Refresh()
            # self.Refresh()
    
    """ Retrieves a new webcam image and paints it onto the frame """
    def onPaint(self, event):
        fw, fh = self.m_panelVideo.GetSize()
        # Retrieve a scaled image from the opencv model
        frame = self.objWebCamFeed.get_image(fw, fh)
        h, w = frame.shape[:2]
        image = wx.Bitmap.FromBuffer(w, h, frame) 
        
        # Use Buffered Painting to avoid flickering
        dc = wx.BufferedPaintDC(self.m_panelVideo)
        dc.DrawBitmap(image, 0, 0)    
    
    """ Background will never be erased, this avoids flickering """
    def onEraseBackground(self, event):
        return

    #put here the code for button "Take Photo"
    def TakePhoto( self, evt ):
        if self.IsShown():
            img = self.objWebCamFeed.read()

            workDir = os.path.join(os.getcwd(),"pics")
            if not os.path.exists(workDir):
                os.makedirs(workDir)        
            
            imgName = str(GetNewImageName()) + ".png"

            imgPath = os.path.join(workDir,imgName)
            cv2.imwrite(imgPath,img)
        
    #put here the code for button "Done"
    def Done( self, evt ):
        if self.IsShown():
            lstThread = threading.enumerate()
            for t in lstThread:
                if t.name == "TimerThread":
                    t.cancel()
                    break   
            
            self.objWebCamFeed.release()                                    
            # self.EndModal(1)  

            self.parent_frame.dictImgOCR = OrderedDict()
            self.parent_frame.dictImgOCR = self.GetAllImageFiles()

            self.Hide()
            if self.parent_frame.landingPanel.IsShown():
                self.parent_frame.landingPanel.Hide()
            self.parent_frame.importPanel.Show()
            self.parent_frame.importPanel.LoadHTMLPage()
            self.parent_frame.Layout()

    #put here the code for button "Set Timer"
    def SetTimer( self, evt ):
        if self.IsShown():
            dlg = TimerDialog(self,self.objWebCamFeed)
            dlg.Show()
        	
    def onBack( self, evt ):
        self.objWebCamFeed.release() 
                   
        self.Hide()
        self.parent_frame.landingPanel.Show()
        self.parent_frame.Layout()

    def getConnectedCams(self):
        max_tested = 100
        for i in range(max_tested):
            temp_camera = cv2.VideoCapture(i)
            if temp_camera.isOpened():
                temp_camera.release()
                continue
            return i 

    def GetAllImageFiles(self):

        d = OrderedDict()

        workDir = os.path.join(os.getcwd(),"pics")

        if os.path.exists(workDir):
            lstAllPNGFiles = [file for file in os.listdir(workDir) if file.endswith('.png')]

            if(len(lstAllPNGFiles) > 0):
                
                for p in lstAllPNGFiles:
                    imgName = p.split('.')[0]
                    imgFullPath = os.path.join(workDir,p)
                    if imgName not in d.keys():
                        imgOCRText = googleOCR.performGoogleOCR(imgFullPath)
                        #print(imgOCRText)
                        d[imgName] = imgOCRText


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

class TimerDialog( wx.Dialog ):
    def __init__( self, parent, objCam):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition,style = wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE_BOX|wx.FRAME_FLOAT_ON_PARENT )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetMaxSize( wx.Size(250,110) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Enter Timer Value (Sec) :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1.Bind(wx.EVT_BUTTON, self.onOK)
        bSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
          
        bSizer1.Add( bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.RIGHT, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )

        self.objTimerWebCam = objCam

    def onOK(self, event):
        timerVal = self.m_textCtrl2.GetValue().strip()
        if (len(timerVal) > 0):
            if timerVal.isdigit():
                t = int(timerVal)
                self.Destroy()
                t = threading.Timer(t,self.capture,[t])
                t.name = "TimerThread"
                t.daemon = True
                t.start()
            else:
                wx.MessageBox("Please enter correct value.")  

    def capture(self,t):
        img = self.objTimerWebCam.read()

        workDir = os.path.join(os.getcwd(),"pics")
        if not os.path.exists(workDir):
            os.makedirs(workDir)        
        
        imgName = str(GetNewImageName()) + ".png"
        
        imgPath = os.path.join(workDir,imgName)
        cv2.imwrite(imgPath,img)   

        t = threading.Timer(t,self.capture,[t])
        t.name = "TimerThread"
        t.daemon = True
        t.start()                 
        

def GetNewImageName():
    workDir = os.path.join(os.getcwd(),"pics")

    lstAllPNGFiles = [file for file in os.listdir(workDir) if file.endswith('.png')]

    lstFiles = []
    for file in lstAllPNGFiles:
        fname = file.split('.')[0]
        if fname.isdigit():
            lstFiles.append(int(fname))

    if len(lstFiles) == 0:
        return 1
    else:
        return max(lstFiles) + 1            


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow()
    frame.Maximize( )
    frame.Show()
    app.MainLoop()
