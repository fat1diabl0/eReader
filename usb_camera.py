from ctypes import POINTER
import comtypes.client
try:
    comtypes.client.GetModule(r'F:\Upwork\Projects\Camera Tool\eReader-master\tlb\\DirectShow.tlb')
except:
    print("Direct Show Library Not Found.")


    
CLSID_SystemDeviceEnum = comtypes.GUID('{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}')
CLSID_VideoInputDeviceCategory = comtypes.GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}")

fg = comtypes.client.CreateObject(CLSID_SystemDeviceEnum,clsctx=comtypes.CLSCTX_INPROC_SERVER,interface=comtypes.gen.DirectShowLib.ICreateDevEnum)
class_enum  = fg.CreateClassEnumerator(CLSID_VideoInputDeviceCategory,0)

print(type(class_enum))

try:
    (moniker, fetched) = class_enum.RemoteNext(1)
    print(type(moniker))
except ValueError:
    print("Device Not Found")
        

##print(fetched)

null_context = POINTER(comtypes.gen.DirectShowLib.IBindCtx)()
null_moniker = POINTER(comtypes.gen.DirectShowLib.IMoniker)()

qi = moniker.QueryInterface(comtypes.gen.DirectShowLib.IPropertyBag)
print(type(qi))
##source = moniker.RemoteBindToObject(null_context,null_moniker,comtypes.gen.DirectShowLib.IBaseFilter._iid_)

source = moniker.RemoteBindToStorage(null_context,null_moniker,qi._iid_)

print(type(source))


##print(qi)

vtValue = comtypes.automation.VARIANT('dwt')
vtValue.vt = comtypes.automation.VT_BSTR

##qi.Read("FriendlyName",vtValue,None)
qi.Read("FriendlyName",comtypes.addressof(vtValue),None)
##qi.Read("Description",comtypes.addressof(vtValue),0)
##qi.Read("DevicePath",vtValue,0)

print(vtValue)
