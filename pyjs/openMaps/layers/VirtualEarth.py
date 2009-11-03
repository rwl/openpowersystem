



class VirtualEarth extends Layer:
    
    def __init__(self, name):
        super(_newInstance(name))
    
    
    JavaScriptObject _newInstance(String name){
        JS("""
        return new $wnd.OpenLayers.Layer.VirtualEarth(name);
        """)
    
    


