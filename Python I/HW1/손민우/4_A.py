def f1(data):
    count = 0
    for i in data:
        if i % 2!=0:
            count += 1
    return count


def f2(data):
    for i in data:
        if i % 2!=0:
            print(i)


def f3(data):
    sum = 0
    for i in data:
        if i % 2!=0:
            sum += i
    return sum


def f4(data):
    sum = 0
    for i in range(0, len(data)):
        if data[i] % 2!=0:
            sum += i
    return sum


def f5(data):
    for i in data:
        print(i ** 2)


def f6(data):
    maxx = 0
    for i in data:
        if maxx < i:
            maxx = i
    return maxx


def f7(data):
    summ = 0
    for i in data:
        summ += i
    return summ / len(data)


def f8(a, b, n):
    for i in range(a, b + 1):
        if i % n==0:
            print(i)


def f9(width, height):
    star = '*' * width
    for i in range(height):
        print(star)


def f10(n):
    for i in range(n):
        print('*' * (i + 1))


def f11(data):
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            return False

    return True


def f12(data):
    for i in range(len(data)):
        if data[i] >= 0:
            return False

    return True


def f13(data, target):
    find = -1
    for i in range(len(data)):
        if data[i]==target:
            find = i
    return find


def f14(data):
    find = -1
    for i in range(len(data)):
        if data[i] <= 0:
            find = i
    return find


def f15(data):
    summ = 0
    for i in range(0, len(data)):
        if i % 2==0:
            summ += data[i]
    return summ


def f16(n):
    for i in range(n, 0, -1):
        print('*' * i)


def f17(data):
    for i in range(len(data) - 1, -1, -2):
        print(data[i])

def f18(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans


def f19(data):
    for n in data:
        ans = 1
        for i in range(1, n + 1):
            ans = ans * i
        print(ans)


def f20(data):
    for n in data:
        for i in range(n,-1,-1):
            print(i, end=' ')
        print()

def f21(l1, l2):
    ans = []
    for i in range(len(l1)):
        ans.append(l1[i] + l2[i])
    return ans

def f22(n):
    for i in range(2, n+1):
        if i % 2 == 0 or i % 3 == 0:
            print(i)

def f23(l):
    maxx = 0
    for data in l:
        for i in data:
            if i > maxx:
                maxx = i
    return maxx


def f24(lst):
    maxx = 0
    index = 0
    for i in range(len(lst)):
        if lst[i] > maxx:
            maxx = lst[i]
            index = i
    temp = lst[:index] + lst[index+1:]
    maxx = 0
    for i in temp:
        if i > maxx:
            maxx = i
    return maxx


def f25(n):
    i = 1
    while True:
        if n // i < 10:
            return n // i
        else:
            i *= 10

def f26(lst):
    for data in lst:
        maxx = data[0]
        for i in data:
            if maxx < i:
                maxx = i
        print(maxx)