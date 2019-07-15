def f1(list):
    if len(list) == 0:
        return 0
    else:
#        if len(list) == 1:
#            return list[0]
#        else:
        return list[0] + f1(list[1:])
    
def f2(n):
    if n == 1:
        return 1
    else:         
        if n%2 == 0:
            return f2(n//2)+1
        else:
            return f2(3*n+1)+1
                
    
def f3(list):
    if len(list) == 0:
        return
    else:
        f3(list[1:])
        print(list[0])


def f4(list):
    if len(list) == 0:
        return
    else:        
        if list[0]%2 != 0:
            print(list[0]*3)
        f4(list[1:])
            
        
def f5(list):
    if len(list) == 0:
        return
    else:
        f5(list[1:])
        if list[0]%2 != 0:
            list[0] = list[0]*3
        print(list[0])
      

def f6(lst):
    result = []
    if type(lst[0]) == list:
        return lst[0]
    else:
        result.append(return[lst[0]])
         
    
    
    
    
    
    
    
    
def f7(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return f7(n-1)+f7(n-2)
    
    
def f8(s):
    if len(s) == 0 or len(s) == 1:
        return True
    else: 
        if s[0] == s[-1]:
            return f8(s[1:-1])
        else:
            return False
        
    
    
def f9(n):
    if n == 0:
        return 1
    else:
        return f9(n-1)*n
    
    
def f10(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + f10(list[1:])    
    
    
def f11(list):
    if len(list) == 0:
        return
    elif len(list) == 1:
        return list[0]
    else:
        return f11(list[1:])
    
    
def f12(n):
    if n == 0:
        return 
    else: 
        print(n)
        f12(n-1)
        
        
def f13(n):
    if n//10 == 0:
        return 1
    else:
        return 1+f13(n//10)
    
    
def f14(list):
    if len(list) == 0:
        return 
    else:
        if list[0] %2 != 0:            
            return list[0]
        else: 
            return f14(list[1:])
        
    
def f15(list):
    if len(list) == 0:
        return 0
    else:
        if list[0] %2 != 0:
            return list[0] + f15(list[1:])
        else:
            return f15(list[1:])

#def f16(list):
#    if len(list) == 0:
#        return 
#    else:        
#        if list[0] %2 != 0:
#            return f16(list[1:])
#        else:
#            return f16(list[1:])

#def f16(list):
#    if len(list) == 0:
#        return list
#    else:
#        if list[0] %2 != 0:
#            return f16(list[1:])

    
def f17(list):
    if len(list) == 2:
        return list[0]
    else:
        return f17(list[1:])
    
    
#def f18(a, b):
#    if a>=b:
#        n = b
        
    
    

def f19(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        if len(list1) == 0:
            return list2
        if len(list2) == 0:
            return list2
    if list1[0] < list2[0]:
        return list1[0:1] +f19(list1[1:], list2)
    else:
        return list2[0:1] + f19(list1, list2[1:])
    

def f20(list):
    
    
    

    
