





class IconMarker extends Marker:
    
    LonLat loc
    
    def __init__(self, icon, ll):
        super(_newInstance(icon.getIconClone(), ll.getLongitude(), ll.getLatitude()))
        _registerListeners(this, getJsObject())
        self.loc = ll
    
    
    def _registerListeners(self, m, marker):
        JS("""
        marker.events.register("mousedown", null, function clickEvent(evt) {
            m.@com.gorthaur.franza.openlayers.client.markers.IconMarker::fireClickEvent()();
        });
        marker.events.register("mouseover", null, function overEvent(evt) {
            m.@com.gorthaur.franza.openlayers.client.markers.IconMarker::fireHoverOverEvent()();
        });
        marker.events.register("mouseout", null, function overEvent(evt) {
            m.@com.gorthaur.franza.openlayers.client.markers.IconMarker::fireHoverOutEvent()();
        });
        """)
    
    
    JavaScriptObject _newInstance(JavaScriptObject icon,
    double lon, double lat) {
        JS("""
        return new $wnd.OpenLayers.Marker(new $wnd.OpenLayers.LonLat(lon,lat),icon);
        """)
    
    
    def getLocation(self):
        return loc
    
    
    def destroy(self):
        _destroy(getJsObject())
    
    
    def _destroy(self, o):
        JS("""
        o.destroy();
        """)
    
    


