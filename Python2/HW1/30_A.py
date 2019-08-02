import numpy as np

# 1
a = np.zeros(10)
print(a)

# 2
a[4] = 1

# 3
b = np.arange(10, 50)
print(b)

# 4
a = np.arange(25).reshape(5, 5)
print(a)

# 5
a= np.eye(5)
print(a)

# 6
a = np.random.random((5,5))
print(a)
print(a.min())
print(a.max())

# 7
a = np.ones((4,3))
b = np.random.random((3,2))
c = np.dot(a,b)
print(a)
print(b)
print(c)

# 8
print(c.transpose())

# 9
a = np.arange(25).reshape(5,5)
b= np.arange(25, 50).reshape(5,5)
c = a + b
d = a - b
print(a)
print(b)
print(c)
print(d)