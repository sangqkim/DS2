# 1
'''
Animal Class
생성할 때 "Animal created"를 print한다.
whoAmI라는 method가 있으며 "Animal"을 print한다.
eat이라는 method가 있으며 "Eating"을 print한다.

Dog Class
Animal class를 상속받는다.
생성할때 Animal의 초기값을 받는다.
따라서 "Animal created"를 print하고 "Dog created"를 print한다.
whoAmI라는 method가 있으며 "Dog"을 print한다.
bark라는 method가 있으며 "Woof"을 print한다.


Animal created
Dog created
Dog
Eating
Woof!
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


# 2
class Circle:

	def __init__(self):
		self.pie = 3.141592

	def area(self):
		return self.pie * self.r ** 2

	def setRadius(self, r):
		self.r = r

	def getRadius(self):
		return self.r


# 3
'''
Shape class
class를 생성할 때 x, y를 받으며 해당 값을 저장한다. 그리고 
description과 author이라는 member를 만든다.
area라는 method는 x와 y를 곱한 값을 return한다.
perimeter는 x와 y를 통해서 둘레를 구한다.
describe는 text parameter를 description에 저장한다.
authorName은 text parameter를 author에 저장한다.
scaleSize는 parameter로 받은 scale을 x와 y에 각각 곱해서 저장한다.

4500
290
1125.0
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
		return 2 * self.x + 2 * self.y

	def describe(self, text):
		self.description = text

	def authorName(self, text):
		self.author = text

	def scaleSize(self, scale):
		self.x = self.x * scale
		self.y = self.y * scale

class Square(Shape):

	def __init__(self, x):
		super().__init__(x, x)

class DoubleSquare(Square):

	def __init__(self, x):
		super().__init__(x)

	def area(self):
		return (self.x * self.y) * 2

	def perimeter(self):
		return (2 * self.x) * 2 + (2 * self.y)

class InsideDoubleSquare(Square):

	def area(self):
		return (self.x * self.y) * 2 * 0.25

	def perimeter(self):
		return (2 * self.x + 2 * self.y) / 2