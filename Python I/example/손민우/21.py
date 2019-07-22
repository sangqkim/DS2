class Node:
	def __init__(self, contents = None, next = None):
		self.contents = contents
		self.next = next

	def getContents(self):
		return self.contents

	def __str__(self):
		return str(self.contents)

def print_list(node):
	while node:
		print(node.getContents())
		node = node.next
	print()

def testList():
	node1 = Node('car')
	node2 = Node('bus')
	node3 = Node('lorry')
	node1.next = node2
	node2.next = node3
	print_list(node1)


class Stack:

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		if self.items == []:
			return True
		else:
			return False

	def peek(self):
		return self.items[len(self.items) - 1]

# myStack = Stack()
# myStack.push('john')
# myStack.push('kim')
# myStack.pop()
# myStack.items

class Queue:
	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)

	def delete(self):
		itemToDelete = self.items[0]
		del self.items[0]
		return itemToDelete

	def size(self):
		return len(self.items)

	def report(self):
		return self.items

# myQueue = Queue()
# myQueue.add('bob')
# myQueue.add('brodie')
# myQueue.add('carrie')
# myQueue.add('tanya')
# print(myQueue.size())
# print(myQueue.report())
# print(myQueue.delete())
# print(myQueue.report())


