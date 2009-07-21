#import pyjd # dummy in pyjs
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.FileUpload import FileUpload
from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui.decoratorpanel import DecoratedTabPanel, DecoratorPanel
from pyjamas.ui.decoratorpanel import DecoratorTitledPanel
from pyjamas import Window
from pyjamas.JSONService import JSONProxy

class UploadFormHandler:
    """ Event handler for the upload form.
    """
#    def onModuleLoad(self):
#        # Create a FormPanel and point it at a service.
#        self.form = FormPanel()
#        self.form.setAction("/upload/")
#
#        # Because we're going to add a FileUpload widget, we'll need to set the
#        # form to use the POST method, and multipart MIME encoding.
#        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
#        self.form.setMethod(FormPanel.METHOD_POST)
#
#        # Create a panel to hold all of the form widgets.
#        panel = VerticalPanel()
#        self.form.setWidget(panel)
#
#        panel.setStyleName("panel") # same name as in OpenPowerSystem.css.
#
#        # Create a FileUpload widget.
#        upload = FileUpload()
#        upload.setName("uploadFormElement")
#        panel.add(upload)
#
#        # Add a 'submit' button.
#        panel.add(Button("Upload", self))
#
#        # Add an event handler to the form.
#        self.form.addFormHandler(self)
#
#        RootPanel().add(self.form)


    def onClick(self, sender):
        self.form.submit()


    def onSubmitComplete(self, event):
        # When the form submission is successfully completed, this event is
        # fired. Assuming the service returned a response of type text/plain,
        # we can get the result text here (see the FormPanel documentation for
        # further explanation).
        Window.alert(event.getResults())


    def onSubmit(self, event):
        # This event is fired just before the form is submitted. We can take
        # this opportunity to perform validation.
#        if (self.upload.getText().length == 0):
#            Window.alert("The file field must not be empty")
#            event.setCancelled(True)
        pass


class OpenPowerSystem:
    def onModuleLoad(self):
        self.TEXT_WAITING = "Waiting for response..."
        self.TEXT_ERROR = "Server Error"

        self.remote_py = UpperServicePython()

        self.tab_panel = TabPanel()
        self.tab_panel.add(self.get_map_panel(), "Map")
        self.tab_panel.add(self.get_edit_panel(), "Edit")
        self.tab_panel.add(self.get_upload_panel(), "Upload")

        RootPanel().add(self.tab_panel)

    def get_map_panel(self):

        panel = HorizontalPanel()

        info = HTML(r'OpenPowerSystem map.')
        panel.add(info)

        return panel

    def get_edit_panel(self):

        panel = HorizontalPanel()

        info = HTML(r'Edit OpenPowerSystem data.')
        panel.add(info)

        return panel

    def get_upload_panel(self):
        # Create a FormPanel and point it at a service.
        self.form = FormPanel()
        self.form.setAction("/upload/")

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

        # Create a FileUpload widget.
        rdfxml_file = FileUpload()
        rdfxml_file.setName("uploadFormElement")
        panel.add(rdfxml_file)

        # Add a 'submit' button.
        upload = Button("Upload")
        panel.add(upload)

        # Add an event handler to the form.
        handler = UploadFormHandler()
        handler.form = self.form
        self.form.addFormHandler(handler)

        return self.form

#    def onClick(self, sender):
#        self.status.setText(self.TEXT_WAITING)
#        text = self.text_area.getText()
#        if self.remote_py.upper(self.text_area.getText(), self) < 0:
#            self.status.setText(self.TEXT_ERROR)
#
#    def onRemoteResponse(self, response, request_info):
#        self.status.setText(response)
#
#    def onRemoteError(self, code, message, request_info):
#        self.status.setText("Server Error or Invalid Response: ERROR " + code + " - " + message)


class UpperServicePython(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/json", ["upload"])

if __name__ == '__main__':
#    pyjd.setup("./public/Upload.html")
    app = OpenPowerSystem()
    app.onModuleLoad()
#    pyjd.run()
