Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import comtypes.client
>>> comtypes.client.GetModule(r'F:\Upwork\Projects\Camera Tool\eReader-master\tlb\\DirectShow.tlb')
<module 'comtypes.gen._24BC6711_3881_420F_8299_34DA1026D31E_0_1_0' from 'C:\\Program Files\\Python35\\lib\\site-packages\\comtypes\\gen\\_24BC6711_3881_420F_8299_34DA1026D31E_0_1_0.py'>
>>> CLSID_SystemDeviceEnum = comtypes.GUID('{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}')
>>> CLSID_VideoInputDeviceCategory = comtypes.GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}")
>>> fg = comtypes.client.CreateObject(CLSID_SystemDeviceEnum,clsctx=comtypes.CLSCTX_INPROC_SERVER,interface=comtypes.gen.DirectShowLib.ICreateDevEnum)
>>> class_enum  = fg.CreateClassEnumerator(CLSID_VideoInputDeviceCategory,0)
>>> (moniker, fetched) = class_enum.RemoteNext(1)
>>> type(moniker)
<class 'comtypes.POINTER(IMoniker)'>
>>> type(fetched)
<class 'int'>
>>> fetched
1
>>> moniker.GetDisplayName()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    moniker.GetDisplayName()
TypeError: required argument 'pbc' missing
>>> moniker.value
<POINTER(IMoniker) ptr=0x5aae90 at 4aac1c8>
>>> moniker.GetClassID()
GUID("{4315D437-5B8C-11D0-BD3B-00A0C911CE86}")
>>> moniker.ComposeWith()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    moniker.ComposeWith()
TypeError: required argument 'pmkRight' missing
>>> null_context = POINTER(comtypes.gen.DirectShowLib.IBindCtx)()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    null_context = POINTER(comtypes.gen.DirectShowLib.IBindCtx)()
NameError: name 'POINTER' is not defined
>>> from ctypes import POINTER
>>> null_context = POINTER(comtypes.gen.DirectShowLib.IBindCtx)()
>>> null_moniker = POINTER(comtypes.gen.DirectShowLib.IMoniker)()
>>> source = moniker.RemoteBindToObject(null_context,null_moniker,comtypes.gen.DirectShowLib.IBaseFilter._iid_)
>>> type(source)
<class 'comtypes.POINTER(IUnknown)'>
>>> moniker.GetDisplayName(source)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    moniker.GetDisplayName(source)
TypeError: required argument 'pmkToLeft' missing
>>> moniker.GetDisplayName(source,None)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    moniker.GetDisplayName(source,None)
ctypes.ArgumentError: argument 1: <class '_ctypes.COMError'>: (-2147467262, 'No such interface supported', (None, None, None, 0, None))
>>> type(null_context)
<class 'comtypes.POINTER(IBindCtx)'>
>>> type(null_moniker)
<class 'comtypes.POINTER(IMoniker)'>
>>> moniker.GetDisplayName(null_context,null_moniker)
'@device:pnp:\\\\?\\usb#vid_0c45&pid_63ee&mi_00#6&f7809e4&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global'
>>> moniker.IsRunning()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    moniker.IsRunning()
TypeError: required argument 'pbc' missing
>>> moniker.IsRunning(null_moniker)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    moniker.IsRunning(null_moniker)
TypeError: required argument 'pmkToLeft' missing
>>> moniker.IsRunning(null_moniker,null_context))
SyntaxError: invalid syntax
>>> moniker.RemoteBindToStorage(null_context,null_moniker,comtypes.gen.DirectShowLib.IPropertyBag._iid_)
<POINTER(IUnknown) ptr=0x5aae98 at 4a46148>
>>> source = moniker.RemoteBindToStorage(null_context,null_moniker,comtypes.gen.DirectShowLib.IPropertyBag._iid_)
>>> type(source)
<class 'comtypes.POINTER(IUnknown)'>
>>> comtypes.gen.DirectShowLib.IPropertyBag.Read("Description")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    comtypes.gen.DirectShowLib.IPropertyBag.Read("Description")
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
TypeError: Expected a COM this pointer as first argument
>>> comtypes.gen.DirectShowLib.IPropertyBag.Read("Description",0,None)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    comtypes.gen.DirectShowLib.IPropertyBag.Read("Description",0,None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
TypeError: Expected a COM this pointer as first argument
>>> qi = moniker.QueryInterface(comtypes.gen.DirectShowLib.IPropertyBag)
>>> type(qi)
<class 'comtypes.POINTER(IPropertyBag)'>
>>> qi.Read("Description",0,None)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    qi.Read("Description",0,None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024894, 'The system cannot find the file specified.', (None, None, None, 0, None))
>>> qi.Read("FriendlyName",0,None)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    qi.Read("FriendlyName",0,None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))
>>> comtypes.gen.DirectShowLib.VARIANT v
SyntaxError: invalid syntax
>>> v = comtypes.gen.DirectShowLib.VARIANT
>>> type(v)
<class '_ctypes.PyCStructType'>
>>> qi.Read("FriendlyName",v,None)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    qi.Read("FriendlyName",v,None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 644, in call_with_inout
    v = atyp.from_param(v)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 203, in from_param
    return cls(value)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 187, in __init__
    self.value = args[0]
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 365, in _set_value
    raise TypeError("Cannot put %r in VARIANT" % value)
TypeError: Cannot put <class 'comtypes.automation.tagVARIANT'> in VARIANT
>>> qi.Read("Description",v,None)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    qi.Read("Description",v,None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 644, in call_with_inout
    v = atyp.from_param(v)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 203, in from_param
    return cls(value)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 187, in __init__
    self.value = args[0]
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 365, in _set_value
    raise TypeError("Cannot put %r in VARIANT" % value)
TypeError: Cannot put <class 'comtypes.automation.tagVARIANT'> in VARIANT
>>> from ctypes import *
>>> v = ctypes.wintypes.INT
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    v = ctypes.wintypes.INT
NameError: name 'ctypes' is not defined
>>> v = wintypes.INT
>>> type(v)
<class '_ctypes.PyCSimpleType'>
>>>  qi.Read("FriendlyName",v,None)
 
SyntaxError: unexpected indent
>>> qi.Read("FriendlyName",v,None)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    qi.Read("FriendlyName",v,None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 644, in call_with_inout
    v = atyp.from_param(v)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 203, in from_param
    return cls(value)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 187, in __init__
    self.value = args[0]
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 365, in _set_value
    raise TypeError("Cannot put %r in VARIANT" % value)
TypeError: Cannot put <class 'ctypes.c_long'> in VARIANT
>>> v = ctypes.wintypes.VARIANT
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    v = ctypes.wintypes.VARIANT
NameError: name 'ctypes' is not defined
>>> v = wintypes.VARIANT
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    v = wintypes.VARIANT
AttributeError: module 'ctypes.wintypes' has no attribute 'VARIANT'
>>> from ctypes.wintypes import UINT
>>> v = UINT
>>> type(v)
<class '_ctypes.PyCSimpleType'>
>>> qi.Read("FriendlyName",v,None)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    qi.Read("FriendlyName",v,None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 644, in call_with_inout
    v = atyp.from_param(v)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 203, in from_param
    return cls(value)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 187, in __init__
    self.value = args[0]
  File "C:\Program Files\Python35\lib\site-packages\comtypes\automation.py", line 365, in _set_value
    raise TypeError("Cannot put %r in VARIANT" % value)
TypeError: Cannot put <class 'ctypes.c_ulong'> in VARIANT
>>> 
