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
			return 'queue is full'

		self.rear += 1
		if self.rear >= self.M:
			self.rear %= self.M

		self.queue[self.rear] = element

	def dequeue(self):
		if self.is_empty():
			return 'queue is empty'

		self.front += 1
		if self.front >= self.M:
			self.front %= self.M

		return self.queue[self.front]

	def multi_dequeue(self, count):
		for _ in range(count):
			self.dequeue()

	def peek(self):
		return self.queue[self.front]

	def is_empty(self):
		if self.front == self.rear:
			return True
		else:
			return False

	def is_full(self):
		if self.front % self.M == (self.rear+1) % self.M:
			return True
		else:
			return False

