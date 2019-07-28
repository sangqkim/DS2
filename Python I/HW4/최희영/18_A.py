#Advanced  OOP 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pythagoras:
    def __init__(self):
        self.point_one ={}
        self.point_two ={}

    def setPointOne (self, Point):
        self.point_one = {'x':Point.x, 'y':Point.y}

    def setPointTwo (self, Point):
        self.point_two = {'x':Point.x, 'y':Point.y}

    def getSlope(self):
        if (self.point_two['x'] - self.point_one['x']) ==0:
            print("Set another x values for PointOne and PointTwo")
        return  (self.point_two['y'] - self.point_one['y'])/(self.point_two['x'] - self.point_one['x'])

    def getDistance(self):
        return ((self.point_two['x'] - self.point_one['x'])**2 +  (self.point_two['y'] - self.point_one['y'])**2)**0.5

#Advanced  OOP 2
class Calculator:
    def __init__(self):
        self.history =""
        self.temp = 0

    def add(self, x):
        if not (self.history =="" or self.history[-1] == "\n"):
            self.history += " + "+str(x)
        else:
            self.history += str(x)
        self.temp += x

    def substract(self, x):
        if not (self.history == "" or self.history[-1] == "\n"):
            self.history += " - "+str(x)
        else:
            self.history += str(x)
        self.temp -= x

    def multiply(self, x):
        if not (self.history == "" or self.history[-1] == "\n"):
            self.history += " * " +str(x)
        else:
            self.history += str(x)
        self.temp *= x

    def equals(self, boolean = False):
        if boolean:
            self.history += " = %d\n" % self.temp
            print(self.temp)
        else:
            if not (self.history == "" or self.history[-1] == "\n"):
                self.history +=" = %d\n"%self.temp
                self.temp=0

    def showHistory(self):
        if self.history == "":
            print("No calculation done yet!\nHistory:")
        else:
            print("History:")
            print(self.history, end=" ")

#Advanced  OOP 3
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions =[]

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(('deposit', amount))

    def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        self.transactions.append(('withdrawal', amount))

    def status(self):
        print(self.holder + ": ", end="")
        print(self.transactions)


def main():
    bob_account = Account('Bob')
    bob_account.deposit(1000000)
    bob_account.withdrawal(100)
    bob_account.deposit(440)
    bob_account.status()

    tom_account = Account('Tom')
    tom_account.deposit(5000000)
    tom_account.withdrawal(250)
    tom_account.deposit(875)
    tom_account.status()

#Advanced  OOP 4
Atno_to_Symbol = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O'}

class atom(object):
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.position = (x, y, z)

    def symbol(self):  # class method
        return Atno_to_Symbol[self.atno]

    def __repr__(self):  # overloads printing
        return '%d %10.4f %10.4f %10.4f' % (self.atno, self.position[0], self.position[1], self.position[2])


class molecule:
    def __init__(self, name='Generic'):
        self.name = name
        self.atomlist = []

    def addatom(self, atom):
        self.atomlist.append(atom)

    def __repr__(self):
        str = "This is a molecule named %s\n" % self.name
        str = str + 'It has %d atoms\n' % len(self.atomlist)
        for atom in self.atomlist:
            str = str + "%s \n" % atom
        return str


''' 코드 설명
Atno_to_Symbol은 원자 번호와 원자를 key-value pair를 갖는 dictionary 이다.
1) atom class
    __init__ method:
        클래스를 초기화시키면서 initial value (x,y,z)를 받는다.
        self.atno는 입력받은 atno를 받고, 
        self.position은 입력받은 x,y,z를 tuple type으로 받는다. 
    symbol method:
        self.atno에 맞는 Atno_to_Symbol의 value (원자기호)를 return 해준다.
    __repr__ method:
        atom 클래스로부터 생성된 object를 print할 때 출력되는 내용을 정의한다.
        출력 내용은 class 초기화 때 입력받은 self.atno와 x,y,z 값을 나타낸다.
2) molecule class
    __init__ method:
         클래스를 초기화시키면서 name이라는 초기값는 받는데, 
         default는 'Generic'이고, self.atomlist라는 빈 리스트를 생성한다.
         addatom method는 atom object를 인수로 받는다.
    __repr__ method:
        str에 입력된 문장 출력과 함께 atom object에서 return된 값을 출력한다.
'''
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
'''

#Advanced  OOP 5
class Person:
    def __init__(self, name):
        self.name = name
        self.year = 0

    def getName(self):
        return self.name

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

    def raiseSalary(self, perc):
        self.salary = self.salary * (1 + (perc/100))
        return self.salary

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

#for 5 years salary
def calc_salary(Professor, year):
    salary = Professor.getAnnualSalary()
    total= salary*year
    print("%d year salary: " %year, total)

#month 로 문제가 바뀜
def calc_increased_salary(Professor, month, perc):
    salary = Professor.getSalary()
    result = 0
    for i in range(month):
        salary = salary * (1 + (perc / 100))
        result += salary
    print("%d month salary %d%% raise : " %(month, perc), result)

tim_cook = Professor('Tim Cook', 'Soft.Arch', 'CSE', 5500)
calc_salary(tim_cook, 5)
calc_increased_salary(tim_cook, 5, 15)


#Advanced  OOP 6
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

    def periodPay(self, year):
        total=0
        for i in range(year):
            total+= self.raiseAnnualPay(self.percent)
        return total

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

def calc_incresed_salary(Professor, year, percent):
    salary = Staff.getAnnualPay()
    for _ in range(year):
        increase_money = salary * (percent / 100)
        salary += increase_money

    return salary


def who_has_a_lager_pay(Staff_A:Staff, Staff_B:Staff):

    s1_monthly_pay = calc_incresed_salary(Staff_A, 7, 7) / 12
    s2_monthly_pay = calc_incresed_salary(Staff_B, 7, 15) / 12

    if s1_monthly_pay > s2_monthly_pay:
        print(Staff_A.getName() + ' has a lager monthly pay')

    elif s2_monthly_pay > s1_monthly_pay:
        print(Staff_B.getName() + ' has a lager monthly pay')

    else:
        print('Same Same')
