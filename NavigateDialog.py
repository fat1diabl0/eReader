# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class dlgNavigate
###########################################################################

class NavigateDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Envision Reader", pos = wx.DefaultPosition, size = wx.Size( 485,320 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.ImportScreen = parent

		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panBookmark = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.searchBookmark = wx.SearchCtrl( self.panBookmark, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchBookmark.ShowSearchButton( True )
		self.searchBookmark.ShowCancelButton( True )
		bSizer9.Add( self.searchBookmark, 0, wx.ALL|wx.EXPAND, 5 )
		
		lstBoxBookmarkChoices = list(self.ImportScreen.dictBookmarkData.keys())
		self.lstBoxBookmark = wx.ListBox( self.panBookmark, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lstBoxBookmarkChoices, wx.LB_NEEDED_SB )
		bSizer9.Add( self.lstBoxBookmark, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		
		#bSizer10.AddSpacer( wx.DefaultSize, 0, wx.EXPAND, 5 )
		
		self.btnBMGo = wx.Button( self.panBookmark, wx.ID_ANY, u"Go To Bookmark", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnBMGo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.btnBMPrevious = wx.Button( self.panBookmark, wx.ID_ANY, u"Previous", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnBMPrevious, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnBMNext = wx.Button( self.panBookmark, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnBMNext, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnBMDelete = wx.Button( self.panBookmark, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnBMDelete, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnBMDeleteAll = wx.Button( self.panBookmark, wx.ID_ANY, u"Delete All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnBMDeleteAll, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer8.Add( bSizer10, 1, wx.EXPAND|wx.ALIGN_BOTTOM|wx.TOP, 5 )
		
		
		self.panBookmark.SetSizer( bSizer8 )
		self.panBookmark.Layout()
		bSizer8.Fit( self.panBookmark )
		self.m_notebook1.AddPage( self.panBookmark, u"Bookmark", True )
		self.pnlHeading = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.searchHeading = wx.SearchCtrl( self.pnlHeading, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchHeading.ShowSearchButton( True )
		self.searchHeading.ShowCancelButton( True )
		bSizer12.Add( self.searchHeading, 0, wx.ALL|wx.EXPAND, 5 )
		
		lstBoxHeadingChoices = []
		self.lstBoxHeading = wx.ListBox( self.pnlHeading, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lstBoxHeadingChoices, wx.LB_NEEDED_SB )
		bSizer12.Add( self.lstBoxHeading, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		
		#bSizer13.AddSpacer( ( 0, 25), 0, 0, 5 )
		
		self.btnHeadGo = wx.Button( self.pnlHeading, wx.ID_ANY, u"Go To Heading", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.btnHeadGo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.btnHeadPrevious = wx.Button( self.pnlHeading, wx.ID_ANY, u"Previous", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.btnHeadPrevious, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnHeadNext = wx.Button( self.pnlHeading, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.btnHeadNext, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer13, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )
		
		
		self.pnlHeading.SetSizer( bSizer11 )
		self.pnlHeading.Layout()
		bSizer11.Fit( self.pnlHeading )
		self.m_notebook1.AddPage( self.pnlHeading, u"Headings", False )
		
		bSizer7.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnCancel, 0, wx.ALL, 5 )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.OnClose )
		
		bSizer1.Add( bSizer4, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		
		# Connect Events
		self.m_notebook1.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnTabChanged )
		self.btnBMGo.Bind( wx.EVT_BUTTON, self.OnGoToBookmark )
		self.btnBMPrevious.Bind( wx.EVT_BUTTON, self.OnBMPrevious )
		self.btnBMNext.Bind( wx.EVT_BUTTON, self.OnBMNext )
		self.btnBMDelete.Bind( wx.EVT_BUTTON, self.OnBMDelete )
		self.btnBMDeleteAll.Bind( wx.EVT_BUTTON, self.OnBMDeleteAll )
		self.btnHeadGo.Bind( wx.EVT_BUTTON, self.OnGoToHeading )
		self.btnHeadPrevious.Bind( wx.EVT_BUTTON, self.OnHeadingPrevious )
		self.btnHeadNext.Bind( wx.EVT_BUTTON, self.OnHeadingNext )
		self.searchBookmark.Bind( wx.EVT_TEXT_ENTER, self.OnBMSearchEnter )
		self.searchBookmark.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnBMSearchEnter )
		self.searchBookmark.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnBMSearchCancel )

	def __del__( self ):
		pass

	def OnTabChanged( self, event ):
		page = self.m_notebook1.GetPageText(event.GetSelection())
		#print(page)
	
	def OnBMSearchEnter( self , evt ):
		strSearchVal = evt.GetString().strip()

		if len(strSearchVal) != 0:
			if strSearchVal in self.ImportScreen.dictBookmarkData.keys():
			
				self.lstBoxBookmark.Clear()
				lstBoxBookmarkChoices = [strSearchVal]
				self.lstBoxBookmark.InsertItems(lstBoxBookmarkChoices,0)				

	def OnBMSearchCancel( self , evt ):
		self.searchBookmark.Clear()
		self.lstBoxBookmark.Clear()
		lstBoxBookmarkChoices = list(self.ImportScreen.dictBookmarkData.keys())
		if len(lstBoxBookmarkChoices) > 0:
			self.lstBoxBookmark.InsertItems(lstBoxBookmarkChoices,0)	

	def OnGoToBookmark( self, event ):
		intSelectedIndex = self.lstBoxBookmark.GetSelection()
		strBMName  = self.lstBoxBookmark.GetString(intSelectedIndex)
		strPageName = self.ImportScreen.dictBookmarkData[strBMName][0]
		strBMText = self.ImportScreen.dictBookmarkData[strBMName][1]

		self.ImportScreen.UpdateHTMLPage(strPageName)
	
	def OnBMPrevious( self, event ):
		intSelectedIndex = self.lstBoxBookmark.GetSelection()

		if intSelectedIndex > 0:
			newIndex = intSelectedIndex - 1
			self.lstBoxBookmark.SetSelection(newIndex)

			strBMName  = self.lstBoxBookmark.GetString(newIndex)
			strPageName = self.ImportScreen.dictBookmarkData[strBMName][0]
			strBMText = self.ImportScreen.dictBookmarkData[strBMName][1]

			self.ImportScreen.UpdateHTMLPage(strPageName)
	
	def OnBMNext( self, event ):
		intSelectedIndex = self.lstBoxBookmark.GetSelection()
		
		if intSelectedIndex < len(self.ImportScreen.dictBookmarkData.keys()) - 1:
			newIndex = intSelectedIndex + 1
			self.lstBoxBookmark.SetSelection(newIndex)

			strBMName  = self.lstBoxBookmark.GetString(newIndex)
			strPageName = self.ImportScreen.dictBookmarkData[strBMName][0]
			strBMText = self.ImportScreen.dictBookmarkData[strBMName][1]

			self.ImportScreen.UpdateHTMLPage(strPageName)

	def OnBMDelete( self, event ):
		intSelectedIndex = self.lstBoxBookmark.GetSelection()
		
		if intSelectedIndex > 0:
			strBMName  = self.lstBoxBookmark.GetString(intSelectedIndex)
			del self.ImportScreen.dictBookmarkData[strBMName]

			self.lstBoxBookmark.Clear()
			lstBoxBookmarkChoices = list(self.ImportScreen.dictBookmarkData.keys())
			self.lstBoxBookmark.InsertItems(lstBoxBookmarkChoices,0)			
	
	def OnBMDeleteAll( self, event ):
		self.ImportScreen.dictBookmarkData.clear()
		self.lstBoxBookmark.Clear()
	
	def OnGoToHeading( self, event ):
		event.Skip()
	
	def OnHeadingPrevious( self, event ):
		event.Skip()
	
	def OnHeadingNext( self, event ):
		event.Skip()
		
	def OnClose( self , evt ):
		self.Destroy()

