def f1(list):
    cnt = 0
    for i in list:
        if i%2 != 0 :
            cnt = cnt + 1
    return cnt


def f2(list):
    for i in list:
        if i%2 != 0 :
            print(i)
            
            
def f3(list):
    sum = 0
    for i in list:
        if i%2 != 0 :
            sum = sum + i
    return sum


def f4(list):
    sum = 0
    for i in range(len(list)):
        if list[i]%2 != 0 :
            sum = sum + i
    return sum


def f5(list):
    result = []
    for i in list:
        result.append(i**2)
    return result


def f6(list):
    max = 0
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
    return max
    

def f7(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    avg = sum/len(list)
    return avg


def f8(a, b, n):
    for i in list(range(a, b+1)):
        if i%n == 0:
            print(i)


def f9(width, height):
    line = '*' * width
    for i in range(height):
        print(line)
        
        
def f10(n):
    for i in range(1, n+1):
        print('*'*i)
        

def f11(list):
    result = 1
    if len(list) == 0:
        return True
    else:
        for i in range(len(list)-1):
            if list[i] < list[i+1]:
                result = result * 0
            else:
                result = result * 1
        if result == 1:
            return True
        else:
            return False
    
     
def f12(list):
    result = True
    for i in range(len(list)):
        if list[i] >= 0:
            result = False
    return result


def f13(list, target):
    idx = 0
    for i in range(len(list)):
        if list[i] == target:
           idx = i
    return idx


def f14(list):
    idx = 0
    for i in range(len(list)):
        if list[i] < 0:
            idx = i
    return idx


def f15(list):
    sum = 0
    for i in range(len(list)):
        if i %2 == 0:
            sum = sum+list[i]
    return sum


def f16(n):
    for i in range(n, 0, -1):
        print('*'*i)
        
        
def f17(list):
    for i in range(len(list)-1, -1, -2):
        print(list[i])
        

def f18(n):
    result = 1
    while(n):
        result = n*result
        n = n - 1
    return result
        
        
def f19(list):
    for i in range(len(list)):
            n = list[i]
            temp = 1
            while(n):
                temp = n*temp
                n = n - 1
            print(temp)


def f20(list):    
    for i in range(len(list)):
        n = list[i]
        while(n+1):
            print(n, end=' ')
            n = n - 1
        print()


def f21(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i]+list2[i])
    return result


def f22(n):
    for i in range(1, n+1):
        if i%2 == 0 or i%3 == 0 :
            print(i)
            
    
def f23(list):
    max = -100000
    for row in range(len(list)):
        for col in range(len(list[row])):
            if max < list[row][col]:
                max = list[row][col]
    return max
            

def f24(list):
    max = -100000
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
    max2 = -10000
    for i in range(len(list)):
        if max2 < list[i] and list[i] < max:
            max2 = list[i]
    return max2


def f25(n):
    s = str(n)
    return int(s[0])


def f26(list):
    for row in list:
        max = -100000
        for i in range(len(row)):
            if max < row[i]:
                max = row[i]
        print(max)
            
