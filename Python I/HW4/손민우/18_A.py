# 1
class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

class Pythagoras:

	def __init__(self):
		self.point_one = {}
		self.point_two = {}

	def setPointOne(self, Point):
		self.point_one = {'x': Point.x, 'y': Point.y}

	def setPointTwo(self, Point):
		self.point_two = {'x': Point.x, 'y': Point.y}

	def getSlope(self):
		return (self.point_two['y'] - self.point_one['y']) / (self.point_two['x'] - self.point_one['x'])

	def getDistance(self):
		return ((self.point_two['x'] - self.point_one['x'])**2 + (self.point_two['y'] - self.point_one['y'])**2) ** 0.5


# 2
class Calculator:

	def __init__(self):
		self.history = []
		self.n = 0

	def add(self, n):
		if len(self.history) == 0:
			self.n = n
			self.history.append(n)

		else:
			if isinstance(self.history[-1], int):
				self.n += n
				self.history.append('+')
				self.history.append(n)
			else:
				self.n = n
				self.history.append(n)

	def subtract(self, n):
		self.n -= n
		self.history.append('-')
		self.history.append(n)

	def multiply(self, n):
		self.n *= n
		self.history.append('*')
		self.history.append(n)

	def equals(self, check = False):
		if check:
			self.history.append('=')
			self.history.append(self.n)
			self.history.append('end')
			print(self.n)
		else:
			self.history.append('=')
			self.history.append(self.n)
			self.history.append('end')

	def show_history(self):
		if len(self.history) == 0 or not isinstance(self.history[0], int):
			self.history = []
			print('No calculation done yet!')

		else:
			print('History:')
			for i in self.history:
				if i == 'end':
					print()
				else:
					print(i, end=' ')

test = Calculator()
test.equals()
test.show_history()
test.add(2)
test.subtract(1)
test.equals()
test.show_history()

test.add(2)
test.multiply(4)
test.equals(True)

test.add(10)
test.subtract(5)
test.multiply(2)
test.equals()
test.show_history()

# 3

class Account:

	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
		self.transactions = []

	def deposit(self, amount):
		self.balance = self.balance + amount
		self.transactions.append(('deposit', amount))

	def withdrawal(self, amount):
		if amount > self.balance:
			return "Insufficient funds"

		self.balance = self.balance - amount
		self.transactions.append(('withdrawal', amount))

	def status(self):
		print(self.holder + ": ", end='')
		print(self.transactions)

# 4
'''
print(at)
6     0.0000     1.0000     2.0000
at.symbol()
'C'

print(mol)
This is a molecule named Water
It has 3 atoms
8     0.0000     0.0000     0.0000
1     0.0000     0.0000     1.0000
1     0.0000     1.0000     0.0000

* atom class
atom class를 생성할 떄 atno, x, y, z를 parameter로 받아 저장한다. 
x,y,z는 tuple로 묶어서 position에 저장한다.
symbol이라는 method는 기존에 선언되어 있던 Atno_to_Symbol이라는 dictionary에서 atno의 값에 해당하는 value를 return 한다.
__repr__은 atom class를 호출할 때 atno와 생성할 때 받은 x,y,z 값을 차례대로 return한다.

* molecule class
생성할 때 name을 parameter로 받아 저장하며 아무 값도 받지 않으면 'Generic'으로 저장한다. 또한, atomlist라는 list를 생성한다.
addatom method는 atom을 parameter로 받으며 받은 값을 atomlist에 append한다.
__repr__은 molecule class를 호출할 때 정의된 string과 parameter로 받은 name과 atomlist를 구현된 형식에 맞게 return한다.
'''
Atno_to_Symbol = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O'}


class atom:

	def __init__(self, atno, x, y, z):
		self.atno = atno
		self.position = (x, y, z)

	def symbol(self):
		return Atno_to_Symbol[self.atno]

	def __repr__(self):
		return '%d %10.4f %10.4f %10.4f' %(self.atno, self.position[0], self.position[1], self.position[2])

