

class Size:
    
    double width
    double height
    
    def getWidth(self):
        return width
    
    
    def setWidth(self, width):
        self.width = width
    
    
    def getHeight(self):
        return height
    
    
    def setHeight(self, height):
        self.height = height
    
    
    def __init__(self, width, height):
        super()
        self.width = width
        self.height = height
    
    
    def clone(self):
        return Size(width, height)
    
    
    @Override
    def equals(self, obj):
        if obj instanceof Size:
            Size s = (Size) obj
            return s.width == width  and  s.height == height
        
        
        return False
    


