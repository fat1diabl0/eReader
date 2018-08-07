Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import winsound
>>> import ossaudiodev
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import ossaudiodev
ImportError: No module named 'ossaudiodev'
>>> import wx
>>> import wx.adv
>>> wx.adv.Sound(r"F:\Upwork\Projects\Camera Tool\eReader-master\Camera Shutter Sound.wav")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    wx.adv.Sound(r"F:\Upwork\Projects\Camera Tool\eReader-master\Camera Shutter Sound.wav")
wx._core.PyNoAppError: The wx.App object must be created first!
>>> s =  wx.adv.Sound(r"F:\Upwork\Projects\Camera Tool\eReader-master\Camera Shutter Sound.wav")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s =  wx.adv.Sound(r"F:\Upwork\Projects\Camera Tool\eReader-master\Camera Shutter Sound.wav")
wx._core.PyNoAppError: The wx.App object must be created first!
>>> 