class molecule:
	def __init__(self, name='Generic'):
		self.name = name
		self.atomlist = []

	def addatom(self, atom):
		self.atomlist.append(atom)

	def __repr__(self):
		str = 'This is a molecule named %s\n' %self.name
		str = str + 'It has %d atoms\n' %len(self.atomlist)
		for atom in self.atomlist:
			str = str + '%s\n' % atom
		return str

# 5
class Person:

	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class Student(Person):

	def __init__(self, name, depart, year, credit):
		super().__init__(name)
		self.depart = depart
		self.year = year
		self.credit = credit

	def setDepart(self, depart):
		self.depart = depart

	def getDepart(self):
		return self.depart

	def setYear(self, year):
		self.year = year

	def getYear(self):
		return self.year

	def setCredit(self, credit):
		self.credit = credit

	def getCredit(self):
		return self.credit

	def increaseYear(self):
		self.year += 1

class Professor(Person):

	def __init__(self, name, course, depart, salary):
		super().__init__(name)
		self.course = course
		self.depart = depart
		self.salary = salary

	def getCourse(self):
		return self.course

	def getDepart(self):
		return self.depart

	def getAnnualSalary(self):
		return self.salary * 12

	def getSalary(self):
		return self.salary

	def raiseSalary(self, percent):
		increase_money = self.salary * (percent/100)
		self.salary += increase_money
		return self.salary

def calc_salary(Professor, year):

	salary = Professor.getAnnualSalary()
	return salary * year

def calc_incresed_salary(Professor, month, percent): # Month로 바꿈

	salary = Professor.getSalary()
	for _ in range(month):
		increase_money = salary * (percent / 100)
		salary += increase_money

	return salary

tim_cook = Professor('Tim Cook', 'Soft.Arch.', 'CSE',5500)
print(calc_salary(tim_cook, 5))
print(calc_incresed_salary(tim_cook, 5, 15))

# 6
class Person:

	def __init__(self, name, address):
		self.name = name
		self.addr = address

	def getName(self):
		return self.name

	def getAddress(self):
		return self.addr


class Staff(Person):

	def __init__(self, name, address, school, ann_pay):
		super().__init__(name, address)
		self.school = school
		self.ann_pay = ann_pay

	def getSchool(self):
		return self.school

	def getMonthlyPay(self):
		return self.ann_pay / 12

	def getAnnualPay(self):
		return self.ann_pay

	def raiseAnnualPay(self, percent):
		increase_money = self.ann_pay * (percent / 100)
		self.ann_pay += increase_money
		return self.ann_pay

class Student(Person):

	def __init__(self, name, address, GPA, year, fee):
		super().__init__(name, address)
		self.gpa = GPA
		self.year = year
		self.fee = fee

	def getGpa(self):
		return self.gpa

	def setGpa(self, gpa):
		self.gpa = gpa

	def hasMinimumGpa(self):
		if self.gpa > 3.5:
			return True
		else:
			return False

	def willGraduateNextYear(self):
		if self.year == 4:
			return True
		else:
			return False


def calc_incresed_salary(Staff, year, percent):

	salary = Staff.getAnnualPay()
	for _ in range(year):
		increase_money = salary * (percent / 100)
		salary += increase_money

	return salary

def who_has_a_lager_pay(Staff_A:Staff, Staff_B:Staff):

	# s1_pay = Staff_A.getMonthlyPay()
	# s2_pay = Staff_B.getMonthlyPay()
	s1_monthly_pay = calc_incresed_salary(Staff_A, 7, 7) / 12
	s2_monthly_pay = calc_incresed_salary(Staff_B, 7, 15) / 12

	if s1_monthly_pay > s2_monthly_pay:
		print(Staff_A.getName() + ' has a lager monthly pay')

	elif s2_monthly_pay > s1_monthly_pay:
		print(Staff_B.getName() + ' has a lager monthly pay')

	else:
		print('Same Same')


tom = Staff('Tom', 'Gangnam', 'Yonsei', 350000)
dane = Staff('Dane', 'Shindorim', 'Sogang', 20000)

calc_incresed_salary(tom, 7, 7)
calc_incresed_salary(dane, 7, 15)

who_has_a_lager_pay(tom, dane)



