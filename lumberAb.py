from abc import ABC

class Lumber(ABC):

    def __init__(self, dimension, type, description):
        self.dimension = dimension
        self.type = type
        self.description = description

    def getDimension(self):
        return self.dimension
    
    def getType(self):
        return self.type
    
    def getDescription(self):
        return self.description
    
       