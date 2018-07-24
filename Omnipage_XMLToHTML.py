Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: C:/Users/DEEP/Desktop/omnipage_ocr.py ===============
>>> 
=============== RESTART: C:/Users/DEEP/Desktop/omnipage_ocr.py ===============
>>> 
=============== RESTART: C:/Users/DEEP/Desktop/omnipage_ocr.py ===============
>>> 
=============== RESTART: C:/Users/DEEP/Desktop/omnipage_ocr.py ===============
>>> 
=============== RESTART: C:/Users/DEEP/Desktop/omnipage_ocr.py ===============
>>> from comtypes import client
>>> api = client.GetModule(r"C:\Program Files\Nuance\OPCaptureSDK20\Include\IproPlus.tlb")
>>> obj = client.CreateObject(api.Engine)
>>> obj.Init()
0
>>> doc = obj.Documents.Add()
>>> doc.Deskew = 4
>>> doc.AutoZoning_Form = True
>>> doc.AutoZoning_Column = 2
>>> z = doc.LoadImage(r"F:\c210k_pdf.pdf")
>>> obj.Converters
<POINTER(IConverters) ptr=0x3e66168 at 45835c8>
>>> lst = obj.Converters
>>> lst
<POINTER(IConverters) ptr=0x3e66168 at 45836c8>
>>> lst[0]
<POINTER(IConverter) ptr=0x4355670 at 45835c8>
>>> len(lst)
55
>>> lst[0].DisplayName
'MP3 Audio Premium Quality'
>>> lst[0].Name
'Converters.Text.Audiomp3'
>>> lst[0].Extension
'.mp3'
>>> lst[0].Property
<bound_named_property 'IConverter.Property' at 359f748>
>>> lst[0].Count
42
>>> for c in lst:
	print(c.DisplayName)

	
Traceback (most recent call last):
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 275, in __getattr__
    fixed_name = self.__map_case__[name.lower()]
KeyError: 'displayname'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    print(c.DisplayName)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 277, in __getattr__
    raise AttributeError(name)
AttributeError: DisplayName
>>> for i in range(len(lst))
SyntaxError: invalid syntax
>>> for i in range(len(lst)):
	print(lst[0].DisplayName)

	
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
MP3 Audio Premium Quality
>>> for i in range(len(lst)):
	print(lst[i].DisplayName)

	
MP3 Audio Premium Quality
Text - Comma Separated
Binary (DirectTXT)
Text - Comma Separated (DirectTXT)
Microsoft Word
PDF Searchable Image (DirectTXT)
Text (DirectTXT)
XML (DirectTXT)
ePub
Microsoft Excel XP, 2003
Text - Formatted
HTML 3.2
HTML 4.0
HTML 5
Kindle Document
PDF
PDF Edited
PDF Searchable Image
PDF with image substitutes
Microsoft PowerPoint 97
Microsoft PowerPoint
Microsoft Publisher 98
Microsoft Word 2000, XP
Text
Text with line breaks
Unicode Text - Comma Separated
Unicode Text - Formatted
Unicode Text
Unicode Text with line breaks
Microsoft Word 2003 (WordML)
WordPad
WordPerfect 12, X3
Microsoft Excel
XML
XPS
XPS Searchable Image
BMP - Windows Bitmap
DCX - Multi-page PaintBrush
GIF - CompuServe Bitmap
HDP - HD Photo Image
JB2 - JBIG 2 Bitmap
JPG - JPEG Bitmap
JP2 - JPEG 2000 Bitmap
MAX - PaperPort Image
OPG - OPCSDK Image
PCX - PaintBrush
PDF - PDF Image
PNG - Portable Network Graphics
TIF - TIFF Tag Image File Format
XPS - XPS Image
PDF and Word
Image PDF and TIFF
Word and Text
Word and TIFF
Text - Comma Separated
>>> obj.Converters
<POINTER(IConverters) ptr=0x3e66168 at 46f1f48>
>>> for i in range(len(lst)):
	print(lst[i].Name)

	
