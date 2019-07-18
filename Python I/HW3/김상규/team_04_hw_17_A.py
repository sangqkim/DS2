# 1: 
''' 코드 설명
Animal class가 생성될 때, __init__ instance가 실행되어 "Animal created" 문장을 출력한다.
whoAmI, eat instance method가 있으며, 각각 호출되면 print() 안에 있는 내용을 출력한다.

Dog class는 Animal class를 상속받는다.
super().__init__() 명령으로 인해 Animal의 초기값을 받는다.
whoAmI라는 method는 Animal class와 동일하여 overriding 된다.
bark라는 새로운 method가 있으며 호출될 때 해당 내용이 출력된다.
'''

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



'''
* 출력 결과
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

c = Circle()

print("##### 2번 문제 #####")  
c.setRadius(5)
print(c.getRadius())
print(c.area())

      
'''
출력 결과
5
78.5398

'''

# 3
''' 코드 설명
Shape class 생성될 때, __init__ instance가 실행되고 x, y를 인수로 받고,
self.description = "This shape has not been described yet"와 
self.author = "Nobody has claimed to make this shape yet"을 각각의 str를 받는다.

area method는 x*y를 return 하고, 
perimeter는 2x + 2y를 return 하고,
describe는 인수로 받은 str를 self.desciption에 할당한다.
authorName은 인수로 받은 str를 self.author에 할당한다.
scaleSize는 받은 인수를 self.x와 self.y에 곱해 각각 update한다.

'''
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
    
    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2*self.x + 2*self.y
    
    def describe(self, text):
        self.description = text
        
    def authorName(self, text):
        self.author = text
        
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

print("##### 3번 문제 #####")
      
rectangle = Shape(100, 45)
print(rectangle.area())
print(rectangle.perimeter())
rectangle.describe("A wide rectangle, more that twice\as wide as it is tall")
rectangle.scaleSize(0.5)
print(rectangle.area())
''' 출력 결과
4500
290
1125.0
'''


class Square(Shape):
    def __init__(self, x):
        super().__init__(x, x)
        
print("##### 3-1번 문제 #####")
s = Square(8)
print(s.area())
print(s.perimeter())

class DoubleSquare(Square):
    def __init__(self, x):
        super().__init__(x)
        self.x = x
        self.y = 2*x
                
print("##### 3-2번 문제 #####")
      
ds = DoubleSquare(8)
print(ds.area())
print(ds.perimeter())

class InsideDoubleSquare(Square):
    def __init__(self, x):
        super().__init__(x)
        self.x = x/2
        self.y = x/2

print("##### 3-2번 문제 #####")
ids = InsideDoubleSquare(8)
print(ids.area())
print(ids.perimeter())