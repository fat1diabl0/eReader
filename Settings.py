# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import cv2
import SettingsData

###########################################################################
## Class dlgSettings
###########################################################################

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
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Preferred Scanner:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer111.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer8.Add( bSizer111, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer121 = wx.BoxSizer( wx.VERTICAL )
		
		choScannerChoices = []
		
		for i in range(len(SettingsData.lstOfCam)):
			choScannerChoices.append(SettingsData.lstOfCam[i])

		self.choScanner = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), choScannerChoices, 0 )

		IsFound = False
		for i in range(len(SettingsData.lstOfCam)):
			if SettingsData.PreferredScanner in SettingsData.lstOfCam[i]:
				self.choScanner.SetStringSelection(SettingsData.lstOfCam[i])
				SettingsData.camID = i
				IsFound = True

		if not IsFound:
			if len(SettingsData.lstOfCam) == 1:
				self.choScanner.SetStringSelection(SettingsData.lstOfCam[0])
				SettingsData.camID = 0

		self.choScanner.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer121.Add( self.choScanner, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer8.Add( bSizer121, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer8, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		zbcSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.txtFontLabel = wx.StaticText( self, wx.ID_ANY, u"Select Font:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtFontLabel.Wrap( -1 )
		self.txtFontLabel.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		zbcSizer.Add( self.txtFontLabel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		# bSizer111.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer12.Add( zbcSizer, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		# print(SettingsData.FontSize)
		# self.btnFontPicker = wx.FontPickerCtrl( self, wx.ID_ANY, wx.Font( 24, 70, 90, 90, False, "Helvetica" ), wx.DefaultPosition, wx.Size( 150,-1 ), wx.FNTP_FONTDESC_AS_LABEL )
		# self.btnFontPicker.SetMaxPointSize( 100 ) 
		self.btnFontPicker = wx.Button( self, wx.ID_ANY, u"Select Font", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.btnFontPicker.Bind( wx.EVT_BUTTON, self.onSelectFont )
		bSizer15.Add( self.btnFontPicker, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		# self.btnFontPicker.SetLabel(SettingsData.Font + ',' + str(SettingsData.FontSize))
		self.btnFontPicker.SetForegroundColour(SettingsData.FontColor)			
		
		
		bSizer12.Add( bSizer15, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( bSizer12, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Save Captured Images?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer16.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.BOTTOM, 5 )
		
		
		bSizer91.Add( bSizer16, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		choSaveImagesChoices = [ u"No", u"Yes", wx.EmptyString ]
		self.choSaveImages = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), choSaveImagesChoices, 0 )
		self.choSaveImages.SetStringSelection( SettingsData.IsSaveImages )
		self.choSaveImages.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		
		bSizer17.Add( self.choSaveImages, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 1 )
		
		
		bSizer91.Add( bSizer17, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Select OCR Method:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer18.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		
		bSizer101.Add( bSizer18, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		choOCRMethodChoices = [ u"OmniPage", u"Google"]
		self.choOCRMethod = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), choOCRMethodChoices, 0 )
		self.choOCRMethod.SetStringSelection( SettingsData.OCRMethod )
		bSizer19.Add( self.choOCRMethod, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer101.Add( bSizer19, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
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
		
		self.btnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCancel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.onCancel )
		
		bSizer11.Add( self.btnCancel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.RIGHT, 5 )
		
		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnSave.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.btnSave.Bind( wx.EVT_BUTTON, self.onSave )
		# self.btnSave.SetFocus()
		
		bSizer11.Add( self.btnSave, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.RIGHT, 5 )
		
		
		bSizer9.Add( bSizer11, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 5 )
		
		
		bSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUP)
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		settingsFilePath = os.path.join(os.getcwd(),"Settings.dat")
		if os.path.exists(settingsFilePath):
			with open(settingsFilePath,'r') as f:
				lines = f.readlines()
				for l in lines:
					fields = l.split(':')
					if fields[0] == "PreferredScanner":
						SettingsData.PreferredScanner = fields[1].strip()
					elif fields[0] == "Font":
						SettingsData.Font = fields[1].strip()
					elif fields[0] == "FontSize":
						SettingsData.FontSize = fields[1].strip()
					elif fields[0] == "FontColor":
						c = wx.Colour(int(fields[1].strip()))
						SettingsData.FontColor = c
					elif fields[0] == "IsSaveImages":
						SettingsData.IsSaveImages = fields[1].strip()
					elif fields[0] == "OCRMethod":
						SettingsData.OCRMethod = fields[1].strip()		

		# print(SettingsData.FontSize)
		self.choScanner.SetStringSelection( SettingsData.PreferredScanner )
		self.btnFontPicker.SetLabel(SettingsData.Font + ',' + str(SettingsData.FontSize))
		self.btnFontPicker.SetForegroundColour(SettingsData.FontColor)
		self.choSaveImages.SetStringSelection( SettingsData.IsSaveImages )
		self.choOCRMethod.SetStringSelection( SettingsData.OCRMethod )

		self.choScanner.SetFocus()	

	def __del__( self ):
		pass
	
	def OnKeyUP(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_ESCAPE:
			self.Close()
		else:
			event.Skip() 		

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
		self.choOCRMethod.SetStringSelection( SettingsData.Default_OCRMethod )

		SettingsData.PreferredScanner = SettingsData.Default_PreferredScanner	
		SettingsData.Font = SettingsData.Default_Font	
		SettingsData.FontSize = SettingsData.Default_FontSize	
		SettingsData.FontColor = SettingsData.Default_FontColor
		SettingsData.IsSaveImages = SettingsData.Default_IsSaveImages	
		SettingsData.OCRMethod = SettingsData.Default_OCRMethod	

	def onSave(self,evt):
		SettingsData.PreferredScanner 	= self.choScanner.GetStringSelection()
		SettingsData.IsSaveImages 		= self.choSaveImages.GetStringSelection()
		SettingsData.OCRMethod 		= self.choOCRMethod.GetStringSelection()

		btnLabel = self.btnFontPicker.GetLabel()
		fgColor = self.btnFontPicker.GetForegroundColour()

		fname = (btnLabel.split(',')[0]).strip()
		pntSize = btnLabel.split(',')[1]
		SettingsData.Font 			= fname
		SettingsData.FontSize 		= int(pntSize)
		SettingsData.FontColor 		= fgColor

		settingsFilePath = os.path.join(os.getcwd(),"Settings.dat")
		
		with open(settingsFilePath,'w') as f:
			f.write("PreferredScanner:"+SettingsData.PreferredScanner+"\n")
			f.write("Font:"+SettingsData.Font+"\n")
			f.write("FontSize:"+str(SettingsData.FontSize)+"\n")
			f.write("FontColor:"+str(SettingsData.FontColor.GetRGB())+"\n")
			f.write("IsSaveImages:"+SettingsData.IsSaveImages+"\n")
			f.write("OCRMethod:"+SettingsData.OCRMethod+"\n")

		self.Destroy()

	def onCancel(self,evt):
		self.Destroy( )	

