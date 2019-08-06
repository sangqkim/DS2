#1
import numpy as np

a = np.zeros(10)
#np.array([0 for _ in range(10)])
print("(1)")
print(a)

#2
a[4] = 1
print("(2)")
print(a)

#3
a = np.arange(10, 50)
print("(3)")
print(*a, end=' ')

#4
a = np.arange(0, 25)
a = a.reshape(5,5)
#a = np.arange(0, 25).reshape(5,5)
print("\n(4)")
print(a)

#5
a = np.eye(5)
print("(5)")
print(a)

#6
np.random.seed(5)
a = np.random.random((5,5))
print("(6)")
print(a)
print("min value: ", a.min())
print("max value: ", a.max())

#7
a = np.ones((4,3))
b = np.random.random((3,2))
c = np.dot(a,b)
print("(7)")
#print(a)
#print(b)
print(c)

#8
print("(8)")
#print(c.T)
print(c.transpose())

#9
a = np.arange(25).reshape(5,5)
b = np.arange(25,50).reshape(5,5)
c = a+b
d = a-b
print("(9)")
print("a\n", a)
print("b\n", b)
print("Addition\n", c)
print("Subtraction\n", d)
