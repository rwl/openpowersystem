


from pyjamas import Timer
from pyjamas import Window
from pyjamas import WindowResizeListener
from pyjamas.ui.RootPanel import RootPanel













"""*
* Entry point classes define <code>onModuleLoad()</code>.
"""
class OpenLayers implements EntryPoint:
    
    """*
    * This is the entry point method.
    """
    def onModuleLoad(self):
        fixSize()
        Window.enableScrolling(False)
        MapWidget map = MapWidget(True)
        #			map.getMap().addLayer(Google(Google.TYPE.PHYSICAL, "Normal", False), True)
        #			map.getMap().addLayer(Google(Google.TYPE.PHYSICAL, "Physical", True), True)
        #			map.getMap().addLayer(Google(Google.TYPE.HYBRID, "Hybrid", False), False)
        map.getMap().addLayer(Google(Google.TYPE.SATELLITE, "Satellite", False), False)
        MarkerLayer ml = MarkerLayer("Markers")
        map.getMap().addLayer(ml, False)
        #			map.getMap().addLayer(Yahoo("Yahoo Layer"), False)
        #			map.getMap().addLayer(WMS("WMS", "http:#terraservice.net/ogcmap.ashx", "{'layers': 'DRG'}"), True)
        #			map.getMap().addLayer(VirtualEarth("VE"), True)
        #			map.getMap().setZoomLevel(4)
        #			map.getMap().panTo(LonLat(18, 34))
        #			OverviewMap ov = OverviewMap(Google(Google.TYPE.NORMAL, "Overview",  True))
        #			map.getMap().addControl(ov)
        IconMarker marker = IconMarker(Icon("http:#boston.openguides.org/markers/AQUA.png",Size(10, 17), Pixel(0, 0)), LonLat( -76.207844, 36.756947))
        marker.add(MarkerClickEventHandler() {
            
            def markerClicked(self, m):
                System.out.println("Marker Clicked")
            
            
        )
        ml.addMarker(marker)
        map.getMap().addControl(NavToolBar())
        #			map.getMap().addControl(PanZoomBar())
        #			map.getMap().addControl(LayerSwitcher())
        
        #			ov.addControl(NavToolBar())
        #			ov.addLayer(Google(Google.TYPE.NORMAL, "Overview",  True))
        #			, 'size': $wnd.OpenLayers.Size(width, height)
        
        #		map.getMap().zoomToMaxExtent()
        
        map.getMap().addMapListener(MapMoveListener() {
            
            void mapMoved(LonLat center, int zoomLevel,
            Bounds boundingBox) {
                System.out.println("Move Complete " + boundingBox)
                System.out.println("Center: " + center)
                System.out.println("ZoomLevel: " + zoomLevel)
            
            
        )
        
        RootPanel.get().add(map)
        #		Timer t = Timer() {
            #
            #			@Override
            #			void run() {
                #				fixSize()
                #			}
                #
                #		}
                t.schedule(500)
                
                Window.addWindowResizeListener(WindowResizeListener() {
                    
                    def onWindowResized(self, width, height):
                        fixSize()
                    
                    
                )
            
            
            def fixSize(self):
                RootPanel.get().setSize(Window.getClientWidth() + "px", Window.getClientHeight() + "px")
            
            
        
        
