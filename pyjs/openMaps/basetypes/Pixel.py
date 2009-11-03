

class Pixel:
    
    int x, y
    
    def __init__(self, x, y):
        super()
        self.x = x
        self.y = y
    
    
    def getX(self):
        return x
    
    
    def setX(self, x):
        self.x = x
    
    
    def getY(self):
        return y
    
    
    def setY(self, y):
        self.y = y
    
    
    def add(self, p):
        x += p.x
        y += p.y
    
    
    def offset(self, p):
        x -= p.x
        y -= p.y
    
    
    @Override
    def equals(self, obj):
        if obj instanceof Pixel:
            Pixel o = (Pixel) obj
            return o.x == x  and  o.y == y
        
        
        return False
    
    


