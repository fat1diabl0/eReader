import comtypes
import comtypes.client
try:
    comtypes.client.GetModule(r'C:\Users\20050093\Desktop\Test\pyPlayer-master\tlb\\DirectShow.tlb')
except:
    print("Direct Show Library Not Found.")


    
CLSID_SystemDeviceEnum = comtypes.GUID('{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}')
CLSID_VideoInputDeviceCategory = comtypes.GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}")

fg = comtypes.client.CreateObject(CLSID_SystemDeviceEnum,clsctx=comtypes.CLSCTX_INPROC_SERVER,interface=comtypes.gen.DirectShowLib.ICreateDevEnum)
class_enum  = fg.CreateClassEnumerator(CLSID_VideoInputDeviceCategory,0)

try:
    (moniker, fetched) = class_enum.RemoteNext(1)
except ValueError:
    raise RuntimeError("Device not found")


qi = moniker.QueryInterface(comtypes.gen.DirectShowLib.IPropertyBag)

vtValue = comtypes.automation.VARIANT()
vtValue.vt = comtypes.automation.VT_BSTR

qi.Read("FriendlyName",comtypes.addressof(vtValue),None)

print(vtValue.value)
