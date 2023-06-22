class Dimension:
    def __init__(self,height,width,length):
        self.height = height
        self.width = height
        self.length = length
    
    def __str__(self):
        return f"{self.height}x{self.width}x{self.length}"