# -*- coding: utf-8 -*-

import re
import wx, os
import wx.html2
from ExportDialog import ExportDialog
from Settings import SettingsDialog
import SettingsData
from NavigateDialog import NavigateDialog 

try:
    from agw import gradientbutton as GB
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.gradientbutton as GB

class ImportWindow( wx.Dialog ):
    def __init__( self, par):
        wx.Dialog.__init__(self, par, -1, 'Envision Reader', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX  )
        self.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
        size = wx.Display( ).GetClientArea( )
        width_window = size.GetWidth( )
        height_window = size.GetHeight( )
        self.SetMinSize( wx.Size( 0.75 * width_window, 0.75 * height_window ) )
        self.SetPosition( wx.Point( 0.125 *width_window, 0.125 * height_window ) )
        self.icons_folder = os.path.join( os.getcwd( ), 'Assets' )
        self.html_folder = os.path.join( os.getcwd( ), 'test_html' )
        self.min_width_menu = 250
        self.dictImgOCRData = par.dictImgOCR
        self.activeButton = ""

        #Set Shortcut for Find & Replace Dialog
        randomId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onFindShortCut, id=randomId)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('H'), randomId )])
        self.SetAcceleratorTable(accel_tbl)

        self.BuildInterface( )

    def BuildInterface( self ):
        main_sizer = wx.BoxSizer( wx.HORIZONTAL )
        right_sizer = wx.BoxSizer( wx.VERTICAL )

        #html panel
        html_panel = wx.Panel( self, -1 )
        html_panel.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
        right_sizer.Add( html_panel, 1, wx.EXPAND )
        html_panel_sizer = wx.BoxSizer( wx.VERTICAL )

        #wx.html widget
        self.html_widget = wx.html2.WebView.New( html_panel, style = wx.BORDER_NONE )
        self.html_widget.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
        html_panel_sizer.Add( self.html_widget, 1, wx.EXPAND )
        html_panel.SetSizer( html_panel_sizer )

        #html pager with buttons to different html content
        html_pager_sizer = wx.BoxSizer( wx.HORIZONTAL )

        for key in self.dictImgOCRData.keys():
            label_btn = key
            html_btn = GB.GradientButton( html_panel, -1, label=label_btn, name=label_btn)
            html_btn.Bind( wx.EVT_BUTTON, self.ChangeHtmlContent )
            html_pager_sizer.Add( html_btn, 0, wx.RIGHT, 20 )

        # To Click on first button initially
        if len(self.dictImgOCRData.keys()) > 0:
            btnName = list(self.dictImgOCRData.keys())[0]
            self.UpdateHTMLPage(btnName)
            self.activeButton = btnName

        html_panel_sizer.Add( html_pager_sizer, 0, wx.ALL, 20 )

        #menu with buttons
        left_sizer = wx.BoxSizer( wx.VERTICAL )
        left_sizer.SetMinSize( self.min_width_menu, 200 )
        main_sizer.Add( left_sizer )
        main_sizer.Add( right_sizer, 1, wx.EXPAND )

        #back button
        back_btn_panel = wx.Panel( self, -1 )
        back_btn_panel.SetBackgroundColour( wx.BLACK )
        back_btn_sizer = wx.BoxSizer( wx.HORIZONTAL )
        st_txt_back = wx.StaticText( back_btn_panel, -1, 'Back', style = wx.ALIGN_CENTRE_HORIZONTAL )
        back_btn_panel.Bind( wx.EVT_LEFT_DOWN, self.OnClose )
        st_txt_back.Bind( wx.EVT_LEFT_DOWN, self.OnClose )
        st_txt_back.SetForegroundColour( wx.WHITE )
        font_back = st_txt_back.GetFont( )
        font_back.SetPointSize( 15 )
        st_txt_back.SetFont( font_back )
        back_btn_sizer.Add( st_txt_back, 1, wx.TOP | wx.BOTTOM, 25 )
        back_btn_panel.SetSizer( back_btn_sizer )
        left_sizer.Add( back_btn_panel, 0, wx.EXPAND )

        buttons = [
            [ 'Export Icon.png', 'EXPORT', self.ExportText ],
            [ 'Find Icon.png', 'NAVIGATE', self.NavigateText ],
            [ 'Settings Icon.png', 'SETTINGS', self.Settings ]
        ]

        for img_path, label, func in buttons:
            #image button
            img = wx.Image( os.path.join( self.icons_folder, img_path ), wx.BITMAP_TYPE_PNG )
            bmp = img.ConvertToBitmap( )
            btn = wx.BitmapButton( self, -1, bmp, style=wx.NO_BORDER )
            btn.SetBackgroundColour( wx.Colour( 79, 79, 79 ) )
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

    def ChangeHtmlContent( self, evt ):
        btn = evt.GetEventObject( );
        btnName = btn.GetName( )
        self.UpdateHTMLPage(btnName)
        self.activeButton = btnName

    def UpdateHTMLPage(self,btnName):
        c = SettingsData.FontColor.Get(includeAlpha=False)
        color = "rgb(" + str(c[0]) +',' + str(c[1]) +',' + str(c[2]) +')' 
        html = '<html><body style="background-color: rgb( 224, 224, 224 );font-family:'+SettingsData.Font+';font-size:'+str(SettingsData.FontSize)+'px;color:'+ color +'"> ' + self.dictImgOCRData[btnName] +'</body></html>'
        self.html_widget.SetPage( html, '' )        

    def onFindShortCut(self,evt):
       self.findData = wx.FindReplaceData() 
       dlg = wx.FindReplaceDialog(self, self.findData, "Find & Replace", wx.FR_REPLACEDIALOG)
       dlg.Bind(wx.EVT_FIND, self.onFindNext)
       dlg.Bind(wx.EVT_FIND_NEXT, self.onFindNext)
       dlg.Bind(wx.EVT_FIND_REPLACE, self.onReplace)
       dlg.Bind(wx.EVT_FIND_REPLACE_ALL, self.onReplaceAll)
       dlg.Bind(wx.EVT_FIND_CLOSE, self.onFindClose)
       dlg.Show(True) 

    def onFindNext(self, evt):
        strFind = (self.findData.GetFindString()).strip()
        intFlags = self.findData.GetFlags()

        if intFlags == 1:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT
        elif intFlags == 3:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD
        elif intFlags == 5:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_MATCH_CASE
        elif intFlags == 7:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE

        self.html_widget.Find(strFind,flags=flagToSet)

    def onReplace(self, evt):
        strFind = (self.findData.GetFindString()).strip()
        strReplace = (self.findData.GetReplaceString()).strip()

        if len(strReplace):
            intFlags = self.findData.GetFlags()

            if intFlags == 1:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT
                pattern = re.compile(strFind,re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.dictImgOCRData[self.activeButton],count=1)

            elif intFlags == 3:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD
                pattern = re.compile(r'\b'+strFind+r'\b',re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.dictImgOCRData[self.activeButton],count=1)

            elif intFlags == 5:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_MATCH_CASE
                strNewPageText = self.dictImgOCRData[self.activeButton].replace(strFind,strReplace,1)

            elif intFlags == 7:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE        
                pattern = re.compile(r'\b'+strFind+r'\b')
                strNewPageText = pattern.sub(strReplace,self.dictImgOCRData[self.activeButton],count=1)

            intNoOfFound = self.html_widget.Find(strFind,flags=flagToSet)

            self.dictImgOCRData[self.activeButton] = strNewPageText
            self.UpdateHTMLPage(self.activeButton)            
        else:
            wx.MessageBox("Please enter replace value.")

    def onReplaceAll(self, evt):
        strFind = (self.findData.GetFindString()).strip()
        strReplace = (self.findData.GetReplaceString()).strip()
        
        if len(strReplace):
            intFlags = self.findData.GetFlags()

            if intFlags == 1:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT
                pattern = re.compile(strFind,re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.dictImgOCRData[self.activeButton])

            elif intFlags == 3:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD
                pattern = re.compile(r'\b'+strFind+r'\b',re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.dictImgOCRData[self.activeButton])

            elif intFlags == 5:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_MATCH_CASE
                strNewPageText = self.dictImgOCRData[self.activeButton].replace(strFind,strReplace)

            elif intFlags == 7:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE        
                pattern = re.compile(r'\b'+strFind+r'\b')
                strNewPageText = pattern.sub(strReplace,self.dictImgOCRData[self.activeButton])


            self.dictImgOCRData[self.activeButton] = strNewPageText
            self.UpdateHTMLPage(self.activeButton)
        else:
            wx.MessageBox("Please enter replace value.")

    def onFindClose(self, evt):
        self.html_widget.Find("")
        evt.GetDialog().Destroy()
        self.UpdateHTMLPage(self.activeButton)
        
    #code for export text. Export wx.html2 area file.
    def ExportText( self, evt ):
        html = self.html_widget.GetPageSource( )
        txt = self.html_widget.GetPageText( )
        dlg = ExportDialog( self, html, txt )
        dlg.CentreOnScreen( )
        dlg.Fit( )
        dlg.ShowModal( )

    #put here the code for button "Navigate Text"
    def NavigateText( self, evt ):
        #wx.MessageBox( 'Navigate Text Button' )
        dlg = NavigateDialog(self)
        dlg.ShowModal()

    #put here the code for button "Set Timer"
    def Settings( self, evt ):
        dlg = SettingsDialog(self)
        dlg.ShowModal()

    def OnClose( self, evt ):
        #self.EndModal( -1 )
        self.Destroy( )
