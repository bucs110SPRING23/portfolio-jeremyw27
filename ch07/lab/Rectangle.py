class Rectangle:
    def __init__(self, x=0, y=0, h=0, w=0):
        """
        absolute value of x, y coordinates as well as height and width are saved to instance variables
        args: x, y, h, w (int)
        return: none
        """
        self.x = abs(x)
        self.y = abs(y)
        self.h = abs(h)
        self.w = abs(w)
    
    def __str__(self):
        """
        returns a string that contains the rectangle's x and y coordinates as well as its height and width
        args: none
        return: string that says "(x: #, y: #) width: #, height: #"
        """
        return "(x: " + self.x + ", y: " + self.y + ") width: " + self.w + ", height: " + self.h