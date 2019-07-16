def f1(n):
    for i in range(n):
        lst=list(range(1,i+2))
        print(*lst)

def f2(n):
    start=1
    for i in range(1,n+1):
        lst=list(range(start,start+i))
        start+=len(lst)
        print(*lst)

def f3(n):
    lst0=[]
    start=1
    for i in range(1,n+1):
        lst=list(range(start,start+i))
        start+=len(lst)
        lst0.append(lst)
        print(*lst)
    for i in range(n-2,-1,-1):
        print(*lst0[i])

def f4(n):
    start=1
    for i in range(1,n+1):
        lst=list(range(start,start+i))
        start+=len(lst)
        print(*lst)
    for i in range(n-1,-1,-1):
        lst0=list(range(start,start+i))
        start+=len(lst0)
        print(*lst0)

def f5(matrix):
    for row in matrix:
        sum=0
        for col in row:
            sum+= col
        print(sum)


def f6(matrix):
    for i in range(len(matrix)):
        print(matrix[i][i])

def f8(matrix):
    sum=0
    for row in matrix:
        for col in row:
            sum+=col
    print(sum)


def f9(matrix):
    cal=1
    for row in matrix:
        for col in row:
            cal*=col
    print(cal)

def f10(matrix):
    for row in matrix:
        for col in row:
            if col%2!=0:
                print(col, end=" ")
        print()


def f11(matrix1, matrix2):
    matrix3 =[]
    for i in range(len(matrix1)):
        row=[]
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j]+matrix2[i][j])
        matrix3.append(row)
    return matrix3


def f12(matrix1, matrix2):
    matrix3=[]
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum=0
            for k in range(len(matrix1[0])):
                sum+=matrix1[i][k]*matrix2[k][j]
            row.append(sum)
        matrix3.append(row)
    return matrix3


print(f12([[1,2,3],[4,5,6]],[[-1,-1],[-1,-1],[-1,-1]]))


def f13(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][i] !=1 :
                return False
            elif i != j and matrix[i][j] !=0:
                return False
    return True
print(  f13([[1,0,0],[0,1,5],[0,0,1]])  )

def f14(rows,cols):
    m= list([0]*(cols+2) for _ in range(rows+2))

    for i in range(1,rows+1):
        for j in range(1,cols+1):
            m[i][j]=1
    res=[]

    for i in range(1, rows + 1):
        row=[]
        for j in range(1, cols + 1):
            row.append((m[i-1][j]+m[i+1][j]+m[i][j-1]+m[i][j+1]))
        res.append(row)
    return res

print(f14(5,1))
