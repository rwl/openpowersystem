from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Tree import Tree
from pyjamas.ui.TreeItem import TreeItem
from pyjamas.JSONService import JSONProxy

class Edit:
    def onModuleLoad(self):
        self.TEXT_WAITING = "Waiting for response..."
        self.TEXT_ERROR = "Server Error"

        self.remote_py = RegionNamesServicePython()

        self.panel = VerticalPanel()

        top_panel = HorizontalPanel()
        top_panel.setSpacing(8)
        self.panel.add(top_panel)

        refresh = Button("Refresh", self)
        top_panel.add(refresh)

        self.status = Label()
        top_panel.add(self.status)

        edit_panel = HorizontalPanel()
        self.panel.add(edit_panel)

        self.tree = Tree()
        self.tree.addTreeListener(self)
        edit_panel.add(self.tree)

        upload_item = TreeItem("Upload")
        self.tree.add(upload_item)
        map_item = TreeItem("Map")
        self.tree.add(map_item)

    def onTreeItemSelected(self, item):
        pass

    def onTreeItemStateChanged(self, item):
        child = item.getChild(0)

    def onClick(self, sender):
        self.status.setText(self.TEXT_WAITING)
        if self.remote_py.get_geographical_region_names(self) < 0:
            self.status.setText(self.TEXT_ERROR)

    def onRemoteResponse(self, response, request_info):
        for name in response:
            item = TreeItem(name)
            item.addItem(PendingItem())
            self.tree.addItem(item)

        self.status.setText('')

    def onRemoteError(self, code, message, request_info):
        self.status.setText("Server Error or Invalid Response: ERROR " +
                            code + " - " + message)

class PendingItem(TreeItem):
    def __init__(self):
        TreeItem.__init__(self, "Please wait...")

    def isPendingItem(self):
        return True


class RegionNamesServicePython(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/json", ["get_geographical_region_names"])
