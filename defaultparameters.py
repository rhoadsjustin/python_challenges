""" this is a file """
class Point():
    """ this is a class """
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y

    def __str__(self):
        """ string method """
        return "({},{})".format(self.x, self.y)

    def distance(self, p2=None):
        if p2 is None:
            p2 = Point()
        DX = self.x - p2.x
        DY = self.y - p2.y
        return (DX ** 2 + DY ** 2) ** .5
