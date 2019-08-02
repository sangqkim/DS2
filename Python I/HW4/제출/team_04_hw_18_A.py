# 1
print("***** #1 *****")
class Point:
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



print()
print("***** #2 *****")
# 2
class Calculator:  
    
    def __init__(self):
        self.total = 0
        self.calc_str = []
        self.history = []
        self.n = 0
        
    def add(self, num):
        self.total += num
        self.n += 1
        if len(self.calc_str) == 0:
            self.calc_str.append(str(num))
        else:
            self.calc_str.append('+ ' + str(num))
    
    def subtract(self, num):
        self.total -= num
        self.n += 1
        self.calc_str.append('- ' + str(num))     
        
    def multiply(self, num):
        self.total *= num
        self.n += 1
        self.calc_str.append('* ' + str(num))
    
    def equals(self, equal=False): 
        if self.n != 0:            
            self.calc_str.append('= ' + str(self.total))
            self.history.append(self.calc_str)
            self.calc_str = []
            self.temp = self.total
            self.total = 0
            if equal == True:
                print(self.temp)           
    
    def showHistory(self):
        if self.n == 0:
            print("No calculation done yet!") 
            print("History:")
        else:
            print("History:")
            for i in range(len(self.history)):
                for j in range(len(self.history[i])):
                    print(self.history[i][j], end=' ')
                print()

test = Calculator()
test.equals()
test.showHistory()

test.add(2)
test.subtract(1)
test.equals()
test.showHistory()

test.add(2)
test.multiply(4)
test.equals(True)

test.add(10)
test.subtract(5)
test.multiply(2)
test.equals()
test.showHistory()

   
print()
print("***** #3 *****")
# 3
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount))
    
    def withdrawal(self, amount):
        
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        self.transactions.append(('withdrawal', amount))
            
    def status(self):
        print(self.holder + ": ", end=" ")
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
    tom_account.withdrawal(875)
    tom_account.status()

main()

print()
print("***** #4 *****")
      
      
# 4
Atno_to_Symbol = {1:'H', 2:'He', 3:'Li', 4:'Be', 5: 'B', 6:'C', 7: 'N', 8:'O'}
class atom(object):
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.position = (x, y, z)
        
    def symbol(self): # class method
        return Atno_to_Symbol[self.atno]
    
    def __repr__(self): # overloads printing
        return '%d %10.4f %10.4f %10.4f' %(self.atno, self.position[0], self.position[1], self.position[2])

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
    addatom method:
        atom object를 인수로 받으며 atomlist에 값을 추가한다.
    __repr__ method:
        str에 입력된 문장 출력과 함께 atom object에서 return된 값을 출력한다.
        
'''

at = atom(6, 0.0, 1.0, 2.0)
print(at)
at.symbol()


mol = molecule('Water')
at = atom(8, 0., 0. ,0.)
mol.addatom(at)
mol.addatom(atom(1, 0., 0., 1.))
mol.addatom(atom(1, 0., 1., 0.))
print(mol)

''' 출력 결과
6     0.0000     1.0000     2.0000
'C'
This is a molecule named Water
It has 3 atoms
8     0.0000     0.0000     0.0000 
1     0.0000     0.0000     1.0000 
1     0.0000     1.0000     0.0000

'''



print()
print("***** #5 *****")
# 5
class Person:
    def __init__(self, name, depart):
        self.name = name
        self.depart = depart
        self.year = 0
    def getName(self):
        return self.name    
    
    def getDepart(self):
        return self.depart
    
   
        
class Student(Person):
    def __init__(self, name, year):
        super().__init__(name)  
        self.year = year
        
    def setCredit(self, credit):
        self.credit = credit   
    
    def getCredit(self):
        return self.credit
    
    def increaseYear(self):
        self.year += 1            
   

class Professor(Person):
    def __init__(self, name, Depart, course, salary):
        super().__init__(name, Depart)
        self.course = course 
        self.salary = salary
    
    def getCourse(self):
        return self.course   
    
    def getAnnualSalary(self):
        return self.salary * 12
    
    def raiseSalary(self, percent):
        self.salary = self.salary * (1+percent/100)
        return self.salary


def calcTotalAmountSalary(professor, month, percent): # 기간은 month로 변경
    total = 0
    if percent == 0:
        for i in range(month):
            total += professor.raiseSalary(percent)
        print(month, " month salary : ", total)           
        
    else: 
        for i in range(month):
            total += professor.raiseSalary(percent)
        print(month, " month salary :", percent, "% raise: ", total)           
            
        

# Create an object called tim_cook 
tim_cook = Professor('Tim Cook', 'CSE', 'Soft.Arch.', 5500)

calcTotalAmountSalary(tim_cook, 5, 0)
calcTotalAmountSalary(tim_cook, 5, 15)




print()
print("***** #6 *****")
# 6
class Person:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def getName(self):
        return self.name
       
    def getAddress(self, address):
       return self.address    
    

class Staff(Person):
    def __init__(self, name, address, school, pay):
        super().__init__(name, address)
        self.school = school
        self.pay = pay
        
    def getSchool(self):
        return self.school
    
    def raiseAnnualPay(self, percent):
        self.pay = self.pay * (1+percent/100)
#        return self.pay
            
    def getAnnualPay(self):       
        return self.pay 
        
    def getMonthlyPay(self):
        return self.pay/12
        
    def comparePay(self, other):
        if self.pay > other.pay:
            print(self.name, " has a larger monthly pay")
        else:
            print(other.name, " has a larger monthly pay")
        

class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
    
    def setGpa(self, gpa):
        self.gpa = gpa
    
    def getGpa(self):
        return self.gpa
    
    def hasMinimumGpa(self):
        if self.gap >= 3.5: # gpa 3.5 이상으로 가정
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
        
# Create an object called tom and dane 
tom = Staff('tom'.title(), 'Gangnam', 'Yonsei', 35000)
dane = Staff('dane'.title(), 'Shindorim', 'Sogang', 20000)

calc_incresed_salary(tom, 7, 7)

calc_incresed_salary(dane, 7, 15)


who_has_a_lager_pay(tom, dane)