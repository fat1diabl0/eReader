Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 18, in <module>
    (moniker, fetched) = class_enum.RemoteNext(0)
_ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
<class 'comtypes.POINTER(IMoniker)'>
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 27, in <module>
    moniker.RemoteBindToObject(comtypes.gen.DirectShowLib.IBindCtx,None,qi._iid_)
ctypes.ArgumentError: argument 1: <class 'TypeError'>: Don't know how to convert parameter 1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 26, in <module>
    null_context = POINTER(comtypes.gen.DirectShowLib.IBindCtx)()
NameError: name 'POINTER' is not defined
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 31, in <module>
    moniker.RemoteBindToObject(null_context,null_moniker,qi._iid_)
_ctypes.COMError: (-2147467262, 'No such interface supported', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 32, in <module>
    moniker.RemoteBindToObject(null_context,null_moniker,qi._iid_)
_ctypes.COMError: (-2147467262, 'No such interface supported', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
None
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 45, in <module>
    qi.Read("Description",vtValue,0)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024894, 'The system cannot find the file specified.', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 45, in <module>
    qi.Read("Description",comtypes.addressof(vtValue),0)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024894, 'The system cannot find the file specified.', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 44, in <module>
    qi.Read("FriendlyName",comtypes.addressof(vtValue),0)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 44, in <module>
    qi.Read("FriendlyName",comtypes.addressof(vtValue.value),0)
TypeError: invalid type
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 34, in <module>
    source = moniker.RemoteBindToStorage(null_context,null_moniker,comtypes.addressof(qi)._iid_)
AttributeError: 'int' object has no attribute '_iid_'
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 34, in <module>
    source = moniker.RemoteBindToStorage(null_context,null_moniker,comtypes.addressof(qi._iid_))
ctypes.ArgumentError: argument 3: <class 'TypeError'>: expected LP_GUID instance instead of int
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 44, in <module>
    qi.Read("FriendlyName",comtypes.addressof(vtValue.value),0)
TypeError: invalid type
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 44, in <module>
    qi.Read("FriendlyName",comtypes.addressof(vtValue),0)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 44, in <module>
    qi.Read("FriendlyName",comtypes.addressof(vtValue),None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 44, in <module>
    qi.Read("FriendlyName",comtypes.addressof(vtValue),None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
None
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
VARIANT(vt=0x1, None)
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
Traceback (most recent call last):
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 275, in __getattr__
    fixed_name = self.__map_case__[name.lower()]
KeyError: 'next'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 19, in <module>
    (moniker, fetched) = class_enum.Next(1)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 277, in __getattr__
    raise AttributeError(name)
AttributeError: Next
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
1
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
VARIANT(vt=0x1, None)
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
VARIANT(vt=0x1, None)
>>> 
================ RESTART: C:\Users\DEEP\Desktop\usb-camera.py ================
<class 'comtypes.POINTER(IEnumMoniker)'>
<class 'comtypes.POINTER(IMoniker)'>
<class 'comtypes.POINTER(IPropertyBag)'>
<class 'comtypes.POINTER(IUnknown)'>
Traceback (most recent call last):
  File "C:\Users\DEEP\Desktop\usb-camera.py", line 45, in <module>
    qi.Read("FriendlyName",comtypes.addressof(vtValue),None)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 655, in call_with_inout
    rescode = func(self_, *args, **kw)
_ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))
>>> 
