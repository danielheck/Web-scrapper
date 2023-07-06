from abc import ABC

class Lumber(ABC):

    def __init__(self, dimension, type, description):
        self._dimension = dimension
        self._type = type
        self.description = description

    def getDimension(self):
        return self._dimension
    
    def getType(self):
        return self._type
    
    def getDescription(self):
        return self.description
    

if __name__ == "__main__":
    
    lumber = Lumber("7/16x4x8", "osb", "k")
    print(f"gettypeone {lumber.getType()}")
    print(f"gettypetwo {lumber._type}")