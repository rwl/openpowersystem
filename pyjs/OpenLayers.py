# Copyright (C) 2009 Richard W. Lincoln
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

import OpenLayers.js

class Map:
    """ Instances of OpenLayers.Map are interactive maps embedded in a web
        page. On their own maps do not provide much functionality.  To extend
        a map it's necessary to add controls (OpenLayers.Control) and layers
        (OpenLayers.Layer) to the map.
    """

    def __init__(self, div, **options):
        """ Constructor for a new OpenLayers.Map instance.
        """
        JS("var map = new OpenLayers.Map('map', { controls: [] })")

    def render(self, div):
        """ Render the map to a specified container.
        """

    def setOptions(self, **options):
        """ Change the map options.
        """

    def getTileSize(self):
        """ Get the tile size for the map.
        """

    def getLayersBy(self, name):
        """ Get a list of layers with names matching the given name.
        """

    def getLayer(self, id):
        """ Get a layer based on its id.
        """

    def addLayer(self, layer):
        pass

    def addLayers(self, layers):
        pass

    def removeLayer(self, layer, setNewBaseLayer):
        """ Removes a layer from the map by removing its visual element (the
            layer.div property), then removing it from the map's internal list
            of layers, setting the layer's map property to null.
        """



    def render(self):
        """ Render the map to a specified container.
        """

    def destroy(self):
        """ Destroy this map.
        """

    def setOptions(self):
        """ Change the map options.
        """

    def getTileSize(self):
        """ Get the tile size for the map.
        """

    def getBy(self):
        """ Get a list of objects given a property and a match item.
        """

    def getLayersBy(self):
        """ Get a list of layers with properties matching the given criteria.
        """

    def getLayersByName(self):
        """ Get a list of layers with names matching the given name.
        """

    def getLayersByClass(self):
        """ Get a list of layers of a given class (CLASS_NAME).
        """

    def getControlsBy(self):
        """ Get a list of controls with properties matching the given criteria.
        """

    def getControlsByClass(self):
        """ Get a list of controls of a given class (CLASS_NAME).
        """

    def getLayer(self):
        """ Get a layer based on its id.
        """

    def addLayer(self):
        pass

    def addLayers(self):
        pass

    def removeLayer(self):
        """ Removes a layer from the map by removing its visual element (the
            layer.div property), then removing it from the map?s internal list
            of layers, setting the layer?s map property to null.
        """

    def getNumLayers(self):
        """ The number of layers attached to the map.
        """

    def getLayerIndex(self):
        pass

    def setLayerIndex(self):
        """ Move the given layer to the specified (zero-based) index in the
            layer list, changing its z-index in the map display.
        """

    def raiseLayer(self):
        """ Change the index of the given layer by delta.
        """

    def setBaseLayer(self):
        """ Allows user to specify one of the currently-loaded layers as the
            Map's new base layer.
        """

    def addControl(self):
        pass

    def getControl(self):
        pass

    def removeControl(self):
        """ Remove a control from the map.
        """

    def addPopup(self):
        pass

    def removePopup(self):
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

    def pan(self):
        """ Allows user to pan by a value of screen pixels.
        """

    def panTo(self):
        """ Allows user to pan to a new lonlat If the new lonlat is in the
            current extent the map will slide smoothly.
        """

    def setCenter(self):
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

    def getMaxExtent(self):
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

    def getZoomForExtent(self):
        pass

    def getResolutionForZoom(self):
        pass

    def getZoomForResolution(self):
        pass

    def zoomTo(self):
        """ Zoom to a specific zoom level.
        """

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass

    def zoomToExtent(self):
        """ Zoom to the passed in bounds, recenter.
        """

    def zoomToMaxExtent(self):
        """ Zoom to the full extent and recenter.
        """

    def zoomToScale(self):
        """ Zoom to a specified scale.
        """

    def getViewPortPxFromLonLat(self):
        pass

    def getLonLatFromPixel(self):
        pass

    def getPixelFromLonLat(self):
        """ Returns a pixel location given a map location.
        """

    def getViewPortPxFromLayerPx(self):
        pass

    def getLayerPxFromViewPortPx(self):
        pass

    def getLayerPxFromLonLat(self):
        pass