Converters.Text.Audiomp3
Converters.Text.Csv
Converters.Text.DBinary
Converters.Text.DCsv
Converters.Text.DocX
Converters.Text.DPDFImageOnText
Converters.Text.DText
Converters.Text.DXMLCoord
Converters.Text.ePub
Converters.Text.Excel2000
Converters.Text.FormattedTxt
Converters.Text.Html32
Converters.Text.Html40
Converters.Text.Html50
Converters.Text.Kindle
Converters.Text.PDF
Converters.Text.PDFEdited
Converters.Text.PDFImageOnText
Converters.Text.PDFImageSubst
Converters.Text.PowerPoint97
Converters.Text.PptX
Converters.Text.Publisher98
Converters.Text.RTF2000
Converters.Text.Text
Converters.Text.TextWithLinebreaks
Converters.Text.UCsv
Converters.Text.UFormattedTxt
Converters.Text.UText
Converters.Text.UTextWithLinebreaks
Converters.Text.WordML
Converters.Text.WordPad
Converters.Text.WordPerfect10
Converters.Text.XlsX
Converters.Text.XML
Converters.Text.XPS
Converters.Text.XPSsearchable
Converters.Image.BMP
Converters.Image.DCX
Converters.Image.GIF
Converters.Image.HDP
Converters.Image.JBIG2
Converters.Image.JPEG
Converters.Image.JPG2000
Converters.Image.MAX
Converters.Image.OPG
Converters.Image.PCX
Converters.Image.PDFIMG
Converters.Image.PNG
Converters.Image.TIFF
Converters.Image.XPSIMG
Converters.Multi.pdf_word2000
Converters.Multi.pdfimg_tiff
Converters.Multi.word2000_text
Converters.Multi.word2000_tiff
Converters.Form.CSV
>>> c = obj.Converters["Converters.Text.Html50")
SyntaxError: invalid syntax
>>> c = obj.Converters["Converters.Text.Html50"]
>>> c
<POINTER(IConverter) ptr=0x6f7e330 at 46420c8>
>>> c.FormattingLevel = 2
>>> WFhandle = doc.WFHandler()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    WFhandle = doc.WFHandler()
TypeError: 'POINTER(IWFHandler)' object is not callable
>>> WFhandle = doc.WFHandler
>>> WFhandle.ClearTempParams()
0
>>> WFhandle.SetTempParam(WFStepParameters.SP_PRO_AUTOPROOFREAD, false, false)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    WFhandle.SetTempParam(WFStepParameters.SP_PRO_AUTOPROOFREAD, false, false)
NameError: name 'WFStepParameters' is not defined
>>> WFhandle.AddWFInput(r"F:\c210k_pdf.pdf", null)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    WFhandle.AddWFInput(r"F:\c210k_pdf.pdf", null)
NameError: name 'null' is not defined
>>> WFhandle.AddWFInput(r"F:\c210k_pdf.pdf", NULL)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    WFhandle.AddWFInput(r"F:\c210k_pdf.pdf", NULL)
NameError: name 'NULL' is not defined
>>> WFhandle.AddWFInput(r"F:\c210k_pdf.pdf", Null)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    WFhandle.AddWFInput(r"F:\c210k_pdf.pdf", Null)
NameError: name 'Null' is not defined
>>> WFhandle.AddWFInput(r"F:\Image.jpg")
0
>>> WFhandle.AddWFOutput(r"F:\Output.txt", "Converters.Text.Html50")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    WFhandle.AddWFOutput(r"F:\Output.txt", "Converters.Text.Html50")
_ctypes.COMError: (-2147164923, None, ("The workflow doesn't need any output file.", None, '', 0, None))
>>> WFhandle.AddWFOutput(r"F:\Output.html", "Converters.Text.Html50")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    WFhandle.AddWFOutput(r"F:\Output.html", "Converters.Text.Html50")
_ctypes.COMError: (-2147164923, None, ("The workflow doesn't need any output file.", None, '', 0, None))
>>> WFhandle.AddWFOutput(r"F:\Output.html", r"Converters.Text.Html50")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    WFhandle.AddWFOutput(r"F:\Output.html", r"Converters.Text.Html50")
_ctypes.COMError: (-2147164923, None, ("The workflow doesn't need any output file.", None, '', 0, None))
>>> WFhandle.AddWFOutput("Converters.Text.Html50")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    WFhandle.AddWFOutput("Converters.Text.Html50")
TypeError: required argument 'ConverterName' missing
>>> WFhandle.AddWFOutput("Output.html", "Converters.Text.Html50")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    WFhandle.AddWFOutput("Output.html", "Converters.Text.Html50")
_ctypes.COMError: (-2147164923, None, ("The workflow doesn't need any output file.", None, '', 0, None))
>>> WFhandle.AddWFOutput("F:\Output.txt", "Converters.Text.Html50")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    WFhandle.AddWFOutput("F:\Output.txt", "Converters.Text.Html50")
_ctypes.COMError: (-2147164923, None, ("The workflow doesn't need any output file.", None, '', 0, None))
>>> oWFProcInfo = WFhandle.StartWorkflow(true, WFPROCMODE.WPM_REAL_MODE)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    oWFProcInfo = WFhandle.StartWorkflow(true, WFPROCMODE.WPM_REAL_MODE)
NameError: name 'true' is not defined
>>> oWFProcInfo = WFhandle.StartWorkflow(True, WFPROCMODE.WPM_REAL_MODE)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    oWFProcInfo = WFhandle.StartWorkflow(True, WFPROCMODE.WPM_REAL_MODE)
NameError: name 'WFPROCMODE' is not defined
>>> oWFProcInfo = WFhandle.StartWorkflow(True, 2)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    oWFProcInfo = WFhandle.StartWorkflow(True, 2)
_ctypes.COMError: (-2147164927, None, ('The starting of the active workflow has failed.', None, '', 0, None))
>>> 
