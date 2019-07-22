# 1
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








# 3
#class Account:
#    def __init__(self, name):
#        self.name = name
#        self.transaction = []
#        self.deposit_value = 0
#    
#    def deposit(self, value):
#        self.depositve_value = value
#        self.transaction_log('deposit', value)
#    def transaction_log(self, keyword, value):
#        self.transaction_log(keyword, value)






print("*****")
# 5
class Person:
    def __init__(self, name):
        self.name = name
        self.year = 0
        
    # 빈 칸을 채워주는 method 만듬 setXXX()
    def setName(self, name):
        self.name = name
        
    def setDepart(self, depart):
        self.depart = depart
        
    def setCredit(self, credit):
        self.credit = credit
        
    def setCourse(self, course):
        self.course = course    
        
    def setSalary(self, salary):
        self.salary = salary
    
    def raiseSalary(self, percent):
        self.salary = self.salary * (1+percent/100)
        return self.salary
#        print(year, " year salary :", percent, "% raise: ", self.total_salary) 
        
    
    def getTotalSalary(self, year, percent):
        
        if percent == 0:
            self.increaseYear()
            self.total_salary = self.salary*year
            print(year, " year salary: ", self.total_salary)
            
        else:
            total = 0
            for i in range(year):
                self.increaseYear()
                total += self.raiseSalary(percent)                                    
            self.total_salary = total
            print(year, " year salary :", percent, "% raise: ", self.total_salary)           
        
    def increaseYear(self):
        self.year += 1  
    
    def getAnnualSalary(self, salary):
        self.salary = salary * 12        
   

class Professor(Person):
    def __init__(self, name):
        super().__init__(name)

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        

# Create an object called tim_cook 
tim_cook = Professor('Tim Cook')

# Set tim_cook values to match the data from the table 
tim_cook.setCourse('Soft.Arch.')
tim_cook.setDepart('CSE')
tim_cook.setSalary(5500)

# Write a code that will calculate the total amount of salary tim_cook will receive in five years
tim_cook.getTotalSalary(5, 0)

# Write a code that will calculate the total amount of salary of tim_cook if his salary is raised 15% every year for five year 
tim_cook.getTotalSalary(5, 15)



print("*****")
# 6
class Person:
    
    def __init__(self, name):
        self.name = name
  
    def setAddress(self, address):
       self.address = address
       
    def setSchool(self, school):
        self.school = school
    
    def setAnnualPay(self, pay):
        self.pay = pay
    
    def raiseAnnualPay(self, percent):
        self.pay = self.pay * (1+percent/100)
        return self.pay
    
    def getAnnualSalary(self, year, percent):
        for i in range(year):
            self.raiseAnnualPay(percent)
            

class Staff(Person):
    def __init__(self, name):
        super().__init__(name)

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        
# Create an object called tom and dane 
tom = Staff('tom'.title())
dane = Staff('dane'.title())

#  Set tom and dane values to match the data from the table 
tom.setAddress('Gangnam')
tom.setSchool('Yonsei')
tom.setAnnualPay(35000)

dane.setAddress('Shindorim')
dane.setSchool('Sogang')
dane.setAnnualPay(20000)

# Write a code that will calculate tom and dane annual salary after seven year
tom.getAnnualSalary(7, 7)
dane.getAnnualSalary(7, 15)
#print(tom.pay)
#print(dane.pay)

# Write a code to see who has a larger monthly pay 
# 여기 해야함.
