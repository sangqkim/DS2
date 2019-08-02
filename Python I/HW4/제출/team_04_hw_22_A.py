# 22-A

# 1
# Parenthesis Matching
# version 1, Stack 직접 만들어 코딩
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
				p_lst.append('ERROR')
	if len(s.lst):
		if 'ERROR' in p_lst:
			pass
		else:
			p_lst.append('ERROR')
	print(*p_lst)


# version 2, python module 사용
import queue
def printMatchedPairs(lst):
	a = queue.LifoQueue()
	p_lst = []
	for i in range(len(lst)):
		if lst[i]=='(':
			a.put(i)
		elif lst[i]==')':
			try:
				idx = a.get(timeout=0.1)
				p_lst.append((idx, i))
			except:
				p_lst.append('ERROR')
	if not a.empty():
		if 'ERROR' in p_lst:
			pass
		else:
			p_lst.append('ERROR')
	print(*p_lst)

lst = "(a*(b+c)+d)"
p_check(lst)
lst = "(a*(b+c)+d)"
printMatchedPairs(lst)


# 2
def towersofhanoi(n,x,y,z):
	if n > 0:
		towersofhanoi(n-1, x,z,y)
		print("move the top disk from tower " + x + " to top of tower " + y)
		towersofhanoi(n-1,z,y,z)
towersofhanoi(4, 'x', 'y', 'z')