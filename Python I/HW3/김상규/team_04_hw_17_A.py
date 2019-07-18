# 1: 
class Animal:
    def __init__(self):
        print("Animal created")
    
    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
    
    def whoAmI(self):
        print("Dog")
        
    def bark(self):
        print("Woof!")

print("##### 1번 문제 #####")
d = Dog()
d.whoAmI()
d.eat()
d.bark()
''' 코드 설명
__init__ instance가 class를 호출할 때 실행


'''

''' 코드 결과
Animal created
Dog created
Dog
Eating
Woof!
'''



# 2
class Circle:
    
    def __init__(self):
        self.pi = 3.141592
    def area(self):
        return self.pi*self.r*self.r
        
    def setRadius(self, r):
        self.r = r
        
    def getRadius(self):
        return self.r

print("##### 2번 문제 #####")        

c = Circle()

c.setRadius(5)
print(c.getRadius())
print(c.area())


# 3
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
    
    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2*self.x * self.y
    
    def describe(self, text):
        self.description = text
        
    def authorName(self, text):
        self.author = text
        
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

print("##### 3-1번 문제 #####")
      
rectangle = Shape(100, 45)
print(rectangle.area())
print(rectangle.perimeter())
rectangle.describe("A wide rectangle, more that twice\as wide as it is tall")
rectangle.scaleSize(0.5)
print(rectangle.area())


print("##### 3-2번 문제 #####")

#class Square(Shape):
#    def area_Square(self):
#        return self.x*self.x
#    
#square = Square(5)
        
'''
__init__ instance가 class를 호출할 때 실행
생성할 때 x, y도 함께 넣어줘야함
'''
