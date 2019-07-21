# 1
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
#        print("Execution of Point Class")
        
class Pythagoras:
    
    def __init__(self):
        print("Pythagors calculation...")        
    
    def setPointOne(self, obj):
        self.point_one_x = obj.x
        self.point_one_y = obj.y
#        print("Set point one.")
        
    def setPointTwo(self, obj):
        self.point_two_x = obj.x
        self.point_two_y = obj.y
#        print("Set point two.")
    
    def getSlope(self):
        self.slope = (self.point_two_y-self.point_one_y)/(self.point_two_x-self.point_one_x)
        return self.slope
    
    def getDistance(self):
        self.distance = (((self.point_two_x-self.point_one_x))**2 + ((self.point_two_y-self.point_one_y))**2)**0.5
        return self.distance
   
pt1 = Point(0, 0)
pt2 = Point(3, 4)
     
pyt = Pythagoras()
pyt.setPointOne(pt1)
pyt.setPointTwo(pt2)
print(pyt.getSlope())
print(pyt.getDistance())

