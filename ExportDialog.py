# -*- coding: utf-8 -*-

import wx, os, pdfkit, re
import wx.lib.filebrowsebutton as filebrowse

try:
    from agw import gradientbutton as GB
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.gradientbutton as GB

class ExportDialog( wx.Dialog ):
    def __init__( self, par, html_content, txt_content ):
        wx.Dialog.__init__(self, par, -1, '', style=0 )
        self.SetBackgroundColour( wx.Colour( 244, 244, 244 ) )
        config_path = os.path.join( os.getcwd( ), 'settings.dat' )
        print( config_path )
        self.config = wx.Config( 'envision_reader' )
        self.data = { }
        self.data[ 'html_content' ] = html_content
        self.data[ 'txt_content' ] = txt_content
        self.BuildInterface( )

    def BuildInterface( self ):
        self.main_sizer = wx.BoxSizer( wx.VERTICAL )

        # Save As filed
        save_as_sizer = wx.BoxSizer( wx.HORIZONTAL )
        st = wx.StaticText( self, -1, 'Save as:', style=wx.ALIGN_RIGHT )
        save_as_sizer.Add( st, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 8 )
        self.save_as = wx.TextCtrl( self, -1, size=(350,-1) )
        save_as_sizer.Add( self.save_as, 0, wx.RIGHT, 72 )
        self.main_sizer.Add( save_as_sizer, 0, wx.TOP | wx.ALIGN_RIGHT, 86 )

        # Tags field
        tags_sizer = wx.BoxSizer( wx.HORIZONTAL )
        st = wx.StaticText( self, -1, 'Tags:', style=wx.ALIGN_RIGHT )
        tags_sizer.Add( st, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 8 )
        self.tags = wx.TextCtrl( self, -1, size=(350,-1) )
        tags_sizer.Add( self.tags, 0, wx.RIGHT, 72 )
        self.main_sizer.Add( tags_sizer, 0, wx.TOP | wx.ALIGN_RIGHT, 15 )

        # Where field
        where_sizer = wx.BoxSizer( wx.HORIZONTAL )
        self.where = filebrowse.DirBrowseButton( self, -1, size=(400,-1), labelText= "Where: " )#, changeCallback=self.__SelectDirectory )
        initial_directory = self.config.Read( 'were_fild_init_dir' )
        if len( initial_directory ) != 0:
            self.where.SetValue( initial_directory )
        where_sizer.Add( self.where, 0 )
        where_sizer.Add( ( 70, 20 ), 0 )#just add empty space
        self.main_sizer.Add( where_sizer, 0, wx.TOP | wx.ALIGN_RIGHT, 15 )
        self.BuildFormatsPanel( )
        #confirm_btns_sizer = self.CreateButtonSizer( wx.OK | wx.CANCEL )
        #self.main_sizer.Add( confirm_btns_sizer,0, wx.ALIGN_RIGHT|  wx.RIGHT | wx.LEFT | wx.BOTTOM, 20 )
        self.CreateOkCancelBtns( )

        self.SetSizer( self.main_sizer )
        self.Layout( )

    # build a panel with buttons for choosing of saving format
    def BuildFormatsPanel( self ):
        panel = wx.Panel( self, -1, size=(500,60))
        panel.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
        panel_sizer = wx.BoxSizer( wx.VERTICAL )
        formats_list = [ '.html', '.pdf', '.txt' ]
        self.formats = wx.RadioBox( panel, -1, choices=formats_list, style=wx.RA_SPECIFY_COLS, majorDimension=3 )
        panel_sizer.AddStretchSpacer( 1 )
        panel_sizer.Add( self.formats, 0, wx.ALIGN_CENTER )
        panel_sizer.AddStretchSpacer( 1 )
        panel.SetSizer( panel_sizer, 1 )
        self.main_sizer.Add( panel, 0, wx.ALL, 20 )

    def CreateOkCancelBtns( self ):
        ok_cancel_sizer = wx.BoxSizer( wx.HORIZONTAL )
        ok_btn = wx.Button( self, -1, 'Save' )
        ok_btn.Bind( wx.EVT_BUTTON, self.OnOk )
        ok_cancel_sizer.Add( ok_btn, 0, wx.RIGHT, 20 )
        cancel_btn = wx.Button( self, -1, 'Cancel' )
        cancel_btn.Bind( wx.EVT_BUTTON, self.OnCancel )
        ok_cancel_sizer.Add( cancel_btn )
        self.main_sizer.Add( ok_cancel_sizer,0, wx.ALIGN_RIGHT|  wx.RIGHT | wx.LEFT | wx.BOTTOM, 20 )

    #validate input and write the output of wx.html in the chosen format
    def OnOk( self, evt ):
        save_as = self.save_as.GetLineText( 0 ).strip( )
        if save_as == '':
            wx.MessageBox( 'Please fill a valid name for the file.', 'Error', style=wx.OK | wx.CENTER | wx.ICON_ERROR )
            return
        tags = self.tags.GetLineText( 0 ).strip( )
        directory = self.where.GetValue( ).strip( )
        if directory == '':
            wx.MessageBox( 'Please pick a valid destination to save the file.', 'Error', style=wx.OK | wx.CENTER | wx.ICON_ERROR )
            return
        elif directory != '' and not os.path.exists( directory ):
            wx.MessageBox( 'The directory ' + directory + ' doesn\'t exist!', 'Error', style=wx.OK | wx.CENTER | wx.ICON_ERROR )
            return
        format_ind = self.formats.GetSelection( )
        if format_ind == wx.NOT_FOUND:
            wx.MessageBox( 'Please choose format of the export', 'Error', style=wx.OK | wx.CENTER | wx.ICON_ERROR )
            return
        format = self.formats.GetString( format_ind )
        self.data[ 'format' ] = format.strip( '.' )
        self.config.Write( 'were_fild_init_dir', directory )
        self.data[ 'path' ] = os.path.join( directory, save_as + format )
        self.WriteFile( )
        self.EndModal( -1 )
        self.Destroy( )

    #just close the dialog
    def OnCancel( self, evt ):
        self.EndModal( -1 )
        self.Destroy( )

    #
    def WriteFile( self ):
        if self.data[ 'format' ] == 'txt':
            with open( self.data[ 'path'], 'w' ) as f:
                f.write( self.data[ 'txt_content' ] )
        elif self.data[ 'format' ] == 'html':
            with open( self.data[ 'path'], 'w' ) as f:
                f.write( self.data[ 'html_content' ] )
        #pdf format
        else:
            html = re.sub( '<body.+?>','<body style="font-size:20px;">', self.data[ 'html_content' ], 1, re.IGNORECASE  )
            pdfkit.from_string( html, self.data[ 'path' ] )


    # Get value in the field "Where" when directory is chosen
    # def __SelectDirectory( self, evt ):
    #     print( evt.GetString( ) )
