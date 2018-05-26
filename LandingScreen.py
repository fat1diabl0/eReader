# -*- coding: utf-8 -*-

import wx, os
from CameraScreen import *
from ImportScreen import *
from backend import googleOCR
from collections import OrderedDict
import threading

class MainFrame( wx.Frame ):
    #Window with 2 buttons
    def __init__( self ):
        wx.Frame.__init__( self, None, -1, 'Envision Reader' )
        size = wx.Display( ).GetClientArea( )
        width_window = size.GetWidth( )
        height_window = size.GetHeight( )
        self.SetMinSize( wx.Size( 0.75 * width_window, 0.75 * height_window ) )
        self.SetPosition( wx.Point( 0.125 *width_window, 0.125 * height_window ) )
        self.BuildInterface( )
        self.CreateMenu( )

    def CreateMenu( self ):
        menu_bar = wx.MenuBar( )
        

        file_menu = wx.Menu( )
        menu_item = wx.MenuItem( file_menu,wx.ID_OPEN, text = "Import",kind = wx.ITEM_NORMAL )

        file_menu.Append( menu_item )
        menu_item = wx.MenuItem( file_menu,wx.ID_ADD, text = "Export",kind = wx.ITEM_NORMAL )
        file_menu.Append( menu_item )
        menu_item = wx.MenuItem( file_menu,wx.ID_EXIT, text = "Quit",kind = wx.ITEM_NORMAL )
        file_menu.Append( menu_item )
        menu_bar.Append( file_menu, 'File' )

        navigation_menu = wx.Menu( )
        menu_item = wx.MenuItem( navigation_menu,wx.ID_ANY, text = "Bookmark",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_item = wx.MenuItem( navigation_menu,wx.ID_ANY, text = "Headings",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_item = wx.MenuItem( navigation_menu,wx.ID_ANY, text = "Find",kind = wx.ITEM_NORMAL )
        navigation_menu.Append( menu_item )
        menu_bar.Append( navigation_menu, 'Navigation' )

        help_menu = wx.Menu( )
        menu_item = wx.MenuItem( help_menu,wx.ID_HELP, text = "Manual",kind = wx.ITEM_NORMAL )
        help_menu.Append( menu_item )
        menu_item = wx.MenuItem( help_menu,wx.ID_HELP, text = "Report a Bug",kind = wx.ITEM_NORMAL )
        help_menu.Append( menu_item )

        menu_bar.Append( help_menu, 'Help' )


        self.SetMenuBar( menu_bar )
        

        self.Bind( wx.EVT_MENU, self.HandleMenuItem )

    def HandleMenuItem( self, evt ):
        #menu_item = evt.GetEventObject( )
        menu_id = evt.GetId( )
        if menu_id == wx.ID_OPEN:
            wx.MessageBox( 'Import Images/PDF' )
        elif menu_id == wx.ID_ADD:
            wx.MessageBox( 'Export to PDF/HTML/RTF' )
        elif menu_id == wx.ID_EXIT:
            self.Close()
        elif menu_id == wx.ID_NEW:
            wx.MessageBox( 'Navigation' )
        elif menu_id == wx.ID_ANY:
            wx.MessageBox( 'Navigation Options' )
        elif menu_id == wx.ID_HELP:
            wx.MessageBox( 'Help' )

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

        # self.gauge = wx.Gauge(panel, range = 20, size = (500, 25), style = wx.GA_HORIZONTAL)
        # vsizer.Add(self.gauge)

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

    #click on button "Camera"
    def OnCameraBtnClick( self, evt ):
        dlg = CameraWindow( self )
        dlg.Maximize( )
        res = dlg.ShowModal( )
        
        if res:
            wx.MessageBox(message='OCR Processing',caption='Envision Reader',style=wx.OK | wx.ICON_INFORMATION)                   
            self.dictImgOCR = GetAllImageFiles()
            dlg = ImportWindow( self )
            dlg.Maximize( )
            dlg.Show( )        

    #put here code for button "Import"
    def OnImportBtnClick( self, evt ):
        img_wildcard = "PNG and GPG files (*.png;*.jpg)|*.png;*.jpg"
        image_dlg = wx.FileDialog( self, "Open Image File", wildcard=img_wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if image_dlg.ShowModal( ) == wx.ID_OK:
            lstImgPath = image_dlg.GetPaths( )
            
            wx.MessageBox(message='OCR Processing',caption='Envision Reader',style=wx.OK | wx.ICON_INFORMATION)
            #perform Google OCR
            self.dictImgOCR = OrderedDict()
            for img in lstImgPath:
                imgOCRText = googleOCR.performGoogleOCR(img)
                #print(imgOCRText)
                imgName = os.path.splitext(os.path.basename(img))[0]
                self.dictImgOCR[imgName] = imgOCRText

            dlg = ImportWindow( self )
            dlg.Maximize( )
            dlg.ShowModal( )
        
        image_dlg.Destroy( )

    def OnResize( self, evt ):
        self.Layout( )
        self.Refresh( )

def GetAllImageFiles():

    d = OrderedDict()

    workDir = os.path.join(os.getcwd(),"pics")

    if os.path.exists(workDir):
        lstAllPNGFiles = [file for file in os.listdir(workDir) if file.endswith('.png')]
        #print(lstAllPNGFiles)
        for p in lstAllPNGFiles:
            imgName = p.split('.')[0]
            imgFullPath = os.path.join(workDir,p)
            if imgName not in d.keys():
                imgOCRText = googleOCR.performGoogleOCR(imgFullPath)
                d[imgName] = imgOCRText

    return d

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame( )
    #frame.Center( wx.BOTH )
    frame.Maximize( )
    frame.Show()
    app.MainLoop()
