import wx
import wx.xrc
import wx.html2
import re

class bookmarkData():
  def __init__(self):
    self.bmName = ""
    self.bmText = ""
    self.index = -1
    self.replaceHTML = ""
    

class MyFrame1 ( wx.Frame ):
  def __init__( self, parent ):
    wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
    
    self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

    right_sizer = wx.BoxSizer( wx.VERTICAL )
    
    self.html_panel = wx.Panel( self, -1 )
    self.html_panel.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
    right_sizer.Add( self.html_panel, 1, wx.EXPAND )

    html_panel_sizer = wx.BoxSizer( wx.VERTICAL )
    
    self.html_widget = wx.html2.WebView.New( self.html_panel, style = wx.BORDER_NONE )
    self.html_widget.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
    self.html_widget.SetEditable(True)
    html = '<html><body><p>Make the selected text red on the yellow background</p></body></html>'
    self.html_widget.SetPage( html, '' )       

    html_panel_sizer.Add( self.html_widget, 1, wx.EXPAND )
    self.html_panel.SetSizer( html_panel_sizer )

    self.m_button3 = wx.Button( self, wx.ID_ANY, u"Create Bookmark", wx.DefaultPosition, wx.DefaultSize, 0 )
    right_sizer.Add( self.m_button3, 0, wx.ALL, 5 )
    self.m_button3.Bind( wx.EVT_BUTTON, self.CreateBookmark )

    self.m_button4 = wx.Button( self, wx.ID_ANY, u"Go To Bookmark", wx.DefaultPosition, wx.DefaultSize, 0 )
    right_sizer.Add( self.m_button4, 0, wx.ALL, 5 )
    self.m_button4.Bind( wx.EVT_BUTTON, self.GoToBookmark )

    self.m_button5 = wx.Button( self, wx.ID_ANY, u"Clear Bookmark", wx.DefaultPosition, wx.DefaultSize, 0 )
    right_sizer.Add( self.m_button5, 0, wx.ALL, 5 )
    self.m_button5.Bind( wx.EVT_BUTTON, self.ClearBookMark )     
    
    self.SetSizer( right_sizer )
    self.Layout()
    
    self.Centre( wx.BOTH )

    self.lstBookmarks = []

  def __del__( self ):
    pass

  def GetIndex(self,selected_text):
##    print(self.html_widget.GetPageText())
##    print(self.html_widget.GetPageSource())
    
    before_page_text = self.html_widget.GetPageText()
    print(before_page_text)
    self.html_widget.Cut()
    after_page_text = self.html_widget.GetPageText()
    print(after_page_text)

    html = '<html><body><p>Make the selected text red on the yellow background</p></body></html>'
    self.html_widget.SetPage( html, '' )

    if len(before_page_text) == len(selected_text) and len(after_page_text) == 0:
##      print(0)
##      print(len(selected_text))
      return 0
    else:
      for i in range(len(after_page_text)):
        if before_page_text[i] != after_page_text[i]:
##          print(i)
##          print(i + len(selected_text))
          return i
          break

      return len(after_page_text)

  def CreateBookmark(self,event):
    selected_text = self.html_widget.GetSelectedText().strip()
    index = self.GetIndex(selected_text)

    obj = bookmarkData()
    obj.bmName = selected_text
    obj.bmText = selected_text
    obj.index = index
    obj.replaceHTML = r"<p aria-label="+selected_text+" role=navigation>"+selected_text+"</p>"

    pos = -1

    for i in range(len(self.lstBookmarks)):
      if self.lstBookmarks[i].index < obj.index:
        pos = i
        continue
      else:
        break

    self.lstBookmarks.insert(pos+1,obj)
    self.UpdateHTML()

  def UpdateHTML(self):
    strPageText = self.html_widget.GetPageText()

    for i in reversed(range(len(self.lstBookmarks))):
      selected_text = self.lstBookmarks[i].bmText
      index = self.lstBookmarks[i].index

      result =  strPageText[:index] + self.lstBookmarks[i].replaceHTML + strPageText[index+len(selected_text):]

      strPageText = result
##      print(strPageText)

    html = '<html><body><p>' + strPageText +'</p></body></html>'
    self.html_widget.SetPage( html, '' )      
    

  def ClearBookMark(self,event):
    self.lstBookmarks.clear()
    
  def GoToBookmark(self,event):
    for i in range(len(self.lstBookmarks)):
      print(self.lstBookmarks[i].index)
    
##    self.html_widget.SetPage( self.lstBookmarks[0].highlightHTML,'' )
##    for i in range(len(self.lstBookmarks)):
##      print(self.lstBookmarks[i].bmName)
##      print(self.lstBookmarks[i].bmWord)
##      print(self.lstBookmarks[i].highlightHTML)
##      print(self.lstBookmarks[i].endIndex)
##    self.html_widget.Find("")
##    
##    flag = wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE
##    flag_highlight = wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE | wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT
##
##    n = self.html_widget.Find(self.lstBookmarks[0].bmWord,flag)
##    if n == 1:
##      self.html_widget.Find(self.lstBookmarks[0].bmWord,flag_highlight)
##    else:
##      for i in range(n):
##        self.html_widget.Find(self.lstBookmarks[0].bmWord,flag_highlight)
##        strText = self.html_widget.GetSelectedText()
##        print(strText)
        
##      i = self.GetIndex(strText)
##      print(i)
##      if i == self.lstBookmarks[0].startIndex:
##        print("Found")

                            
                            
    
      
      
    
      

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
	

