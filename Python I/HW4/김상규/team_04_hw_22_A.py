# 22-A

# 1
# Parenthesis Matching
class Stack:    
    # the stack class
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
#         return self.items[len(self.items)-1] # top element를 return
        return self.items[-1] # top element를 return
    
           
#def p_check(str):
#    s = Stack()
#    p_lst = []
#    for idx, elm in enumerate(str):
#        if elm == "(":
#            s.push(idx)
#        elif elm == ")":
#            o_p_idx = s.pop()
#            c_p_idx = idx
#            p_lst.append((o_p_idx, c_p_idx))
            

#def parenthesisMatching(lst):
#    s = Stack()
#    for i in range(len(lst)):
#        if lst[i] == "(":
#            s.append(i)
#        elif lst[i] == ")":
#            idx = s.pop()
            
            
# version 2
def parenthesisMatching(lst):
    import queue
    s = queue.LifoQueue(len(lst))
    
    for i in range(len(lst)):
        if lst[i] == "(":        
            s.put(i)
        elif lst[i] == ")":
            idx = s.get()
#            print('({},{})'.format(idx, i))
            print('(%d,%d)' %(idx, i))
            

lst = "(a*(b+c)+d)"
parenthesisMatching(lst)





# 2
def towerOfHanoi(n, x, y, z):
    if n > 0:
        towerOfHanoi(n-1, x, z, y)
        print("Move the top disk from tower " + x + " to top of tower " + y)
        towerOfHanoi(n-1, z, y, x)

towerOfHanoi(4, "x", "y", "z")


# 3
class node:
    def _init_(self, val, left=None, right=None): # default value는 항상 뒤에 써야함.
        self.val = _val
        self.left = _left
        self.right = _right
        
    
    
        