import clr
import os
import sys

clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReferenceToFileAndPath("C:\\Program Files (x86)\\Nuance\\OPCaptureSDK20\\Bin\\Nuance.OmniPage.CSDK.ArgTypes")
clr.AddReferenceToFileAndPath('C:\\Program Files (x86)\\Nuance\\OPCaptureSDK20\\Bin\\Nuance.OmniPage.CSDK.Objects')


from Nuance.OmniPage.CSDK.Objects import SettingCollection, Page, Image, Engine
from Nuance.OmniPage.CSDK.ArgTypes import RecAPIConstants, IMG_CONVERSION, DTXTOUTPUTFORMATS, IMAGEINDEX
from time import time, sleep
from datetime import datetime
from System.IO import Directory, Path, File
from System.Xml.Linq import XDocument
from System.Xml import XmlDocument

strInput = sys.argv[1]
strOutput = sys.argv[2]

Engine.Init('Nuance', 'Dragon OCR')
settings = SettingCollection()
page = Page(strInput, RecAPIConstants.IMGF_FIRSTPAGE, settings)
page.Preprocess()
page.Recognize()
##settings.DTXTOutputformat = DTXTOUTPUTFORMATS.DTXT_TXTS
settings.DTXTOutputformat = DTXTOUTPUTFORMATS.DTXT_XMLCOORD
page.Convert2DTXT(strOutput)

with open(strOutput,'r') as f:
        print(f.readlines())

File.Delete(strOutput)

Engine.ForceQuit()		
		
