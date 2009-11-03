



class WorldWind extends Layer:
    
    JavaScriptObject _construct(String name, String url, float tileSize, int zoomLevel)   {
        JS("""
        return new $wnd.OpenLayers.Layer.WorldWind(name, url, tileSize, zoomLevel);
        """)
    
    
    def __init__(self, name, url, tileSize, zoomLevels):
        super(_construct(name, url, tileSize, zoomLevels))
    
    


