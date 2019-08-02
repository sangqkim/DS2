import queue

def printMatchedPairs(lst):
	a = queue.LifoQueue()

	for i in range(len(lst)):
		if lst[i] == '(':
			a.put(i)
		elif lst[i] == ')':
			idx = a.get()
			print('({}, {})' .format(idx, i))


def towersofhanoi(n,x,y,z):
	if n > 0:
		towersofhanoi(n-1, x,z,y)
		print("move the top disk from tower " + x + " to top of tower " + y)
		towersofhanoi(n-1,z,y,z)