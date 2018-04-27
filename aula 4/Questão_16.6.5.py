"""rect = (ponto_esqueda_baixo,largura,altura)"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return self.y/self.x
    def get_line_to(self,point):
        a = (point.y - self.y)/(point.x-self.x)
        b = self.y - a*self.x

        return (a,b)
class Rectangle:
    def __init__(self,point,width,height):
        #self.point
        self.point = point
        self.width = width
        self.height = height
    def collideRectangle(self,rect):
        a = rect.point.x - self.point.x
        if a < self.width and a > -rect.width:
            a = rect.point.y - self.point.y
            if a < self.height and a > -rect.height:
                return True
        return False


