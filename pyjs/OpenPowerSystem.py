#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

import pyjd # dummy in pyjs
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.FileUpload import FileUpload
from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui.decoratorpanel import DecoratedTabPanel, DecoratorPanel
from pyjamas.ui.decoratorpanel import DecoratorTitledPanel
from pyjamas import Window

import edit_panel
#from open_layers.open_map import OpenMap, OpenWMSLayer

#------------------------------------------------------------------------------
#  "OpenPowerSystem" class:
#------------------------------------------------------------------------------

class OpenPowerSystem:
    """ Defines the main panel for OpenPowerSystem.
    """

    def __init__(self):
        """ Constructs a new OpenPowerSystem instance.
        """
        self.TEXT_WAITING = "Waiting for response..."
        self.TEXT_ERROR = "Server Error"

        self.base_panel = HorizontalPanel()

        self.tab_panel = TabPanel()
        self.tab_panel.add(self.get_upload_panel(), "Upload")
#        self.tab_panel.add(self.get_home_panel(), "OpenPowerSystem")
#        self.tab_panel.add(self.get_map_panel(), "Map")
#        self.tab_panel.add(self.get_edit_panel(), "Edit")
        self.tab_panel.selectTab(0)

        self.base_panel.add(self.tab_panel)

        RootPanel().add(self.base_panel)


    def get_home_panel(self):
        panel = VerticalPanel()

        title = HTML("""OpenPowerSystem""")
        panel.add(title)

        subtitle = HTML("""The Open Power System data repository.""")
        panel.add(subtitle)

        return panel


#    def get_map_panel(self):
#        panel = VerticalPanel()
#
#        self.map = OpenMap(Width="900px", Height="900px")
#        panel.add(self.map)
#
#        self.wms = OpenWMSLayer("OpenLayers WMS",
#            "http://labs.metacarta.com/wms/vmap0", layers="basic")
#        self.map.addLayer(self.wms)
#
#        return panel


#    def get_edit_panel(self):
#        edit_page = edit_panel.EditPanel()
#        return edit_page.panel


    def get_upload_panel(self):
        # Create a FormPanel and point it at a service.
        self.form = FormPanel()
        self.form.setAction("/upload")

        # Add an event handler to the form.
        handler = UploadFormHandler()
        handler.form = self.form
        self.form.addFormHandler(handler)

        # Because we're going to add a FileUpload widget, we'll need to set the
        # form to use the POST method, and multipart MIME encoding.
        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)

        panel = VerticalPanel()
        panel.setSpacing(8)
        panel.setStyleName("panel") # same name as in OpenPowerSystem.css.
        self.form.setWidget(panel)

        info = HTML(r'Upload CIM RDF/XML instance file.')
        panel.add(info)

        # Create a list box for choice of profile.
        self.profiles = [("UCTE (CIM 14)", "ucte"),
                         ("CPSM (CIM13)", "cpsm"),
                         ("CDPSM (CIM 14)", "cdpsm")]
        self.profile = ListBox(VisibleItemCount=1)
        self.profile.setName("profileType")
        for n, v in self.profiles:
            self.profile.addItem(n, v)
        panel.add(self.profile)

        # Create a FileUpload widget.
        rdfxml_file = FileUpload()
        rdfxml_file.setName("uploadFormElement")
        panel.add(rdfxml_file)

        # Add a 'submit' button.
        upload = Button("Upload", handler)
        panel.add(upload)

        return self.form

#------------------------------------------------------------------------------
#  "UploadFormHandler" class:
#------------------------------------------------------------------------------

class UploadFormHandler:
    """ Event handler for the upload form.
    """

    def onClick(self, sender):
        self.form.submit()


    def onSubmitComplete(self, event):
        """ When the form submission is successfully completed, this event is
            fired. Assuming the service returned a response of type text/plain,
            we can get the result text here (see the FormPanel documentation
            for further explanation).
        """
#        Window.alert(event.getResults())
        pass


    def onSubmit(self, event):
        """ This event is fired just before the form is submitted. We can take
            this opportunity to perform validation.
        """
#        if (self.upload.getFilename().length == 0):
#            Window.alert("The file field must not be empty")
#            event.setCancelled(True)
        pass


if __name__ == '__main__':
    pyjd.setup("http://localhost:8080/content/OpenPowerSystem.html")
    app = OpenPowerSystem()
    pyjd.run() # dummy in pyjs

# EOF -------------------------------------------------------------------------
