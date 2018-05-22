# -*- coding: utf-8 -*-

import wx, os
import cv2
import time
import threading
from models import WebcamFeed

class CameraWindow( wx.Dialog ):
    def __init__( self, par ):
        wx.Dialog.__init__(self, par, -1, 'Envision Reader', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX)
        self.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        size = wx.Display( ).GetClientArea( )
        width_window = size.GetWidth( )
        height_window = size.GetHeight( )
        self.SetMinSize( wx.Size( 0.75 * width_window, 0.75 * height_window ) )
        self.SetPosition( wx.Point( 0.125 *width_window, 0.125 * height_window ) )
        self.icons_folder = os.path.join( os.getcwd( ), 'Assets' )
        self.min_width_menu = 250
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.BuildInterface()
        self.StartLiveWebcamFeed()
     
    def BuildInterface( self ):
        main_sizer = wx.BoxSizer( wx.HORIZONTAL )
        right_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_panelVideo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panelVideo.SetBackgroundColour( wx.BLUE )
        right_sizer.Add(self.m_panelVideo, 1, wx.EXPAND |wx.ALL, 5)

        left_sizer = wx.BoxSizer( wx.VERTICAL )
        left_sizer.SetMinSize( self.min_width_menu, 200 )
        main_sizer.Add( left_sizer )
        main_sizer.Add( right_sizer, 1, wx.EXPAND )

        #back button
        panel = wx.Panel( self, -1 )
        panel.SetBackgroundColour( wx.BLACK )
        back_btn_sizer = wx.BoxSizer( wx.HORIZONTAL )
        st_txt_back = wx.StaticText( panel, -1, 'Back', style = wx.ALIGN_CENTRE_HORIZONTAL )
        panel.Bind( wx.EVT_LEFT_DOWN, self.onClose )
        st_txt_back.Bind( wx.EVT_LEFT_DOWN, self.onClose )
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
            img = wx.Image( os.path.join( self.icons_folder, img_path ), wx.BITMAP_TYPE_PNG )
            bmp = img.ConvertToBitmap( )
            btn = wx.BitmapButton( self, -1, bmp, style=wx.NO_BORDER )
            btn.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
            btn.SetBackgroundColour( wx.BLACK )
            btn.Bind( wx.EVT_BUTTON, func )
            left_sizer.Add( btn, 0, wx.TOP | wx.ALIGN_CENTER, 60 )

            #label button
            btn_txt = wx.StaticText( self, -1, label )
            btn_txt.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
            btn_txt.SetForegroundColour( wx.WHITE )
            font = btn_txt.GetFont( )
            font.SetPointSize( 15 )
            btn_txt.SetFont( font )
            left_sizer.Add( btn_txt, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10 )
        self.SetSizer( main_sizer )
        self.Layout( )

        """ Bind a custom close event (needed for Windows) """
        self.Bind(wx.EVT_CLOSE, self.Close)        

    def StartLiveWebcamFeed( self ):
        self.objWebCamFeed = WebcamFeed()
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
            self.Refresh()
    
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
        img = self.objWebCamFeed.read()

        workDir = os.path.join(os.getcwd(),"pics")
        if not os.path.exists(workDir):
            os.makedirs(workDir)        
        
        imgName = str(GetNewImageName()) + ".png"

        imgPath = os.path.join(workDir,imgName)
        cv2.imwrite(imgPath,img)
        
    #put here the code for button "Done"
    def Done( self, evt ):
        lstThread = threading.enumerate()
        for t in lstThread:
            if t.name == "TimerThread":
                t.cancel()
                break      

    #put here the code for button "Set Timer"
    def SetTimer( self, evt ):
        dlg = TimerDialog(self,self.objWebCamFeed)
        dlg.ShowModal()
        	

    def onClose( self, evt ):
        print("onClose")
        cv2.destroyAllWindows()
        self.objWebCamFeed.release()
        self.Destroy()

    def Close( self, evt ):
        self.Done(evt)
        cv2.destroyAllWindows()
        self.objWebCamFeed.release()
        self.Destroy()

class TimerDialog( wx.Dialog ):
    def __init__( self, parent, objCam):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition,style = wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE_BOX )
        
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
    frame = CameraWindow(None)
    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()
