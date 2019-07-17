class Programmer:
	pass

kim = Programmer()
park = Programmer()


class Ph:
	def printHam(self):
		print("Ham")

x = Ph()
x.printHam()

class Ph:
	def __init__(self):
		self.y = 5
		self.z = 5
	def printHam(self):
		print("Ham")
	def _inner(self):
		print("oing")

x= Ph()
x.printHam()
print(x.y)
print(x.z)

class Hero:
	def __init__(self, name):
		self.name = name
		self.health = 100

	def eat(self, food):
		if food == 'apple':
			self.health -= 100
		elif food == 'ham':
			self.health += 20
Bob = Hero('Bob')
print(Bob.name)
print(Bob.health)
Bob.eat('ham')
print(Bob.health)


class Service:

	def __init__(self, name):
		self.name = name

	def sum(self, a, b):
		result = a + b
		print("%s님, %s + %s = %s입니다." %(self.name, a, b, result))

pey = Service("홍길동")
pey.sum(1,1)


class BaseClass:
	def printHam(self):
		print('han')

class InheritingClass(BaseClass):
	pass

x = InheritingClass()
x.printHam()


class Foo:
	def __init__(self):
		self.health = 100

class SubFoo(Foo):
	def __init__(self):
		super().__init__()
		self.muscle = 200

testobj = SubFoo()
print(testobj.health)
print(testobj.muscle)

class A:
	def f(self):
		return self.g()
	def g(self):
		return 'A'

class B(A):
	def g(self):
		return 'B'

a = A()
b= B()
print(a.f(), b.f())
print(a.g(), b.g())


class BankAccount:
	def __init__(self):
		self.balance = 0

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		return self.balance

class MinimumBalanceAccount(BankAccount):
	def __init__(self, minimum_balance):
		super().__init__()
		self.minimum_balance = minimum_balance

	def withdraw(self, amount):
		if self.balance - amount < self.minimum_balance:
			print('sorry, minumum balance must be maintained')
		else:
			BankAccount.withdraw(self, amount)

class HousePark:
	lastname = '박'
	def __init__(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print("%s, %s여행을 가다." %(self.fullname, where))

	def love(self, other):
		print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))

	def __add__(self, other):
		print("%s, %s 결혼했네" %(self.fullname, other.fullname))

	def __sub__(self, other):
		print("%s, %s 이혼했네" %(self.fullname, other.fullname))

class HouseKim(HousePark):
	lastname = '김'
	def travel(self, where, day):
		print("%s, %s여행 %d일 가네." %(self.fullname, where, day))
