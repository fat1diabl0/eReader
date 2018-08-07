import os

try:
	from comtypes import client
	api = client.GetModule(r"C:\Program Files\Nuance\OPCaptureSDK20\Include\IproPlus.tlb")	
except:
	print("Comtypes is not installed on your system or Please update path in OCR-mod-command.py file.")


def GetOCRByOmniPage(strInput):
	obj = client.CreateObject(api.Engine)
	obj.Init()
	
	doc = obj.Documents.Add()
	
	doc.Deskew = 4
	doc.AutoZoning_Form = True
	doc.AutoZoning_Column = 2	

	z = doc.LoadImage(strInput)
	
	strOutput = os.path.join(os.getcwd(),"output.txt")
	z.ConvertToDirectTXT(strOutput,0)
	
	strOutputXML = os.path.join(os.getcwd(),"Omnipage_XML_Output.xml")
	z.ConvertToDirectTXT(strOutputXML,4)

	strText = ""
	if os.path.exists(strOutput):
		with open(strOutput,'r') as f:
			strText = f.readlines()
		
		strText = ''.join(strText)
		# print(strText)
		os.remove(strOutput)

		return strText
	else:
		print("Output file did not generated by Omnipage.")
		return ""

	
# if __name__ == "__main__":
# 	print(GetOCRByOmniPage(r"F:\manoj_resume.pdf").encode('utf-8'))
