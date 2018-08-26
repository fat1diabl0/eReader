# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyDialog1
###########################################################################

class clsShortCuts ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Shortcuts", pos = wx.DefaultPosition, size = wx.Size( 255,320 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Take Photo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Timer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"FindReplace", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Bookmarks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Navigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"SettingsDialog", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Back Button", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer5.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"CTRL + I", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"CTRL + SPACE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"CTRL + D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"CTRL + T", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"CTRL + S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"CTRL + F", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_staticText23.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"CTRL + B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"CTRL + H", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"CTRL + X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		self.m_staticText26.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"CTRL + BACKSPACE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		self.m_staticText27.SetFont( wx.Font( 10, 74, 90, 90, False, "Helvetica" ) )
		bSizer6.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUP)

		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

	def OnKeyUP(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_ESCAPE:
			self.Close()
		else:
			event.Skip() 		
	

if __name__ == '__main__':
    app = wx.App(False)
    dlg = clsShortCuts(None)
    dlg.Show()
    app.MainLoop()
