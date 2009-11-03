



class Icon:
    
    JavaScriptObject object
    
    def createIcon(self, url, sx, sy, ox, oy):
        JS("""
        return new $wnd.OpenLayers.Icon(url, new $wnd.OpenLayers.Size(sx,sy), new $wnd.OpenLayers.Pixel(ox, oy));
        """)
    
    
    def __init__(self, url, size, offset):
        object = createIcon(url, (int)size.getWidth(), (int)size.getHeight(), offset.getX(), offset.getY())
    
    
    def getIconClone(self):
        return getIconClone(object)
    
    
    def getIconClone(self, o):
        JS("""
        return o.clone();
        """)
    


