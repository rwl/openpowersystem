#import pyjd # dummy in pyjs
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.FileUpload import FileUpload
from pyjamas import Window
from pyjamas.JSONService import JSONProxy

class JSONRPCExample:
    def onModuleLoad(self):
        self.TEXT_WAITING = "Waiting for response..."
        self.TEXT_ERROR = "Server Error"
        self.remote_py = UpperServicePython()
        self.status=Label()
        self.text_area = TextArea()
        self.text_area.setText(r"Please uppercase this string")
        self.text_area.setCharacterWidth(80)
        self.text_area.setVisibleLines(8)
        self.button_py = Button("Send to Python Service", self)
        buttons = HorizontalPanel()
        buttons.add(self.button_py)
        buttons.setSpacing(8)
        info = r'This example demonstrates the calling of appengine upper(case) method with JSON-RPC from javascript (i.e. Python code compiled with pyjs to javascript).'
        panel = VerticalPanel()
        panel.add(HTML(info))
        panel.add(self.text_area)
        panel.add(buttons)
        panel.add(self.status)
        RootPanel().add(panel)

    def onClick(self, sender):
        self.status.setText(self.TEXT_WAITING)
        text = self.text_area.getText()
        if self.remote_py.upper(self.text_area.getText(), self) < 0:
            self.status.setText(self.TEXT_ERROR)

    def onRemoteResponse(self, response, request_info):
        self.status.setText(response)

    def onRemoteError(self, code, message, request_info):
        self.status.setText("Server Error or Invalid Response: ERROR " + code + " - " + message)


class UpperServicePython(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/json", ["upper"])

class Upload:
    def onModuleLoad(self):
        # Create a FormPanel and point it at a service.
        self.form = FormPanel()
        self.form.setAction("/upload/")

        # Because we're going to add a FileUpload widget, we'll need to set the
        # form to use the POST method, and multipart MIME encoding.
        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)

        # Create a panel to hold all of the form widgets.
        panel = VerticalPanel()
        self.form.setWidget(panel)

        panel.setStyleName("panel") # same name as in OpenPowerSystem.css.

        # Create a FileUpload widget.
        upload = FileUpload()
        upload.setName("uploadFormElement")
        panel.add(upload)

        # Add a 'submit' button.
        panel.add(Button("Upload", self))

        # Add an event handler to the form.
        self.form.addFormHandler(self)

        RootPanel().add(self.form)


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
        if (self.upload.getText().length == 0):
            Window.alert("The file field must not be empty")
            event.setCancelled(True)


if __name__ == '__main__':
#    pyjd.setup("./public/Upload.html")
    app = Upload()
    app.onModuleLoad()
#    pyjd.run()
