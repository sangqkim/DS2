class Peroson:
	def __init__(self, name):
		self.name = name
		print(self.name)

	def Sayhello(self):
		print("Hello, my name is", self.name)

class A:
	def A(self):
		print('I Am A')

class B:
	def A(self):
		print('I am a')
	def B(self):
		print('I am B')

class C(A,B):
	def c(self):
		print('I am C')

class A:
	def foo(self):
		print('excuting foo')

	@classmethod
	def class_foo(cls):
		print('excuting class_foo')

class Employee:
	empcount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empcount += 1

	def displayCOunt(self):
		print('Total Employee %d' %Employee.empcount)

	def displayEmployee(self):
		print('Name : ', self.name, ', Salary: ', self.salary)


class Vector:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d, %d)' %(self.a, self.b)

	def __add__(self, other):
		return Vector(self.a + other.a , self.b+other.b)

	def __eq__(self, other):
		print('Vector')


class Vector1:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d, %d)' % (self.a, self.b)

	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)

class Fraction:

	temp = 0
	def __init__(self, num, den):
		self.num = num
		self.den = den
		self.simplify()

	def simplify(self):
		g = Fraction.gcd(self.num, self.den)
		self.num = self.num//g
		self.den = self.den//g

	@staticmethod
	def gcd(a,b):
		while b != 0:
			(a, b) = (b, a%b)

		return a

class Mycollection:
	def __init__(self):
		self.size = 10
		self.data = list(range(self.size))

	def __iter__(self):
		self.index = 0
		return self

	def __next__(self):
		if self.index >= self.size:
			raise StopIteration

		n = self.data[self.index]
		self.index += 1
		return n

def gen():
	yield 1
	yield 2
	yield 3

g = gen()
print(type(g))

n = next(g)
print(n)
n = next(g)
print(n)
n = next(g)
print(n)
# n = next(g)
# print(n)
for x in gen():
	print(x)

def g(lst):
	if len(lst) == 0:
		return []
	else:
		if lst[0] % 2 == 0:
			return [lst[0]*10] + g(lst[1:])
		else:
			return g(lst[1:])