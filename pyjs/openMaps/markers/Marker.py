





class Marker:
    
    interface MarkerClickEventHandler {
        void markerClicked(Marker m)
    
    
    interface MarkerHoverEventHandler {
        void markerMouseOver(Marker m)
        void markerMouseOut(Marker m)
    
    
    ArrayList<MarkerClickEventHandler> clickHandlers = ArrayList<MarkerClickEventHandler>()
    ArrayList<MarkerHoverEventHandler> hoverHandlers = ArrayList<MarkerHoverEventHandler>()
    
    JavaScriptObject obj
    
    def __init__(self, o):
        self.obj = o
    
    
    def getJsObject(self):
        return obj
    
    
    def add(self, h):
        clickHandlers.add(h)
    
    
    def add(self, h):
        hoverHandlers.add(h)
    
    
    def fireClickEvent(self):
        for MarkerClickEventHandler e: clickHandlers:
            e.markerClicked(this)
        
    
    
    def fireHoverOverEvent(self):
        for MarkerHoverEventHandler e: hoverHandlers:
            e.markerMouseOver(this)
        
    
    
    def fireHoverOutEvent(self):
        for MarkerHoverEventHandler e: hoverHandlers:
            e.markerMouseOut(this)
        
    


