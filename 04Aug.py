Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import comtypes.client
>>> comtypes.client.GetModule(r"C:\Users\DEEP\Downloads\pyPlayer-master\tlb\DirectShow.tlb")
<module 'comtypes.gen._24BC6711_3881_420F_8299_34DA1026D31E_0_1_0' from 'C:\\Program Files\\Python35\\lib\\site-packages\\comtypes\\gen\\_24BC6711_3881_420F_8299_34DA1026D31E_0_1_0.py'>
>>> from comtypes.gen.DirectShowLib import *
>>> from comtypes import client,GUID
>>> qedit = client.GetModule("qedit.dll")
>>> quartz = client.GetModule("quartz.dll")
>>> from uuids import ids, rids
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    from uuids import ids, rids
ImportError: No module named 'uuids'
>>> import uuid
>>> from uuid import id
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    from uuid import id
ImportError: cannot import name 'id'
>>> from uuid import ids
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    from uuid import ids
ImportError: cannot import name 'ids'
>>> from uuid import id
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    from uuid import id
ImportError: cannot import name 'id'
>>> from uuid import ids
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    from uuid import ids
ImportError: cannot import name 'ids'
>>> import interfaces as dsifs
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import interfaces as dsifs
ImportError: No module named 'interfaces'
>>> clsid = '{EE30215D-164F-4A92-A4EB-9D4C13390F9F}'
>>> fg = comtypes.CoCreateInstance(clsid,None,comtypes.CLSCTX_INPROC_SERVER)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    fg = comtypes.CoCreateInstance(clsid,None,comtypes.CLSCTX_INPROC_SERVER)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 1225, in CoCreateInstance
    _ole32.CoCreateInstance(byref(clsid), punkouter, clsctx, byref(iid), byref(p))
TypeError: byref() argument must be a ctypes instance, not 'str'
>>> fg  = comtypes.CoCreateInstance(FilterGraph._reg_clsid_, IGraphBuilder, comtypes.CLSCTX_INPROC_SERVER)
>>> type(fg)
<class 'comtypes.POINTER(IGraphBuilder)'>
>>> clsid = GUID('{EE30215D-164F-4A92-A4EB-9D4C13390F9F}')
>>> fg  = comtypes.CoCreateInstance(clsid, IGraphBuilder, comtypes.CLSCTX_INPROC_SERVER)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fg  = comtypes.CoCreateInstance(clsid, IGraphBuilder, comtypes.CLSCTX_INPROC_SERVER)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 1225, in CoCreateInstance
    _ole32.CoCreateInstance(byref(clsid), punkouter, clsctx, byref(iid), byref(p))
  File "_ctypes/callproc.c", line 920, in GetResult
OSError: [WinError -2147221164] Class not registered
>>> fg  = comtypes.CoCreateInstance(clsid, None, comtypes.CLSCTX_INPROC_SERVER)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    fg  = comtypes.CoCreateInstance(clsid, None, comtypes.CLSCTX_INPROC_SERVER)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 1225, in CoCreateInstance
    _ole32.CoCreateInstance(byref(clsid), punkouter, clsctx, byref(iid), byref(p))
  File "_ctypes/callproc.c", line 920, in GetResult
OSError: [WinError -2147221164] Class not registered
>>> fg  = comtypes.CoCreateInstance(clsid, IBaseFilter, comtypes.CLSCTX_INPROC_SERVER)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fg  = comtypes.CoCreateInstance(clsid, IBaseFilter, comtypes.CLSCTX_INPROC_SERVER)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 1225, in CoCreateInstance
    _ole32.CoCreateInstance(byref(clsid), punkouter, clsctx, byref(iid), byref(p))
  File "_ctypes/callproc.c", line 920, in GetResult
OSError: [WinError -2147221164] Class not registered
>>> dev_enum_xbar = client.CreateObject(ids.CLSID_SystemDeviceEnum,
        interface=dsifs.ICreateDevEnum)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dev_enum_xbar = client.CreateObject(ids.CLSID_SystemDeviceEnum,
NameError: name 'ids' is not defined
>>> fg  = comtypes.CoCreateInstance(CLS, IBaseFilter, comtypes.CLSCTX_INPROC_SERVER)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    fg  = comtypes.CoCreateInstance(CLS, IBaseFilter, comtypes.CLSCTX_INPROC_SERVER)
NameError: name 'CLS' is not defined
>>> import interfaces as dsifs
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    import interfaces as dsifs
ImportError: No module named 'interfaces'
>>> CLSID_SystemDeviceEnum = GUID('{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}')
>>> fg  = comtypes.CoCreateInstance(CLSID_SystemDeviceEnum, None, comtypes.CLSCTX_INPROC_SERVER)
>>> type(fg)
<class 'comtypes.POINTER(IUnknown)'>
>>> client.CreateObject(CLSID_SystemDeviceEnum,pServerInfo=comtypes.CLSCTX_INPROC_SERVER)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    client.CreateObject(CLSID_SystemDeviceEnum,pServerInfo=comtypes.CLSCTX_INPROC_SERVER)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\client\__init__.py", line 247, in CreateObject
    interface=interface, machine=machine, pServerInfo=pServerInfo)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 1375, in CoCreateInstanceEx
    byref(multiqi))
OSError: exception: access violation reading 0x0000000000000019
>>> client.CreateObject(CLSID_SystemDeviceEnum,None,None,None,pServerInfo=comtypes.CLSCTX_INPROC_SERVER)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    client.CreateObject(CLSID_SystemDeviceEnum,None,None,None,pServerInfo=comtypes.CLSCTX_INPROC_SERVER)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\client\__init__.py", line 247, in CreateObject
    interface=interface, machine=machine, pServerInfo=pServerInfo)
  File "C:\Program Files\Python35\lib\site-packages\comtypes\__init__.py", line 1375, in CoCreateInstanceEx
    byref(multiqi))
OSError: exception: access violation reading 0x0000000000000019
>>> 
