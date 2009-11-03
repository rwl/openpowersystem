from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Button import Button

from OpenMaps import OpenMap, OpenWMSLayer

import OpenLayers.js

class SimpleMap:
    def onModuleLoad(self):
        panel = VerticalPanel()

        self.map = OpenMap(Width="800px", Height="800px")

        self.wms = OpenWMSLayer("OpenLayers WMS",
            "http://labs.metacarta.com/wms/vmap0", layers="basic")

        self.map.addLayer(self.wms)

        panel.add(self.map)

        RootPanel().add(panel)

if __name__ == '__main__':
    app = SimpleMap()
    app.onModuleLoad()
