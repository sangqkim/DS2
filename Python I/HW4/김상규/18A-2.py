class Calculator:

    def __init__(self):
        self.history =""
        self.temp = 0

    def add(self, x):
        if not (self.history == "" or self.history[-1] =="\n"):
            self.history+=" + "+str(x)
        else:
            self.history += str(x)
        self.temp += x


    def substract(self, x):
        if not (self.history == "" or self.history[-1] == "\n"):
            self.history += " - "+str(x)
        else:
            self.history += str(x)
        self.temp -= x

    def multiply(self, x):
        if not (self.history == "" or self.history[-1] == "\n"):
            self.history += " * " +str(x)
        else:
            self.history += str(x)
        self.temp *= x

    def equals(self, boolean=False):
        if boolean:
            print(self.temp)
        if not (self.history == "" or self.history[-1] == "\n"):
            self.history += " = %d\n"%self.temp
            self.temp=0

    def showHistory(self):
        if self.history == "":
            print("No calculation done yet!\nHistory:")
        else:
            print("History:")
            print(self.history, end=" ")
