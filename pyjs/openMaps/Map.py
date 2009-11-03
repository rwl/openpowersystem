












class Map:
    
    List<MapClickListener> listeners = ArrayList<MapClickListener>()
    List<MapMoveListener> moveListeners = ArrayList<MapMoveListener>()
    
    def _addControl(self, map, control):
        JS("""
        map.addControl(control);
        """)
    
    
    def _addLayer(self, map, layer, isBase):
        JS("""
        map.addLayer(layer);
        if(isBase) {
            map.setBaseLayer(layer);
        }
        """)
    
    
    def _getNumZoomLevels(self, map):
        JS("""
        return map.getNumZoomLevels();
        """)
    
    
    def _getZoom(self, map):
        JS("""
        return map.getZoom();
        """)
    
    
    def _newInstance(self, m, mapDomElement, totalNumZoomLevels, isSphericalMercator):
        JS("""
        
        function mapEvent(e) {
            m.@com.gorthaur.franza.openlayers.client.Map::fireMoveListeners()();
        };
        
        var map =  new $wnd.OpenLayers.Map(mapDomElement);
        map.events.register("moveend", null, mapEvent);
        
        return map;
        """)
    
    
    def _addClickListener(self, map, m):
        JS("""
        
        $wnd.OpenLayers.Control.Click = $wnd.OpenLayers.Class($wnd.OpenLayers.Control, {
            defaultHandlerOptions: {
                'single': true,
                'double': false,
                'pixelTolerance': 0,
                'stopSingle': false,
                'stopDouble': false
            },
            
            initialize: function(options) {
                this.handlerOptions = $wnd.OpenLayers.Util.extend(
                {}, this.defaultHandlerOptions
                );
                $wnd.OpenLayers.Control.prototype.initialize.apply(
                this, arguments
                );
                this.handler = new $wnd.OpenLayers.Handler.Click(
                this, {
                    'click': this.onClick
                }, this.handlerOptions
                );
            },
            
            onClick: function(e) {
                m.@com.gorthaur.franza.openlayers.client.Map::fireSingleClick(II)(e.xy.x, e.xy.y);
            }
            
            
            
        });
        
        var click = new $wnd.OpenLayers.Control.Click();
        map.addControl(click);
        click.activate();
        
        """)
    
    
    def _panTo(self, map, lon, lat):
        JS("""
        map.panTo(new $wnd.OpenLayers.LonLat(lon, lat));
        """)
    
    
    def _removeLayer(self, map, layer):
        JS("""
        map.removeLayer(layer);
        """)
    
    
    def _setLayerIndex(self, map, layer, index):
        JS("""
        map.setLayerIndex(layer, index);
        """)
    
    
    def _updateSize(self, map):
        JS("""
        map.updateSize();
        """)
    
    
    def _zoomTo(self, map, zoomLevel):
        JS("""
        map.zoomTo(zoomLevel);
        """)
    
    
    def _setCenter(self, map, lon, lat, zoom, dragging, forceZoomChange):
        JS("""
        map.setCenter(new $wnd.OpenLayers.LonLat(lon, lat), zoom, dragging);
        """)
    
    
    JavaScriptObject map
    MapWidget parent
    
    def __init__(self, mapDomElement, parent, speherical):
        self.map = _newInstance(this, mapDomElement, 14, speherical)
        self.parent = parent
    
    
    def addControl(self, c):
        _addControl(map, c.getJsObject())
    
    
    def addLayer(self, l, isBaseLayer):
        _addLayer(map, l.getJsObject(), isBaseLayer)
    
    
    def getNumZoomLevels(self):
        return _getNumZoomLevels(self.map)
    
    
    def getZoomLevel(self):
        return _getZoom(self.map)
    
    
    def panTo(self, ll):
        _panTo(map, ll.getLongitude(), ll.getLatitude())
        fireMoveListeners()
    
    
    def redraw(self):
        _updateSize(self.map)
        
    
    
    def removeLayer(self, layer):
        _removeLayer(self.map, layer.getJsObject())
    
    
    def setLayerIndex(self, layer, index):
        _setLayerIndex(self.map, layer.getJsObject(), index)
    
    
    def setZoomLevel(self, zoomLevel):
        zoomLevel = (zoomLevel >= self.getNumZoomLevels()) ? self.getNumZoomLevels()-1 : zoomLevel
        _zoomTo(self.map, zoomLevel)
        fireMoveListeners()
    
    
    def getJsObject(self):
        return map
    
    
    def getLonLatFromPixel(self, p):
        return LonLat(_getLonFromPixel(map, p.getX(), p.getY()), _getLatFromPixel(map, p.getX(), p.getY()))
    
    
    def setCenter(self, ll, zoom, dragging, forceZoomChange):
        _setCenter(map, ll.getLongitude(), ll.getLatitude(), zoom, dragging, forceZoomChange)
        fireMoveListeners()
    
    
    def _getLonFromPixel(self, o, x, y):
        JS("""
        return o.getLonLatFromPixel(new $wnd.OpenLayers.Pixel(x, y)).lon;
        """)
    
    
    def _getLatFromPixel(self, o, x, y):
        JS("""
        return o.getLonLatFromPixel(new $wnd.OpenLayers.Pixel(x, y)).lat;
        """)
    
    
    def addClickListener(self, mouseListener):
        if(listeners.isEmpty()) {
            _addClickListener(self.map, this)
        
        listeners.add(mouseListener)
        
    
    
    def addMapListener(self, listener):
        moveListeners.add(listener)
    
    
    def getExtent(self):
        Bounds b =  Bounds()
        b.extend(LonLat(_getLowerLonBound(map), _getLowerLatBound(map)))
        b.extend(LonLat(_getUpperLonBound(map), _getUpperLatBound(map)))
        return b
    
    
    double _getLowerLonBound(JavaScriptObject o)  {
        JS("""
        return o.getExtent().toArray()[0];
        """)
    
    
    double _getUpperLonBound(JavaScriptObject o)  {
        JS("""
        return o.getExtent().toArray()[2];
        """)
    
    
    double _getLowerLatBound(JavaScriptObject o)  {
        JS("""
        return o.getExtent().toArray()[1];
        """)
    
    
    double _getUpperLatBound(JavaScriptObject o)  {
        JS("""
        return o.getExtent().toArray()[3];
        """)
    
    
    def fireSingleClick(self, x, y):
        double xl = (double)x / (double) parent.getOffsetWidth()
        System.out.println(xl)
        double llat = _getLowerLatBound(map)
        System.out.println(llat)
        
    
    
    def fireMoveListeners(self):
        #		for(MapMoveListener l: moveListeners) {
            #			Bounds exts = getExtent()
            #			l.mapMoved(exts.getCenterLatLon(), getZoomLevel(), exts)
            #		}
        
        
        def zoomToMaxExtent(self):
            _zoomToMaxExtent(map)
        
        
        void _zoomToMaxExtent(JavaScriptObject m)  {
            JS("""
            m.zoomToMaxExtent();
            """)
        
        
        #	void zoomToExtent(Bounds bounds) {
            #		_zoomToExtent(map, bounds.getJsObject())
            #	}
            #
            #	void _zoomToExtent(JavaScriptObject m)  {
                JS("""
                //		m.zoomToMaxExtent();
                //	""")
            
            
            interface MapClickListener {
                void mapClicked(LonLat position)
            
            
            interface MapMoveListener {
                void mapMoved(LonLat center, int zoomLevel, Bounds boundingBox)
            
            
            
        
        
