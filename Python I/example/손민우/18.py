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