#1
import numpy as np

a = np.zeros(10)
#np.array([0 for _ in range(10)])
print("(1)")
print(a)
'''
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
'''

#2
a[4] = 1
print("(2)")
print(a)
'''
[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
'''

#3
a = np.arange(10, 50)
print("(3)")
print(*a, end=' ')
'''
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
'''
#4
a = np.arange(0, 25)
a = a.reshape(5,5)
#a = np.arange(0, 25).reshape(5,5)
print("\n(4)")
print(a)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
'''

#5
a = np.eye(5)
print("(5)")
print(a)
'''
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
'''

#6
np.random.seed(5)
a = np.random.random((5,5))
print("(6)")
print(a)
print("min value: ", a.min())
print("max value: ", a.max())
'''
[[0.22199317 0.87073231 0.20671916 0.91861091 0.48841119]
 [0.61174386 0.76590786 0.51841799 0.2968005  0.18772123]
 [0.08074127 0.7384403  0.44130922 0.15830987 0.87993703]
 [0.27408646 0.41423502 0.29607993 0.62878791 0.57983781]
 [0.5999292  0.26581912 0.28468588 0.25358821 0.32756395]]
min value:  0.08074126876487486
max value:  0.9186109079379216
'''

#7
a = np.ones((4,3))
b = np.random.random((3,2))
c = np.dot(a,b)
print("(7)")
print(a)
print(b)
print(c)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
[[0.20455555 0.69984361]
 [0.77951459 0.02293309]
 [0.57766286 0.00164217]]
[[1.56173299 0.72441888]
 [1.56173299 0.72441888]
 [1.56173299 0.72441888]
 [1.56173299 0.72441888]]
'''
#8
print("(8)")
#print(c.T)
print(c.transpose())
'''
[[1.56173299 1.56173299 1.56173299 1.56173299]
 [0.72441888 0.72441888 0.72441888 0.72441888]]
'''

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
'''
a
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
b
 [[25 26 27 28 29]
 [30 31 32 33 34]
 [35 36 37 38 39]
 [40 41 42 43 44]
 [45 46 47 48 49]]
Addition
 [[25 27 29 31 33]
 [35 37 39 41 43]
 [45 47 49 51 53]
 [55 57 59 61 63]
 [65 67 69 71 73]]
Subtraction
 [[-25 -25 -25 -25 -25]
 [-25 -25 -25 -25 -25]
 [-25 -25 -25 -25 -25]
 [-25 -25 -25 -25 -25]
 [-25 -25 -25 -25 -25]]
 '''