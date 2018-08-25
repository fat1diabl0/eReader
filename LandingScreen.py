# -*- coding: utf-8 -*-

import wx, os
from CameraScreen import *
from ImportScreen import *
from backend import googleOCR
from collections import OrderedDict
import threading
import shutil
import SettingsData
import PyPDF2
from PIL import Image

class LandingPanel( wx.Panel ):
    #Window with 2 buttons
    def __init__( self,parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )        
        
        size = wx.Display( ).GetClientArea( )
        width_window = size.GetWidth( )
        height_window = size.GetHeight( )
        self.SetMinSize( wx.Size( 0.75 * width_window, 0.75 * height_window ) )
        self.SetPosition( wx.Point( 0.125 *width_window, 0.125 * height_window ) )

        self.parent_frame = parent
        
        self.BuildInterface( )
        self.Layout()

    def BuildInterface( self ):
        panel = wx.Panel( self, -1 )
        main_sizer = wx.BoxSizer( wx.VERTICAL )
        main_sizer.Add( panel, 1, wx.EXPAND )
        panel.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer.AddStretchSpacer(1)
        vsizer.Add(hsizer, 0, wx.CENTER | wx.EXPAND, 15)
        vsizer.AddStretchSpacer(1)
        hsizer.AddStretchSpacer(1)

        img = wx.Image( os.path.join( os.getcwd( ), 'Assets', 'Camera Icon.png' ), wx.BITMAP_TYPE_PNG )
        bmp = img.ConvertToBitmap( )
        btn_camera = wx.BitmapButton( panel, -1, bmp, style=wx.NO_BORDER )
        btn_camera.Bind( wx.EVT_BUTTON, self.OnCameraBtnClick )
        btn_camera.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        # hsizer.Add( btn_camera, 0, wx.ALL , 30 )
        btn_camera_sizer = wx.BoxSizer( wx.VERTICAL )
        btn_camera_sizer.Add( btn_camera )

        btn_camera_text = wx.StaticText( self, -1, 'CAMERA' )
        btn_camera_text.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        btn_camera_text.SetForegroundColour( wx.WHITE )
        font = btn_camera_text.GetFont( )
        font.SetPointSize( 15 )
        btn_camera_text.SetFont( font )
        btn_camera_sizer.Add( btn_camera_text, 0, wx.TOP | wx.ALIGN_CENTER, 5 )
        hsizer.Add( btn_camera_sizer, 0, wx.ALL , 30)

        img = wx.Image( os.path.join( os.getcwd( ), 'Assets', 'Import Icon.png' ), wx.BITMAP_TYPE_PNG )
        bmp = img.ConvertToBitmap( )
        btn_import = wx.BitmapButton( panel, -1, bmp, style=wx.NO_BORDER )
        btn_import.Bind( wx.EVT_BUTTON, self.OnImportBtnClick )
        btn_import.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        btn_import_sizer = wx.BoxSizer( wx.VERTICAL )
        btn_import_sizer.Add( btn_import )

        btn_import_text = wx.StaticText( self, -1, 'IMPORT' )
        btn_import_text.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        btn_import_text.SetForegroundColour( wx.WHITE )
        font = btn_import_text.GetFont( )
        font.SetPointSize( 15 )
        btn_import_text.SetFont( font )
        btn_import_sizer.Add( btn_import_text, 0, wx.TOP | wx.ALIGN_CENTER, 5 )
        hsizer.Add( btn_import_sizer, 0, wx.ALL , 30)

        #hsizer.Add( btn_import, 0, wx.ALL , 30 )

        hsizer.AddStretchSpacer(1)
        #vsizer.AddStretchSpacer(1)
        panel.SetSizer( vsizer )
        self.SetSizer( main_sizer )
        self.Layout( )
        #self.Bind( wx.EVT_SIZE, self.OnResize )
        #self.Fit( )
        self.Centre( wx.BOTH )   

    #click on button "Camera"
    def OnCameraBtnClick( self, evt ):

        self.Hide()
        self.parent_frame.cameraPanel.Show()
        self.parent_frame.Layout()

        self.parent_frame.cameraPanel.StartLiveWebcamFeed()      
        

    #put here code for button "Import"
    def OnImportBtnClick( self, evt ):
        self.parent_frame.onImport(evt)

    def OnResize( self, evt ):
        self.Layout( )
        self.Refresh( )

                    
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = LandingPanel(None)
    #frame.Center( wx.BOTH )
    frame.Maximize( )
    frame.Show()
    app.MainLoop()
