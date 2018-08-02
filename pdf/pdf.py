Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pdfkit
>>> pdfkit.from_string("abc",r"F:\out.pdf")
Traceback (most recent call last):
  File "C:\Program Files\Python35\lib\site-packages\pdfkit\configuration.py", line 21, in __init__
    with open(self.wkhtmltopdf) as f:
FileNotFoundError: [Errno 2] No such file or directory: b''

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pdfkit.from_string("abc",r"F:\out.pdf")
  File "C:\Program Files\Python35\lib\site-packages\pdfkit\api.py", line 70, in from_string
    configuration=configuration, cover_first=cover_first)
  File "C:\Program Files\Python35\lib\site-packages\pdfkit\pdfkit.py", line 42, in __init__
    self.configuration = (Configuration() if configuration is None
  File "C:\Program Files\Python35\lib\site-packages\pdfkit\configuration.py", line 27, in __init__
    'https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf' % self.wkhtmltopdf)
OSError: No wkhtmltopdf executable found: "b''"
If this file exists please check that this process can read it. Otherwise please install wkhtmltopdf - https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
>>> import wkhtmltopdf
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import wkhtmltopdf
  File "C:\Program Files\Python35\lib\site-packages\wkhtmltopdf\__init__.py", line 1, in <module>
    from main import WKhtmlToPdf, wkhtmltopdf
ImportError: No module named 'main'
>>> import pypdf2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import pypdf2
ImportError: No module named 'pypdf2'
>>> import PyPDF2
>>> writer=PdfFileWriter()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    writer=PdfFileWriter()
NameError: name 'PdfFileWriter' is not defined
>>> writer=PyPDF2.PdfFileWriter()
>>> outfp=open(r"F:\outpath",'wb')
>>> writer.write(outfp)
>>> outfp.close()
>>> outfp=open(r"F:\outpath.pdf",'wb')
>>> writer.write(outfp)
>>> outfp.close()
>>> from reportlab.pdfgen import canvas
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    from reportlab.pdfgen import canvas
ImportError: No module named 'reportlab'
>>> from reportlab.pdfgen import canvas
>>> from reportlab.lib.pagesizes import letter
>>> packet = io.BytesIO()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    packet = io.BytesIO()
NameError: name 'io' is not defined
>>> import io
>>> packet = io.BytesIO()
>>> can = canvas.Canvas(packet, pagesize=letter)
>>> can.setFont('Helvetica-Bold', 24)
>>> can.drawString(10, 100, "Hello world")
>>> can.showPage()
>>> 
