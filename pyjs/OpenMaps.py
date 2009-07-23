from pyjamas import DOM
from pyjamas.ui.Widget import Widget
from pyjamas.ui.SimplePanel import SimplePanel

import OpenLayers.js

class OpenMap(Widget):
    def __init__(self, url, *args, **kwargs):
        map_div = DOM.createDiv()
        DOM.setAttribute(map_div, "id", "map")

        self.setElement(map_div)
        self.setStyleName("ol-Map")

        map = None
        wms = None

        JS("""
        var map = new OpenLayers.Map("map");

        var wms = new OpenLayers.Layer.WMS( "OpenLayers WMS",
            url, {'layers': 'basic'} );

        """)
        self.map = map
        self.wms = wms
        map.addLayer(wms);
        self.zoomToMaxExtent()

        Widget.__init__(self, *args, **kwargs)

    def onLoad(self):
        self.map.render(self.getElement())

    def getMapElement(self):
        return self.map

    def getWmsElement(self):
        return self.wms

    def zoomToMaxExtent(self):
        """ Zoom to the full extent and recenter.
        """
        self.map.zoomToMaxExtent()

    def addLayer(self, layer):
        self.map.addLayer(layer.getLayerElement())


class OpenWMSLayer:
    def __init__(self, name, url, **params):
        """ Initialises a new WMS layer instance.

            name: A name for the layer
            url: Base url for the WMS (e.g. http://wms.jpl.nasa.gov/wms.cgi)
            params: An object with key/value pairs representing the GetMap
                query string parameters and parameter values.
        """
        if params is None:
            params = {}

        wms = None

        JS("""
        var wms = new OpenLayers.Layer.WMS(name, url, params);
        """)

        self.wms = wms

    def getLayerElement(self):
        return self.wms
