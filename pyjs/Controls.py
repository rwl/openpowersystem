
import OpenLayers.js

class OpenLayersMap:
    """ Instances of OpenLayers.Map are interactive maps embedded in a web
        page. On their own maps do not provide much functionality.  To extend
        a map it's necessary to add controls (OpenLayers.Control) and layers
        (OpenLayers.Layer) to the map.
    """

    def __init__(self, div, **options):
        """ Constructor for a new OpenLayers.Map instance.
        """
#        element = DOM.createDiv()
#        FocusWidget.__init__(self, element)

        JS("""
        var map = new OpenLayers.Map('map');

        var wms = new OpenLayers.Layer.WMS( "OpenLayers WMS",
            "http://labs.metacarta.com/wms/vmap0", {layers: 'basic'} );
        map.addLayer(wms);
        map.zoomToMaxExtent();
        """)

    def render(self, div):
        """ Render the map to a specified container.
        """

    def setOptions(self, **options):
        """ Change the map options.
        """

    def getTileSize(self):
        """ Get the tile size for the map.
        """

    def getBy(self, array, property, match):
        """ Get a list of objects given a property and a match item.
        """

    def getLayersBy(self, property, match):
        """ Get a list of layers with names matching the given name.
        """

    def getLayersByName(self, match):
        """ Get a list of layers with names matching the given name.
        """

    def getLayersByClass(self, match):
        """ Get a list of layers of a given class (CLASS_NAME).
        """

    def getControlsBy(self, property, match):
        """ Get a list of controls with properties matching the given criteria.
        """

    def getControlsClass(self, match):
        """ Get a list of controls of a given class (CLASS_NAME).
        """

    def getLayer(self, id):
        """ Get a layer based on its id.
        """

    def addLayer(self, layer):
        pass

    def addLayers(self, layers):
        pass

    def removeLayer(self, layer, set_new_base_layer):
        """ Removes a layer from the map by removing its visual element (the
            layer.div property), then removing it from the map's internal list
            of layers, setting the layer's map property to null.
        """

    def getNumLayers(self):
        """ The number of layers attached to the map.
        """

    def getLayerIndex(self, layer):
        pass

    def setLayerIndex(self, layer, idx):
        """ Move the given layer to the specified (zero-based) index in the
            layer list, changing its z-index in the map display.
        """

    def raiseLayer(self, layer, delta):
        """ Change the index of the given layer by delta.
        """

    def setBaseLayer(self, new_base_layer):
        """ Allows user to specify one of the currently-loaded layers as the
            Map's new base layer.
        """

    def addControl(self, control, px):
        pass

    def getControl(self, id):
        pass

    def removeControl(self, control):
        """ Remove a control from the map.
        """

    def addPopup(self, popup, exclusive):
        pass

    def removePopup(self, popup):
        pass

    def getSize(self):
        """ An OpenLayers.Size object that represents the size, in pixels, of
            the div into which OpenLayers has been loaded.
        """

    def updateSize(self):
        """ This function should be called by any external code which
            dynamically changes the size of the map div (because mozilla wont
            let us catch the ?onresize? for an element)
        """

    def getCenter(self):
        """ OpenLayers.LonLat
        """

    def getZoom(self):
        """ Integer
        """

    def pan(self, dx, dy, options):
        """ Allows user to pan by a value of screen pixels.
        """

    def panTo(self, lonlat):
        """ Allows user to pan to a new lonlat If the new lonlat is in the
            current extent the map will slide smoothly.
        """

    def setCenter(self, lonlat, zoom, dragging, force_zoom_change):
        """ Set the map center (and optionally, the zoom level).
        """

    def getProjection(self):
        """ This method returns a string representing the projection.
        """

    def getProjectionObject(self):
        """ Returns the projection obect from the baselayer.
        """

    def getMaxResolution(self):
        """ The Map's Maximum Resolution.
        """

    def getMaxExtent(self, options):
        pass

    def getNumZoomLevels(self):
        """ The total number of zoom levels that can be displayed by the
            current baseLayer.
        """

    def getExtent(self):
        """ A Bounds object which represents the lon/lat bounds of the current
            viewPort.
        """

    def getResolution(self):
        """ The current resolution of the map.
        """

    def getUnits(self):
        """ The current units of the map.
        """

    def getScale(self):
        """ The current scale denominator of the map.
        """

    def getZoomForExtent(self, bounds, closest):
        pass

    def getResolutionForZoom(self, zoom):
        pass

    def getZoomForResolution(self, resolution, closest):
        pass

    def zoomTo(self, zoom):
        """ Zoom to a specific zoom level.
        """

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass

    def zoomToExtent(self, bounds, closest):
        """ Zoom to the passed in bounds, recenter.
        """

    def zoomToMaxExtent(self, options):
        """ Zoom to the full extent and recenter.
        """

    def zoomToScale(self, scale, closest):
        """ Zoom to a specified scale.
        """

    def getViewPortPxFromLonLat(self, lonlat):
        pass

    def getLonLatFromPixel(self, px):
        pass

    def getPixelFromLonLat(self, lonlat):
        """ Returns a pixel location given a map location.
        """

    def getViewPortPxFromLayerPx(self, layer_px):
        pass

    def getLayerPxFromViewPortPx(self, viewport_px):
        pass

    def getLayerPxFromLonLat(self, lonlat):
        pass

class OpenLayersLayer:
    def setName(self, new_name):
        """ Sets the new layer name for this layer.
        """

    def addOptions(self, new_options):
        pass

    def onMapResize(self):
        """ This function can be implemented by subclasses.
        """

    def redraw(self):
        """ Redraws the layer.
        """

    def removeMap(self, map):
        """ Just as setMap() allows each layer the possibility to take a
            personalized action on being added to the map, removeMap() allows
            each layer to take a personalized action on being removed from it.
        """

    def getImageSize(self):
        """ {OpenLayers.Size} The size that the image should be, taking into
            account gutters.
        """

    def setTileSize(self, size):
        """ Set the tile size based on the map size.
        """

    def getVisibility(self):
        """ {Boolean} The layer should be displayed (if in range).
        """

    def setVisibility(self, visibility):
        """ Set the visibility flag for the layer and hide/show & redraw
            accordingly.
        """

    def display(self, display):
        """ Hide or show the Layer.
        """

    def calculateInRange(self):
        """ {Boolean} The layer is displayable at the current map?s current
            resolution.
        """

    def setIsBaseLayer(self, is_base_layer):
        pass

    def getResolution(self):
        """ {Float} The currently selected resolution of the map, taken from
            the resolutions array, indexed by current zoom level.
        """

    def getExtent(self):
        """ {OpenLayers.Bounds} A Bounds object which represents the lon/lat
            bounds of the current viewPort.
        """

    def getZoomForExtent(self, extent, closest):
        pass

    def getResolutionForZoom(self, zoom):
        pass

    def getZoomForResolution(self, resolution, closest):
        pass

    def getLonLatFromViewPortPx(self, view_port_px):
        pass

    def getViewPortPxFromLonLat(self, lonlat):
        """ Returns a pixel location given a map location.
        """

    def setOpacity(self, opacity):
        """ Sets the opacity for the entire layer (all images)
        """
