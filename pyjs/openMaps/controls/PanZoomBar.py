



class PanZoomBar extends Control:
    
    def __init__(self):
        super(_newInstance())
    
    
    JavaScriptObject _newInstance(){
        JS("""
        return new $wnd.OpenLayers.Control.PanZoomBar();
        """)
    
    


