class CircularQueue:

	M = 0
	front = 0
	rear = 0
	queue = 0

	def __init__(self, maxsize):
		self.M = maxsize
		self.queue = [None] * maxsize

	def enqueue(self, element):
		if self.is_full():
			return

		self.rear += 1
		if self.rear >= self.M:
			self.rear %= self.M

		self.queue[self.rear] = element

	def dequeue(self):
		if self.is_empty():
			return

		self.front += 1
		if self.front >= self.M:
			self.front %= self.M

		return self.queue[self.front]

	def multi_dequeue(self, count):
		pass

	def peek(self):
		pass

	def is_empty(self):
		pass

	def is_full(self):
		pass

