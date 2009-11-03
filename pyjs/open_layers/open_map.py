#import pyjd # dummy in pyjs
from pyjamas import DOM
from pyjamas.ui.Widget import Widget
from pyjamas.ui.SimplePanel import SimplePanel

import OpenLayers.js

class OpenMap(SimplePanel):
    def __init__(self, *args, **kwargs):
        map_div = DOM.createDiv()
        DOM.setAttribute(map_div, "id", "map")
        DOM.setStyleAttribute(map_div, "width", kwargs["Width"])
        DOM.setStyleAttribute(map_div, "height", kwargs["Height"])

        self.setElement(map_div)
        self.setStyleName("ol-Map")

#        map_div.width = kwargs["Width"]
#        map_div.height = kwargs["Height"]

        map = None
        wms = None

        JS("""
        var map = new OpenLayers.Map("map");

        """)
        self.map = map

#        Widget.__init__(self, *args, **kwargs)
        SimplePanel.__init__(self, map_div)

    def onLoad(self):
        self.map.updateSize()
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
            params: Key/value pairs representing the GetMap query string
                parameters and parameter values (e.g. layers='basic')
        """
        wms = None

        params_obj = WMSParams(params)

        JS("""
        var wms = new OpenLayers.Layer.WMS(name, url, params_obj);
        """)

        self.wms = wms

    def getLayerElement(self):
        return self.wms


class WMSParams:
    """ OpenLayers expects params to be an object with key/value pairs
        representing the GetMap query string parameters and values.
    """
    def __init__(self, **kw_args):
        for key in kw_args:
            setattr(self, key, kw_args[key])
