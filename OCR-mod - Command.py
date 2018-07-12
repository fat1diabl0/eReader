import clr
import os
import sys

clr.AddReference("C:\\Program Files\\Nuance\\OPCaptureSDK20\\Bin64\\Nuance.OmniPage.CSDK.ArgTypes.dll")
clr.AddReference("C:\\Program Files\\Nuance\\OPCaptureSDK20\\Bin64\\Nuance.OmniPage.CSDK.Objects.dll")

from Nuance.OmniPage.CSDK.Objects import SettingCollection, Page, Image, Engine, ImageFile
from Nuance.OmniPage.CSDK.ArgTypes import RecAPIConstants, IMG_CONVERSION, DTXTOUTPUTFORMATS, IMAGEINDEX
from System.Xml.Linq import XDocument
from System.Xml import XmlDocument

strInput = sys.argv[1]
strOutput = sys.argv[2]

print(strInput)
print(strOutput)

Engine.Init('Nuance', 'Dragon OCR')

settings = SettingCollection()
page = Page(strInput, RecAPIConstants.IMGF_FIRSTPAGE, settings)
page.Preprocess()

settings.DTXTOutputformat = DTXTOUTPUTFORMATS.DTXT_TXTF
# settings.DTXTOutputformat = DTXTOUTPUTFORMATS.DTXT_XMLCOORD
page.Recognize(strOutput)
# page.Convert2DTXT(strOutput)
# Engine.ForceQuit()

