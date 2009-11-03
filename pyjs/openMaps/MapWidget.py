

from pyjamas import DOM
from pyjamas.ui.SimplePanel import SimplePanel

class MapWidget extends SimplePanel:
    
    Map map
    int idx = 1
    
    def __init__(self, isSphericalMercator):
        super(DOM.createDiv())
        super.getElement().setId("MapWidget-" + (idx++))
        self.map = Map(super.getElement(), this,  isSphericalMercator)
        setSize("100%", "100%")
        
    
    
    
    def getMap(self):
        return self.map
    
    
    def onLoad(self):
        super.onLoad()
        self.map.redraw()
    
    
    



