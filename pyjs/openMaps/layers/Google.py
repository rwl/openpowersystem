



class Google extends Layer:
    
    enum TYPE {NORMAL, PHYSICAL, HYBRID, SATELLITE}
    
    def __init__(self, type, name, isSphericalMercator):
        super(createLayer(type, name, isSphericalMercator))
    
    
    def createLayer(self, t, layerName, isSphericalMercator):
        switch(t) {
            case SATELLITE: return _createSatelliteLayer(layerName, isSphericalMercator)
            case HYBRID: return _createHybridLayer(layerName, isSphericalMercator)
            case PHYSICAL: return _createPhysicalLayer(layerName, isSphericalMercator)
        
        return _createNormalLayer(layerName, isSphericalMercator)
        
    
    
    def _createSatelliteLayer(self, layerName, isSphericalMercator):
        JS("""
        return new $wnd.OpenLayers.Layer.Google(layerName, {'type' : $wnd.G_SATELLITE_MAP, sphericalMercator: isSphericalMercator});
        """)
    
    
    def _createHybridLayer(self, layerName, isSphericalMercator):
        JS("""
        return new $wnd.OpenLayers.Layer.Google(layerName, {'type' : $wnd.G_HYBRID_MAP, sphericalMercator: isSphericalMercator});
        """)
    
    
    def _createNormalLayer(self, layerName, isSphericalMercator):
        JS("""
        return new $wnd.OpenLayers.Layer.Google(layerName, {'type' : $wnd.G_NORMAL_MAP, sphericalMercator: isSphericalMercator});
        """)
    
    
    def _createPhysicalLayer(self, layerName, isSphericalMercator):
        JS("""
        return new $wnd.OpenLayers.Layer.Google(layerName, {'type' : $wnd.G_PHYSICAL_MAP, sphericalMercator: isSphericalMercator});
        """)
    
    
    


