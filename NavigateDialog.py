# -*- coding: utf-8 -*-

import wx
try:
    from agw import aui
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui

class NavigateDialog( wx.Dialog ):
    """Dialog which is appear when Navigate button was clicked"""
    def __init__( self, par ):
        wx.Dialog.__init__( self, par, -1, '', size=(650,450), style=0 )
        #self.tabs = aui.AuiNotebook( self, style=aui.AUI_NB_TOP )
        #self.tabs.SetMinClientSize( wx.Size( 700, 700))
        self.tabs = wx.Notebook( self, -1 )
        self.AddFindTab( )
        self.AddBookmarksTab( )
        self.AddHeadingsTab( )
        sizer = wx.BoxSizer( wx.VERTICAL  )
        sizer.Add( self.tabs, 1, wx.EXPAND )
        self.SetSizer( sizer )
        self.Layout( )
        #wx.CallAfter(self.tabs.SendSizeEvent)

    def AddFindTab( self ):
        panel = wx.Panel( self.tabs, -1 )
        self.tabs.AddPage( panel, 'Find' )

    def AddBookmarksTab( self ):
        panel = wx.Panel( self.tabs, -1 )
        panel.SetBackgroundColour( wx.Colour( 244,244, 244 ))
        self.tabs.AddPage( panel, 'Bookmark' )
        inner_panel = wx.Panel( panel, -1 )
        inner_panel.SetBackgroundColour( wx.Colour( 236, 236, 236 ) )
        sizer = wx.BoxSizer( wx.VERTICAL )
        sizer.Add( inner_panel, 1, wx.EXPAND | wx.TOP|wx.LEFT|wx.RIGHT, 20 )
        panel.SetSizer( sizer )

        #add listbox with bookmarks
        inner_panel_sizer = wx.BoxSizer( wx.HORIZONTAL )
        bookmarks_sizer = wx.BoxSizer( wx.VERTICAL )
        st = wx.StaticText( inner_panel, -1, 'Bookmarks:' )
        bookmarks_sizer.Add( st, 0, wx.BOTTOM, 7 )
        list_choices = [ 'Bookmark 1', 'Bookmark X', 'Bookmark Y', 'Bookmark Z' ]
        self.list_bookmarks = wx.ListBox( inner_panel, -1, size=( 200, 200 ), choices=list_choices )
        bookmarks_sizer.Add( self.list_bookmarks, 0 )
        inner_panel_sizer.Add( bookmarks_sizer, 0, wx.TOP|wx.LEFT|wx.RIGHT, 50 )

        buttons_sizer = wx.BoxSizer( wx.VERTICAL )

        btn = wx.Button( inner_panel, -1, 'Go to bookmark', size=(100,-1) )
        buttons_sizer.Add( btn, 0, wx.BOTTOM, 7 )
        btn.Bind( wx.EVT_BUTTON, self.OnBookMarkBtn )

        btn = wx.Button( inner_panel, -1, 'Previous', size=(100,-1) )
        buttons_sizer.Add( btn, 0, wx.BOTTOM, 7 )
        btn.Bind( wx.EVT_BUTTON, self.OnBookMarkBtn )

        btn = wx.Button( inner_panel, -1, 'Previous', size=(100,-1) )
        buttons_sizer.Add( btn, 0, wx.BOTTOM, 7 )
        btn.Bind( wx.EVT_BUTTON, self.OnBookMarkBtn )

        btn = wx.Button( inner_panel, -1, 'Next', size=(100,-1) )
        buttons_sizer.Add( btn, 0, wx.BOTTOM, 7 )
        btn.Bind( wx.EVT_BUTTON, self.OnBookMarkBtn )

        btn = wx.Button( inner_panel, -1, 'Delete', size=(100,-1) )
        buttons_sizer.Add( btn, 0, wx.BOTTOM, 7 )
        btn.Bind( wx.EVT_BUTTON, self.OnBookMarkBtn )

        btn = wx.Button( inner_panel, -1, 'Delete All', size=(100,-1) )
        buttons_sizer.Add( btn, 0, wx.BOTTOM, 7 )
        btn.Bind( wx.EVT_BUTTON, self.OnBookMarkBtn )
        inner_panel_sizer.Add( ( 0,0 ), 1 )#Add extra
        inner_panel_sizer.Add( buttons_sizer, 0, wx.TOP|wx.LEFT, 70 )
        inner_panel_sizer.Add( 50, -1, 0 )
        inner_panel.SetSizer( inner_panel_sizer )
        inner_panel.Layout( )
        self.CreateBookmarkConfirmBtns( panel, sizer )
        panel.Layout( )

    #Create Confirm Buttons on the Bookmark tab
    def CreateBookmarkConfirmBtns( self, panel, sizer ):
        btn_sizer = wx.BoxSizer( wx.HORIZONTAL )
        btn_cancel = wx.Button( panel, -1, 'Cancel' )
        btn_cancel.Bind( wx.EVT_BUTTON, self.Close )
        btn_sizer.Add( btn_cancel, 0, wx.LEFT|wx.TOP|wx.BOTTOM, 20 )
        btn_add_new = wx.Button( panel, -1, 'Add New' )
        btn_sizer.Add( btn_add_new, 0, wx.LEFT|wx.TOP|wx.BOTTOM, 20 )
        sizer.Add( btn_sizer, 0,wx.ALIGN_RIGHT|wx.RIGHT, 20 )

    def Close( self, evt ):
        self.EndModal( -1 )
        self.Destroy( )


    def OnBookMarkBtn( self, evt ):
        wx.MessageBox( 'hello' )


    def AddHeadingsTab( self ):
        panel = wx.Panel( self.tabs, -1 )
        self.tabs.AddPage( panel, 'Heading' )
