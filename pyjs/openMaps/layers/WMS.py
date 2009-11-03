



class WMS extends Layer:
    
    def __init__(self, name, url, options):
        super(_newInstance(name, url, options))
    
    
    JavaScriptObject _newInstance(String name, String url, String options){
        JS("""
        return new $wnd.OpenLayers.Layer.WMS(name, url, options);
        """)
    
    


