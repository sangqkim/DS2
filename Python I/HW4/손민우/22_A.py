
class Stack:

	def __init__(self):
		self.lst = []

	def push(self, idx):
		self.lst.append(idx)

	def pop(self):
		return self.lst.pop()


def p_check(str):
	s = Stack()
	p_lst = []
	for idx, elm in enumerate(str):
		if elm == '(':
			s.push(idx)
		elif elm == ')':
			try:
				o_p_idx = s.pop()
				c_p_idx = idx
				p_lst.append((o_p_idx, c_p_idx))
			except:
				p_lst.append('no matching')
	if len(s.lst):
		print('error')
	print(*p_lst)


import queue

def printMatchedPairs(lst):
	a = queue.LifoQueue()

	for i in range(len(lst)):
		if lst[i]=='(':
			a.put(i)
		elif lst[i]==')':
			idx = a.get()
			print('({}, {})'.format(idx, i))
			print()


def towersofhanoi(n,x,y,z):
	if n > 0:
		towersofhanoi(n-1, x,z,y)
		print("move the top disk from tower " + x + " to top of tower " + y)
		towersofhanoi(n-1,z,y,z)