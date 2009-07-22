from pyjamas import DOM
from pyjamas.ui.Widget import Widget
from pyjamas.ui.SimplePanel import SimplePanel

import OpenLayers.js

class OLMap(SimplePanel):
    def __init__(self, url, *args, **kwargs):
        SimplePanel.__init__(self)

        map_div = DOM.createElement("div")
#        map_div = DOM.createDiv()
        DOM.setAttribute(map_div, "id", "map")

        self.setElement(map_div)

#        self.setWidth(width)
#        self.setHeight(height)

        map = None
        wms = None

        JS("""
        var map = new OpenLayers.Map('map');

        var wms = new OpenLayers.Layer.WMS( "OpenLayers WMS",
            "http://labs.metacarta.com/wms/vmap0", {layers: 'basic'} );

          """)
        self.map = map
        self.wms = wms
        map.addLayer(wms);
        self.zoomToMaxExtent()

#       Widget.__init__(self, *args, **kwargs)

    def onLoad(self):
        SimplePanel.onLoad(self)
        self.map.updateSize()

    def zoomToMaxExtent(self):
        self.map.zoomToMaxExtent()

    def getMapElement(self):
        return self.map

    def getWmsElement(self):
        return self.wms
