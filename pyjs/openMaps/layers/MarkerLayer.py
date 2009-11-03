




class MarkerLayer extends Layer:
    
    JavaScriptObject _construct(String name)   {
        JS("""
        return new $wnd.OpenLayers.Layer.Markers(name);
        """)
    
    
    def __init__(self, name):
        super(_construct(name))
    
    
    def setOpacity(self, opacity):
        _setOpacity(getJsObject(), opacity)
    
    
    def _setOpacity(self, l, o):
        JS("""
        l.setOpacity(o);
        """)
    
    
    def addMarker(self, m):
        _addMarker(getJsObject(), m.getJsObject())
    
    
    def _addMarker(self, l, o):
        JS("""
        l.addMarker(o);
        """)
    
    
    def removeMarker(self, m):
        _removeMarker(getJsObject(), m.getJsObject())
    
    
    def _removeMarker(self, l, o):
        JS("""
        l.removeMarker(o);
        """)
    


