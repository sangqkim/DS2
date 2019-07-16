def f1(lst):
    if len(lst) ==0:
        return 0
    else:
        return lst[0]+f1(lst[1:])



def f2(n):
    if n<=1:
        return n
    else:
        if n%2 == 0:
            return 1+f2(n//2)
        else:
            return 1+f2(3*n+1)


def f3(lst):
    if len(lst) == 0:
        return
    else:
        f3(lst[1:])
        print(lst[0])



def f4(lst):
    if len(lst) == 0:
        return
    else:

        if lst[0] %2 !=0:
            print(lst[0]*3)
            f4(lst[1:])
        else:
            f4(lst[1:])


def f5(lst):
    if not lst:
        return
    else:
        if lst[0] %2 !=0:
            f5(lst[1:])
            print(lst[0]*3)
        else:
            f5(lst[1:])
            print(lst[0])


def f6(lst):

    if not lst:
        return []

    else:
        if type(lst) != list:
            return [lst]
        else:
            return f6(lst[0])+f6(lst[1:])

def f7(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return f7(n-1)+f7(n-2)

def f8(s):

    if len(s) == 0 or len(s) ==1:
        return True
    else:
        if s[0] == s[-1] :
            f8(s[1:len(s)-1])
            return True
        else:
            return False

def f9(n):
    if n<=1:
        return 1
    else:
        return n*f9(n-1)

def f10(lst):
    if not lst:
        return 0
    else:
        return 1+f10(lst[1:])

def f11(lst):
    if not lst:
        return
    elif len(lst)==1:
        return lst[0]
    else:
        return f11(lst[1:])


def f12(n):
    if n==0:
        return
    else:
        print(n)
        f12(n-1)

def f13(n):
    if n//10==0:
        return 1
    else:
        return 1+f13(n//10)


def f14(lst):
    if not lst:
        return
    else:
        if lst[0]%2 ==0:
            return f14(lst[1:])
        else:
            return lst[0]

def f15(lst):
    if not lst:
        return 0
    else:
        if lst[0]%2 ==0:
            return f15(lst[1:])
        else:
            return lst[0]+f15(lst[1:])

def f16(lst):
    if not lst:
        return []
    else:
        if lst[0]%2 ==0:
            return f16(lst[1:])
        else:
            return lst[0:1] + f16(lst[1:])

def f17(lst):
    if len(lst) == 2:
        return lst[0]
    else:
        return f17(lst[1:])

def f18(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return f18(b, a%b)

def f19(lst1,lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    else:
        if lst1[0]<lst2[0]:
            return lst1[0:1]+ f19(lst1[1:],lst2[0:])
        else:
            return lst2[0:1]+ f19(lst2[1:],lst1[0:])

def f20(lst):
    if len(lst)<=1 :
        return lst

    else:
        mid = int((len(lst)) / 2)
        left, right = f20(list(lst[:mid])), f20(list(lst[mid:]))

        return f19(left,right)

