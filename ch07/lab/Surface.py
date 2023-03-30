from Rectangle import Rectangle

class Surface:
    def __init__(self, filename="", x=0, y=0, h=0, w=0):
        """
        takes parameters and saves them to instance variables (self.image, self.rect)
        args: filename (string); x, y, h, w (int)
        return: none
        """
        self.image = filename
        self.rect = Rectangle(x, y, w, h)
    
    def getRect(self):
        """
        returns Rectangle attribute in self.rect
        args: none
        return: Rectangle attribute through self.rect
        """
        return self.rect