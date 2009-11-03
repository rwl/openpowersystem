




class OverviewMap extends Control:
    
    def __init__(self, layer):
        super(_newInstance(256, 256, layer.getJsObject()))
    
    
    JavaScriptObject _newInstance(int width, int height, JavaScriptObject layer){
        JS("""
        var options = {
            layers: [layer],
            projection: "EPSG:26912",
            units: 'm',
            maxExtent: new $wnd.OpenLayers.Bounds(455402, 4967657, 473295, 4984095)
        };
        return new $wnd.OpenLayers.Control.OverviewMap(options);
        """)
    
    
    def addControl(self, o, c):
        JS("""
        o.ovmap.addControl(c);
        """)
    
    
    def addLayer(self, o, c):
        JS("""
        o.ovmap.addLayer(c);
        """)
    
    
    def addControl(self, c):
        addControl(getJsObject(), c.getJsObject())
    
    
    def addLayer(self, l):
        addLayer(getJsObject(), l.getJsObject())
    


