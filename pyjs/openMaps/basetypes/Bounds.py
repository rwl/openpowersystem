




class Bounds:
    
    #Wrapped From http:#dev.openlayers.org/releases/OpenLayers-2.6/doc/apidocs/files/OpenLayers/BaseTypes/Bounds-js.html
    
    JavaScriptObject object = createBounds()
    
    def createBounds(self):
        JS("""
        return new $wnd.OpenLayers.Bounds();
        """)
    
    
    def extend(self, point):
        _extendPoint(object, point.getX(), point.getY())
    
    
    def _extendPoint(self, o, x, y):
        JS("""
        o.extend(new $wnd.OpenLayers.Geometry.Point(x, y));
        """)
    
    
    def extend(self, point):
        _extend(object, point.getLongitude(), point.getLatitude())
    
    
    def extend(self, bound):
        _extend(object, bound.object)
    
    
    def _extend(self, x, o):
        JS("""
        x.extend(o);
        """)
    
    
    def _extend(self, x, lon, lat):
        JS("""
        x.extend(new $wnd.OpenLayers.LonLat(lon, lat));
        """)
    
    
    @Override
    def toString(self):
        return _toString(object)
    
    
    def _toString(self, x):
        JS("""
        return x.toString();
        """)
    
    
    def getWidth(self):
        return _getWidth(object)
    
    
    double _getWidth(JavaScriptObject x){
        JS("""
        return x.getWidth();
        """)
    
    
    def getHeight(self):
        return _getHeight(object)
    
    
    double _getHeight(JavaScriptObject x){
        JS("""
        return x.getHeight();
        """)
    
    
    def getSize(self):
        return Size(getWidth(), getHeight())
    
    
    def getCenterPixel(self):
        return Pixel(_getCenterXPixel(object), _getCenterYPixel(object))
    
    
    
    int _getCenterYPixel(JavaScriptObject x){
        JS("""
        return x.getCenterPixel().y;
        """)
    
    
    
    int _getCenterXPixel(JavaScriptObject x){
        JS("""
        return x.getCenterPixel().x;
        """)
    
    
    def getCenterLatLon(self):
        return LonLat(_getCenterLon(object), _getCenterLat(object))
    
    
    
    double _getCenterLon(JavaScriptObject x){
        JS("""
        return x.getCenterLonLat().lon;
        """)
    
    
    double _getCenterLat(JavaScriptObject x){
        JS("""
        return x.getCenterLonLat().lat;
        """)
    
    
    def contains(self, ll, inclusive):
        return _containsLonLat(object, ll.getLongitude(), ll.getLatitude(), inclusive)
    
    
    boolean _containsLonLat(JavaScriptObject x, double lon,
    double lat, boolean inc) {
        JS("""
        return x.containsLonLat(new $wnd.OpenLayers.LonLat(lon, lat), inc);
        """)
    
    
    def contains(self, ll, inclusive):
        return _containsPixel(object, ll.getX(), ll.getY(), inclusive)
    
    
    boolean _containsPixel(JavaScriptObject o, double x,
    double y, boolean inc) {
        JS("""
        return o.containsPixel(new $wnd.OpenLayers.Pixel(x, y), inc);
        """)
    
    
    def intersectsBounds(self, bounds, inclusive):
        return _intersectsBounds(object, bounds.object, inclusive)
    
    
    boolean _intersectsBounds(JavaScriptObject x, JavaScriptObject o,
    boolean inclusive) {
        JS("""
        return x.intersectsBounds(o, inclusive);
        """)
    
    
    def containsBounds(self, bounds, partial, inclusive):
        return _containsBounds(object, bounds.object, partial, inclusive)
    
    
    boolean _containsBounds(JavaScriptObject x, JavaScriptObject o,
    boolean partial, boolean inclusive) {
        JS("""
        return x.intersectsBounds(o, partial, inclusive);
        """)
    


