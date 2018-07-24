# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import re


class BookmarkDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 271,100 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enter Bookmark Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ctrlBMName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.ctrlBMName, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnBMNameCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnBMNameCancel, 0, wx.ALL, 5 )
		
		self.btnBMNameOk = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnBMNameOk, 0, wx.ALL, 5 )
		
		self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUP)
		
		bSizer1.Add( bSizer3, 0, wx.ALIGN_RIGHT, 5 )
		
		self.Centre( wx.BOTH )

		self.SetSizer( bSizer1 )
		self.Layout()

		self.ImportScreen = parent
		
		# Connect Events
		self.btnBMNameCancel.Bind( wx.EVT_BUTTON, self.OnBMNameCancel )
		self.btnBMNameOk.Bind( wx.EVT_BUTTON, self.OnBMNameOK )
	
	def __del__( self ):
		pass
	
	def OnKeyUP(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_ESCAPE:
			self.Close()
		else:
			event.Skip() 

	# Virtual event handlers, overide them in your derived class
	def OnBMNameCancel( self, event ):
		self.Destroy()
	
	def OnBMNameOK( self, event ):
		strBMName = self.ctrlBMName.GetValue().strip()
		
		if len(strBMName) != 0:

			if strBMName in self.ImportScreen.dictBookmarkData.keys():
				wx.MessageBox("Bookmark Name already exist.")
			else:
				strSelectedText = self.ImportScreen.html_widget.GetSelectedText().strip()
				strPageName = self.ImportScreen.activeButton
				
				if(len(strSelectedText) == 0):
					wx.MessageBox("Please select any text to bookmark.")
				else:
					self.ImportScreen.dictBookmarkData[strBMName] = (strPageName,strSelectedText)
					self.ImportScreen.html_widget.ClearSelection()

					strPageSource = self.ImportScreen.html_widget.GetPageSource()
					# print(strPageSource.encode("utf-8"))

					charBefore = (strPageSource.partition(strSelectedText)[0].strip())[-1]
					charAfter  = (strPageSource.partition(strSelectedText)[2].strip())[0]
					# print(charBefore)
					# print(charAfter)

					if charBefore != '>' and charAfter != '<':
						strReplace = r"</p> <p aria-label="+strBMName+" role=navigation> "+strSelectedText+" </p><p>"
						#strReplace = r"</p> <div aria-label="+strBMName+" role=navigation> "+strSelectedText+" </div><p>"
						#strReplace = r"</p> <span aria-label="+strBMName+" role=navigation> "+strSelectedText+" </span><p>"
					else:
						strReplace = r"<p aria-label="+strBMName+" role=navigation> "+strSelectedText+" </p>"

					# strReplace = r"<p aria-label="+strBMName+" role=navigation> "+strSelectedText+" </p>"
					result = str.replace(strPageSource,strSelectedText,strReplace,1)
					# print(result.encode("utf-8"))
					self.ImportScreen.parent_frame.dictImgOCR[strPageName] = result
					self.ImportScreen.UpdateHTMLPage(strPageName)

					# print(re.findall(r"(?i)"+strSelectedText, strPageSource))

					self.Destroy()
					
		else:
			wx.MessageBox("Please enter bookmark Name.")
	

