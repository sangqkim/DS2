import collections

# c = collections.Counter('olleh')
# print(c)
#
# c = collections.Counter()
# print(c)
#
# c = collections.Counter('gallhad')
# print(c)
#
# c = collections.Counter({'red': 4, 'blue': 2})
# print(c)
#
# c = collections.Counter(cats = 4, dogs = 8)
# print(c)

# d = collections.deque('abcdefg')
#
# d.remove('c')
# print(d)
#
# d.append('h')
# print(d)
#
# d.appendleft('X')
# print(d)
#
# d.pop()
# print(d)
#
# d.popleft()
# print(d)

# d = {'abc': 3, 'a': 4, 'b': 1, 'cd': 2}
# d.items()
# print(collections.OrderedDict(d))
# print(collections.OrderedDict(d.items()))

# import array
#
# s1 = 'This is the array.'
# s2 = 'Hello world'
#
# a = array.array('u', s1)
# b = array.array('u', s2)
#
# print(a)
# print(b)
#
# a.extend(b)
#
# print(a)

from bisect import bisect

grades = 'FEDCBA'
breakpoints = [30, 44, 66, 75, 85]

def grade(total):
	return grades[bisect(breakpoints, total)]

grade(66)
grade_map = map(grade, [33, 99, 77, 44, 12, 88])
print(grade_map)
print(list(grade_map))
