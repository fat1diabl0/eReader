# -*- coding: utf-8 -*-

import re
import wx, os, pdfkit
import wx.html2
from ExportDialog import ExportDialog
from Settings import SettingsDialog
import SettingsData
from NavigateDialog import NavigateDialog 
from BookmarkNameDialog import BookmarkDialog

try:
    from agw import gradientbutton as GB
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.gradientbutton as GB

class ImportPanel( wx.Panel ):
    def __init__( self, parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )        
        
        self.parent_frame = parent
        
        # self.dictImgOCRData = self.parent_frame.dictImgOCR
        self.activeButton = ""

        #Dictionery for storing Bookmark data
        self.dictBookmarkData = {}

        #Dictionery for storing Bookmark data
        self.dictHeadingsData = {}

        self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyCharHook)

        self.BuildInterface( )
        self.Layout()

    def BuildInterface( self ):
        main_sizer = wx.BoxSizer( wx.HORIZONTAL )
        right_sizer = wx.BoxSizer( wx.VERTICAL )

        #html panel
        self.html_panel = wx.Panel( self, -1 )
        self.html_panel.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
        right_sizer.Add( self.html_panel, 1, wx.EXPAND )
        html_panel_sizer = wx.BoxSizer( wx.VERTICAL )

        #wx.html widget
        self.html_widget = wx.html2.WebView.New( self.html_panel, style = wx.BORDER_NONE )
        self.html_widget.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
        self.html_widget.SetEditable(True)

        html_panel_sizer.Add( self.html_widget, 1, wx.EXPAND )
        self.html_panel.SetSizer( html_panel_sizer )

        #html pager with buttons to different html content
        self.html_pager_sizer = wx.BoxSizer( wx.HORIZONTAL )
        html_panel_sizer.Add( self.html_pager_sizer, 0, wx.ALL, 20 )

        #menu with buttons
        left_sizer = wx.BoxSizer( wx.VERTICAL )
        left_sizer.SetMinSize( self.parent_frame.min_width_menu, 200 )
        main_sizer.Add( left_sizer )
        main_sizer.Add( right_sizer, 1, wx.EXPAND )

        #back button
        back_btn_panel = wx.Panel( self, -1 )
        back_btn_panel.SetBackgroundColour( wx.BLACK )
        back_btn_sizer = wx.BoxSizer( wx.HORIZONTAL )
        st_txt_back = wx.StaticText( back_btn_panel, -1, 'Back', style = wx.ALIGN_CENTRE_HORIZONTAL )
        back_btn_panel.Bind( wx.EVT_LEFT_DOWN, self.OnBack )
        st_txt_back.Bind( wx.EVT_LEFT_DOWN, self.OnBack )
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
            img = wx.Image( os.path.join( self.parent_frame.icons_folder, img_path ), wx.BITMAP_TYPE_PNG )
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

    def OnKeyCharHook(self, event):
        keyCode = event.GetKeyCode()
        # print(keyCode)
        if event.ControlDown():
            if event.GetKeyCode() == 70:
                self.onFindShortCut(event)
            elif event.GetKeyCode() == 66:
                self.onBookmarkShortCut(event)
            elif event.GetKeyCode() == 72:
                self.NavigateText(event)                
            elif event.GetKeyCode() == 83:
                self.ExportText(event)                
            elif event.GetKeyCode() == 8:
                self.OnBack(event)
            elif event.GetKeyCode() == 78:
                self.onNew(event)                
            elif event.GetKeyCode() == 314:
                self.onPrevPage(event)                
            elif event.GetKeyCode() == 316:
                self.onNextPage(event)                
        else:
            event.Skip()


    def LoadHTMLPage(self):
        self.html_widget.SetPage( '', '' )        
        self.html_pager_sizer.Clear(True)
        self.Layout()

        for key in self.parent_frame.dictImgOCR.keys():
            label_btn = key
            html_btn = GB.GradientButton( self.html_panel, -1, label=label_btn, name=label_btn)
            html_btn.Bind( wx.EVT_BUTTON, self.ChangeHtmlContent )
            self.html_pager_sizer.Add( html_btn, 0, wx.RIGHT, 20 )

        # To Click on first button initially
        if len(self.parent_frame.dictImgOCR.keys()) > 0:
            btnName = list(self.parent_frame.dictImgOCR.keys())[0]
            self.UpdateHTMLPage(btnName)
            self.activeButton = btnName  

    def ChangeHtmlContent( self, evt ):
        btn = evt.GetEventObject( );
        btnName = btn.GetName( )

        if btnName == self.activeButton:
            pageText = self.html_widget.GetPageText()
            self.parent_frame.dictImgOCR[btnName] = pageText
        elif btnName != self.activeButton:
            pageText = self.html_widget.GetPageText()
            self.parent_frame.dictImgOCR[self.activeButton] = pageText


        self.UpdateHTMLPage(btnName)
        self.activeButton = btnName

    def UpdateHTMLPage(self,btnName):
        # print(self.parent_frame.dictImgOCR[btnName])
        strData = "<br />".join(self.parent_frame.dictImgOCR[btnName].split("\n"))
        # print(strData)
        c = SettingsData.FontColor.Get(includeAlpha=False)
        color = "rgb(" + str(c[0]) +',' + str(c[1]) +',' + str(c[2]) +')' 
        html = '<html><body style="background-color: rgb( 224, 224, 224 );font-family:'+SettingsData.Font+';font-size:'+str(SettingsData.FontSize)+'px;color:'+ color +'"><div id="content"><p> ' + strData +' </p></div></body></html>'
        self.html_widget.SetPage( html, '' )        

    def onFindShortCut(self,evt):
        # print("onFindShortCut")
        if self.IsShown():
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
        flagToSet = 1

        if intFlags == 1:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT
        elif intFlags == 3:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD
        elif intFlags == 5:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_MATCH_CASE
        elif intFlags == 7:
            flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE

        print(self.html_widget.Find(strFind,flags=flagToSet))

    def onReplace(self, evt):
        strFind = (self.findData.GetFindString()).strip()
        strReplace = (self.findData.GetReplaceString()).strip()

        if len(strReplace):
            intFlags = self.findData.GetFlags()
            flagToSet = 1

            if intFlags == 1:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT
                pattern = re.compile(strFind,re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.parent_frame.dictImgOCR[self.activeButton],count=1)

            elif intFlags == 3:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD
                pattern = re.compile(r'\b'+strFind+r'\b',re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.parent_frame.dictImgOCR[self.activeButton],count=1)

            elif intFlags == 5:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_MATCH_CASE
                strNewPageText = self.parent_frame.dictImgOCR[self.activeButton].replace(strFind,strReplace,1)

            elif intFlags == 7:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE        
                pattern = re.compile(r'\b'+strFind+r'\b')
                strNewPageText = pattern.sub(strReplace,self.parent_frame.dictImgOCR[self.activeButton],count=1)

            intNoOfFound = self.html_widget.Find(strFind,flags=flagToSet)

            self.parent_frame.dictImgOCR[self.activeButton] = strNewPageText
            self.UpdateHTMLPage(self.activeButton)            
        else:
            wx.MessageBox("Please enter replace value.")

    def onReplaceAll(self, evt):
        strFind = (self.findData.GetFindString()).strip()
        strReplace = (self.findData.GetReplaceString()).strip()
        
        if len(strReplace):
            intFlags = self.findData.GetFlags()
            flagToSet = 1
            
            if intFlags == 1:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT
                pattern = re.compile(strFind,re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.parent_frame.dictImgOCR[self.activeButton])

            elif intFlags == 3:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD
                pattern = re.compile(r'\b'+strFind+r'\b',re.IGNORECASE)
                strNewPageText = pattern.sub(strReplace,self.parent_frame.dictImgOCR[self.activeButton])

            elif intFlags == 5:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_MATCH_CASE
                strNewPageText = self.parent_frame.dictImgOCR[self.activeButton].replace(strFind,strReplace)

            elif intFlags == 7:
                flagToSet = wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE        
                pattern = re.compile(r'\b'+strFind+r'\b')
                strNewPageText = pattern.sub(strReplace,self.parent_frame.dictImgOCR[self.activeButton])


            self.parent_frame.dictImgOCR[self.activeButton] = strNewPageText
            self.UpdateHTMLPage(self.activeButton)
        else:
            wx.MessageBox("Please enter replace value.")

    def onFindClose(self, evt):
        self.html_widget.Find("")
        evt.GetDialog().Destroy()
        self.UpdateHTMLPage(self.activeButton)
        
    #code for export text. Export wx.html2 area file.
    def ExportText( self, evt ):
        if self.IsShown():
            html = self.html_widget.GetPageSource( )
            pageText = self.html_widget.GetPageText( )

            img_wildcard = "Text Documents(*.txt)|*.txt | HTML Files(*.html)|*.html | PDF Files(*.pdf)|*.pdf"
            dlg = wx.FileDialog(self, "Save As", os.getcwd(),"",img_wildcard, wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)            
            
            if dlg.ShowModal() == wx.ID_OK:
                fullPath = dlg.GetPath()
                wildcardIndex = dlg.GetFilterIndex()

                if wildcardIndex == 0:
                    with open(fullPath, 'w' ) as f:
                        f.write(pageText)   
                elif wildcardIndex == 1:
                    with open(fullPath, 'w' ) as f:
                        f.write(html)   
                elif wildcardIndex == 2:
                    # print(fullPath)
                    exe_path = os.path.join(os.getcwd(),"bin\\wkhtmltopdf.exe")
                    config = pdfkit.configuration(wkhtmltopdf=exe_path)
                    pdfkit.from_string(pageText, fullPath,configuration = config)
                    
            dlg.Destroy()

    #put here the code for button "Navigate Text"
    def NavigateText( self, evt ):
        if self.IsShown():
            dlg = NavigateDialog(self)
            dlg.Show()

    def Settings( self, evt ):
        if self.parent_frame.cameraPanel.IsShown():
            self.parent_frame.cameraPanel.state = self.parent_frame.cameraPanel.STATE_CLOSING
            self.parent_frame.cameraPanel.objWebCamFeed.release()
            
        SettingsData.noOfCam = self.parent_frame.getConnectedCams()

        dlg = SettingsDialog(self)
        dlg.ShowModal()

        if self.parent_frame.cameraPanel.IsShown():
            self.parent_frame.cameraPanel.state = self.parent_frame.cameraPanel.STATE_RUNNING
            self.parent_frame.cameraPanel.StartLiveWebcamFeed()

        if self.IsShown():
            self.UpdateHTMLPage(self.activeButton)


    def onBookmarkShortCut(self,evt):
        if self.IsShown():
            BMDialog = BookmarkDialog(self)
            BMDialog.ShowModal()

    def OnBack( self, evt ):
        # workDir = os.path.join(os.getcwd(),"pics")
        # for file in os.scandir(workDir):
        #     os.unlink(file.path)                

        self.dictBookmarkData.clear()
        self.dictHeadingsData.clear()
        self.Hide()
        
        self.parent_frame.cameraPanel.Show()
        self.parent_frame.Layout()

        self.parent_frame.cameraPanel.StartLiveWebcamFeed()         
        
        # if self.parent_frame.cameraPanel.IsShown():
        #     self.parent_frame.cameraPanel.Hide()
        # self.parent_frame.landingPanel.Show()
        # self.parent_frame.Layout()

    def DeleteText(self,evt):
        self.html_widget.DeleteSelection()
        self.parent_frame.dictImgOCR[self.activeButton] = self.html_widget.GetPageText( )

    def onNew(self,evt):
        ret = wx.MessageBox("Do you want to delete existing images?",style=wx.YES_NO)
        if ret == 2:
            workDir = os.path.join(os.getcwd(),"pics")
            for file in os.scandir(workDir):
                os.unlink(file.path)                


    def onPrevPage(self,evt):
        keyList = self.parent_frame.dictImgOCR.keys()
        for i,v in enumerate(keyList):
            if v == self.activeButton:
                if i == 0:
                    self.activeButton = list(keyList)[len(keyList)-1]
                else:
                    self.activeButton = list(keyList)[i-1]
                break

        # print(self.activeButton)
        self.UpdateHTMLPage(self.activeButton)


    def onNextPage(self,evt):
        keyList = self.parent_frame.dictImgOCR.keys()
        for i,v in enumerate(keyList):
            if v == self.activeButton:
                if i == len(keyList)-1:
                    self.activeButton = list(keyList)[0]
                else:
                    self.activeButton = list(keyList)[i+1]
                break

        # print(self.activeButton)
        self.UpdateHTMLPage(self.activeButton)
