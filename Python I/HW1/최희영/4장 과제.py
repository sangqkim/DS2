def f1(lst):
    hap = 0
    for i in range(len(lst)):

        if lst[i] %2 != 0:
            hap+=1
    return hap
print( f1([1,2,3,4,5]) )

def f2(lst):
    for i in range(len(lst)):

        if lst[i] %2 != 0:
            print(lst[i])

f2([1,2,3,4,5])

def f3(lst):
    sum=0
    for i in range(len(lst)):

        if lst[i] %2 != 0:
            sum+= lst[i]
    return sum
print(f3([1,2,3,4]) )


def f4(lst):
    sum=0
    for i in range(len(lst)):

        if lst[i] %2 != 0:
            sum+= i
    return sum
print(f4([1,2,3,4,5]) )

def f5(lst):
    a=[]
    for i in range(len(lst)):
        a.append(lst[i]**2)
    return a
print(f5([1,2,3,4,5]) )

def f6(lst):
    max=0
    for i in range(len(lst)):
        if max <= lst[i]:
            max =lst[i]
    return max
print(f6([1,2,3,4,5]) )


def f7(lst):
    sum=0
    for i in range(len(lst)):
        sum+= lst[i]
    return sum/len(lst)
print(f7([1,2,3,4,5]) )


def f8(a,b,n):
    for i in list(range(a,b+1)):
        if i % n ==0:
            print(i)

print( f8(1,10,2) )

def f9(width,height):
    for i in range(height):
        print ("*"*width)

def f10(n):
    for i in range(1, n+1):
          print("*"*i)
print( f10(3) )

def f11(lst):
      for i in range(len(lst)-1):
          if lst[i] < lst[i+1]:
              return False

      return True

print(f11([5,4,5,6]) )


def f12(lst):
    for i in range(len(lst)):
        if lst[i] >= 0:
            return False
    return True

print(( f12([-1,-2,-3,-4,5]) ))

def f13(lst,target):
    sol= -1
    for i in range(len(lst)):
        if lst[i] == target:
            sol= i
    return sol


print( f13([1,1,1,1], 1) )

def f14(lst):
    sol= -1
    for i in range(len(lst)):
            if lst[i] <0 :
                sol= i
    return sol

print( f14([1,2,3]) )

def f15(lst):
    sol=0
    for i in range(len(lst)):
        if (i+1)%2 != 0:
            sol+= lst[i]
    return sol

print( f15([1,2,-3])   )

def f16(n):
    for i in range(n,0,-1):
        print("*"*i)
print(f16(3) )

def f17(lst):
    for i in list(range(len(lst)-1, -1, -2)):
        print(lst[i])

print(f17([1,2,3,4,5,6]) )

def f18(n):
    sol = 1
    for i in range(n,0,-1):
        sol= sol* i
    return sol
print(f18(3) )

def f19(lst):
    sol = 1
    for elm in lst:
        sol= sol* elm
        print(sol)

print(f19([1,2,3,4])  )


def f20(lst):
    for elm in lst:
        for i in range(elm, -1, -1):
            print(i, end=" ")
        print( )

print( f20([])  )

def f21(lst1, lst2):
    a=[]
    for i in range(len(lst1)):
        a.append(lst1[i]+lst2[i])

    return a

print( f21([1,2,3], [1,2,3]) )

def f22(n):
    for i in range(1, n+1):
        if i%2 == 0 or i%3 == 0:
            print(i)

print(f22(3))

def f23(lst):
    max=0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst2=lst[i]
            if lst2[j] > max:
                max=lst2[j]
    return max

print(  f23([[3,2,1],[0,-1,9]])  )

def f24(lst):
    max=lst[0]
    snd=lst[0]
    for i in range(len(lst)):
        if max < lst[i]:
            snd=max
            max=lst[i]

    return snd

print( f24([1,4,3,2,5]) )
