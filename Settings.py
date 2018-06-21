# -*- coding: utf-8 -*- 

import wx
import cv2
import wx.xrc
import SettingsData

class SettingsDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Envision Reader", pos = wx.DefaultPosition, size = wx.Size( 520,260 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Settings Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 16, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer1.AddStretchSpacer(1)
		bSizer1.AddStretchSpacer(1)
		
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Preferred Scanner:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer8.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		bSizer8.AddStretchSpacer(1)
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Select Font:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer8.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
				
		bSizer8.AddStretchSpacer(1)
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Save Captured Images?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer8.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL|wx.BOTTOM, 5 )
		
		
		bSizer3.Add( bSizer8, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		choScannerChoices = []
		
		self.noOfCam = self.getConnectedCams()
		# print(self.noOfCam)
		if self.noOfCam  > 1:
			choScannerChoices.append("USB Cam")
			choScannerChoices.append("Web Cam")
		else:
			choScannerChoices.append("Web Cam")
			
		self.choScanner = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), choScannerChoices, 0 )
		if self.noOfCam > 1:
			self.choScanner.SetStringSelection( SettingsData.PreferredScanner )
		else:
			self.choScanner.SetStringSelection("Web Cam")
			
		self.choScanner.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer12.Add( self.choScanner, 1, wx.ALL, 1 )
		
		bSizer12.AddStretchSpacer(1)
				
		self.btnFontPicker = wx.Button( self, wx.ID_ANY, u"Select Font", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.btnFontPicker.Bind( wx.EVT_BUTTON, self.onSelectFont )
		bSizer12.Add( self.btnFontPicker, 0, wx.BOTTOM, 5 )	
		self.btnFontPicker.SetLabel(SettingsData.Font + ',' + str(SettingsData.FontSize))
		self.btnFontPicker.SetForegroundColour(SettingsData.FontColor)			

		bSizer12.AddStretchSpacer(1)
		
		choSaveImagesChoices = [ u"No", u"Yes"]
		self.choSaveImages = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), choSaveImagesChoices, 0 )
		self.choSaveImages.SetStringSelection( SettingsData.IsSaveImages )
		self.choSaveImages.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer12.Add( self.choSaveImages, 0, wx.ALL, 1 )
		
		bSizer3.Add( bSizer12, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		
		bSizer1.AddStretchSpacer(1)
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnDefault = wx.Button( self, wx.ID_ANY, u"Restore Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnDefault.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.btnDefault.Bind( wx.EVT_BUTTON, self.onRestoreDefaults )
		
		bSizer10.Add( self.btnDefault, 0, wx.ALL, 5 )
		
		bSizer9.Add( bSizer10, 0, wx.ALIGN_LEFT|wx.TOP, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer11.AddStretchSpacer(1)
		bSizer11.AddStretchSpacer(1)
		
		self.btnCancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCancel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.onCancel )
		
		bSizer11.Add( self.btnCancel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.RIGHT, 5 )
		
		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnSave.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.btnSave.Bind( wx.EVT_BUTTON, self.onSave )
		
		bSizer11.Add( self.btnSave, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.RIGHT, 5 )
		
		
		bSizer9.Add( bSizer11, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 5 )
		
		
		bSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

	def getConnectedCams(self):
		max_tested = 10
		for i in range(max_tested):
			temp_camera = cv2.VideoCapture(i)
			if temp_camera.isOpened():
				temp_camera.release()
				continue
			return i 

	def onSelectFont(self,evt):
		btnLabel = self.btnFontPicker.GetLabel()
		fgColor = self.btnFontPicker.GetForegroundColour()

		fname = (btnLabel.split(',')[0]).strip()
		pntSize = btnLabel.split(',')[1]
		data = wx.FontData()
		f = wx.Font(pointSize = int(pntSize), family=wx.FONTFAMILY_DEFAULT, style = wx.FONTSTYLE_NORMAL, weight = wx.FONTWEIGHT_NORMAL, underline=False,faceName = fname, encoding=wx.FONTENCODING_DEFAULT)
		data.SetInitialFont(f)
		data.SetColour(fgColor)
		dialog = wx.FontDialog(self, data)

		if dialog.ShowModal() == wx.ID_OK:
			retData = dialog.GetFontData()
			font = retData.GetChosenFont()
			color = retData.GetColour()
			self.btnFontPicker.SetLabel(font.GetFaceName() + ',' + str(font.GetPointSize()))
			self.btnFontPicker.SetForegroundColour(color)

	def onRestoreDefaults(self,evt):
		self.choScanner.SetStringSelection( SettingsData.Default_PreferredScanner )
		self.btnFontPicker.SetLabel(SettingsData.Default_Font + ',' + str(SettingsData.Default_FontSize))
		self.btnFontPicker.SetForegroundColour(SettingsData.Default_FontColor)
		self.choSaveImages.SetStringSelection( SettingsData.Default_IsSaveImages )

		SettingsData.PreferredScanner = SettingsData.Default_PreferredScanner	
		SettingsData.Font = SettingsData.Default_Font	
		SettingsData.FontSize = SettingsData.Default_FontSize	
		SettingsData.FontColor = SettingsData.Default_FontColor
		SettingsData.IsSaveImages = SettingsData.Default_IsSaveImages	

	def onSave(self,evt):
		SettingsData.PreferredScanner 	= self.choScanner.GetStringSelection()
		SettingsData.IsSaveImages 		= self.choSaveImages.GetStringSelection()

		btnLabel = self.btnFontPicker.GetLabel()
		fgColor = self.btnFontPicker.GetForegroundColour()

		fname = (btnLabel.split(',')[0]).strip()
		pntSize = btnLabel.split(',')[1]
		SettingsData.Font 			= fname
		SettingsData.FontSize 		= int(pntSize)
		SettingsData.FontColor 		= fgColor

		self.Destroy()

	def onCancel(self,evt):
		self.Destroy( )
