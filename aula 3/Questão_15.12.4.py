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
