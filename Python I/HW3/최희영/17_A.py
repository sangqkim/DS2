class Animal:
    def __init__(self): #class 생성할때 바로 받는 함수
        print("Animal created") #"Animal created"를 출력한다
    def whoAmI(self): #whoAmI라는 method
        print("Animal") #"Animal" print
    def eat(self): #eat라는 method
        print("Eating") #"Eating" print


class Dog(Animal): #Animal class를 상속받는다
    def __init__(self):
        super().__init__() #생성시 animal의 초기값을 받는다
        print("Dog created") #"Dog created"를 출력한다
    def whoAmI(self): #whoAmI라는 method
        print("Dog") #"Dog" print
    def bark(self): #bark라는 method
        print("Woof!") #"woof!" print

# >>>d=Dog()
# Animal created
# Dog created
# >>>d.whoAmI()
# Dog
# >>>d.eat()
# Eating
# >>>d.bark()
# Woof!

class Circle():
    def __init__(self):
        self.pi = 3.141592
    def area(self):
        return self.pi*(self.r **2)
    def setRadius(self,r):
        self.r = r
    def getRadius(self):
        return self.r



class Shape: #Shape이라는 class
    def __init__(self, x, y): #x,y를 변수로 받는다
        self.x =x
        self.y =y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
    def area(self): #area 메소드로 x,y를 이용한 면적을 구한다
        return self.x * self.y
    def perimeter(self): #perimeter란 메소드로 x,y를 이용한 둘레를 구한다
        return 2*self.x + 2* self.y
    def describe(self, text): #describe란 메소드로 text(설명)을 입력하여 변수에 반환한다
        self.description = text
    def authorName(self, text): #author란 메소드로 text()을 입력하여 변수에 반환한다
        self.author = text
    def scaleSize(self, scale): #scale이란 메소드로 sclae을 입력받고 instance 변수 x,y에 적용한다.
        self.x = self.x*scale
        self.y = self.y*scale

# >>>rectangle = Shape(100,45)
# >>>print(rectangle.area())
# 4500
# >>>print(rectangle.perimeter())
# 290
# >>>rectangle.describe("A wide rectangle, more than twice as wide as it is tall")
# >>>rectangle.scaleSize(0.5)
# >>>print(rectangle.area())
# 1125.0

class Square(Shape):
    def __init__(self, x):
        super().__init__(x,x)

class DoubleSquare(Square):

    def area(self):
        return (self.x * self.y)*2

    def perimeter(self):
        return (2*self.x)*2 + 2* self.y



class InsideDoubleSquare(Square):
    def __init__(self, x):
        super().__init__(x)
        self.x = x/2
        self.y = x/2
