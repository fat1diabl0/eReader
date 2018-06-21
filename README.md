# eReader

## Additional setup for the repo
* Please follow the instructions here to setup the Google OCR repo - https://cloud.google.com/vision/docs/libraries
* You will find the relevant JSON file for the PATH variable in the previous step in the Others folder. 

## Run python3 or py LandingScreen.py to run the whole project

## Milestone 5 updates
* Prirority 1: Please implement the following changes

1. The buttons on the main screen are still not properly labeled. When I come across these buttons with the tab key, they read as button. Please prioritize a fix for this as soon as possible. As Mario said, accessibility is very important for us, and the current version doesn’t meet accessibility standards.
 

Note that it is very important to use the correct declaration order for wx objects. E.g. this is bad:

cameraButton = wx.Button(...)

cameraLabel = wx.StaticText(..., label="camera")

otherButton = wx.Button(...)

otherLabel = wx.StaticText(..., label="cother")

 

You should always declare the label before the object that needs to be associated with the label (i.e. a button, slider, etc.) E.g.

cameraLabel = wx.StaticText(..., label="camera")

cameraButton = wx.Button(...)

otherLabel = wx.StaticText(..., label="cother")

otherButton = wx.Button(...)

 

b. It seems you are using a custom dialog for the save window. Is there a particular reason why you’re not using wx.FileSelector?
 

c. Please make the navigate, export and settings dialogs close with escape.


* Priority 2: Camera functionality setup + PDF import.

* Priority 3: Headings and bookmarks. 



