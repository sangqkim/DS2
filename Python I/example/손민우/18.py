class Peroson:
	def __init__(self, name):
		self.name = name
		print(self.name)

	def Sayhello(self):
		print("Hello, my name is", self.name)

class A:
	def A(self):
		print('I Am A')

class B:
	def A(self):
		print('I am a')
	def B(self):
		print('I am B')

class C(A,B):
	def c(self):
		print('I am C')

