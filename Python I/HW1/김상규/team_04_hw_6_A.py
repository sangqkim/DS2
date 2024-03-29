def f1(n):
    for i in range(1, n+1):
        for j in range(i):
            print(j+1, end=' ')
        print(end='\n')
        

def f1_1(n):
    for line in range(1, n+1):
        data = list(range(1, line+1))
        print(*data) # * 대괄호를 없애는 기능
             
    
def f2(n):
    cnt = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(cnt, end=' ')
            cnt = cnt+1
        print(end='\n')

def f2_1(n):
    start = 1
    for line in range(1, n+1):
        data = []
        for element in range(line):
            data.append(start)
            start = start + 1
        print(*data)
        

def f3(n):
    cnt = 1
    temp = []
    for i in range(1, n+1):
        data = []
        for j in range(i):
            data.append(cnt)
            cnt += 1
        temp.append(data)
    for i in range(n):
        print(*temp[i])
    for i in range(n-2, -1, -1):
        print(*temp[i])
        
def f4(n):
    cnt = 1
    for i in range(1, n+1):
        data = []
        for j in range(i):
            data.append(cnt)
            cnt += 1
        print(*data)    
    for i in range(n-1, 0, -1):  
        data = []
        for j in range(i):
            data.append(cnt)
            cnt += 1
        print(*data) 

def f5(matrix):
    for row in matrix:
        sum = 0
        for col in row:
            sum = sum + col
        print(sum)
    
def f6(matrix):
    idx = 0
    for i in range(len(matrix)):
        print(matrix[idx][idx])
        idx += 1
        
def f7(matrix):
    for row in matrix:
        sum = 0
        for col in row:
            sum = sum + col
        print(sum)


def f8(matrix):
    sum = 0
    for row in matrix:        
        for col in row:
            sum = sum + col
    print(sum)
    

def f9(matrix):
    result = 1
    for row in matrix:        
        for col in row:
            result = result * col
    print(result)
    
    
def f10(matrix):
    for row in matrix:
        for col in row:
            if col%2 == 1:
                print(col, end=' ')
        print('')


def f11(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j]+matrix2[i][j])
        matrix.append(row)
#    print(matrix)
    return matrix

   
def f12(matrix1, matrix2):
    result_matrix = []
    for row in range(len(matrix1)):
        result_row = []
        for col in range(len(matrix2[0])):            
            sum = 0
            for idx in range(len(matrix1[0])): # range(len(matrix2)) ??
                sum = sum + matrix1[row][idx]*matrix2[idx][col]
            result_row.append(sum)
        result_matrix.append(result_row)
    return result_matrix
        
        
        

def f13(matrix):
    result = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                if matrix[i][j] != 1:
                    result = False
            else:
                if matrix[i][j] != 0:
                    result = False
    return result
            

def f14(rows, cols):
    A = []
    for i in range(rows+2):
        a = []
        for j in range(cols+2):
            if i == 0 or i == rows+1 or j == 0 or j == cols+1:
                a.append(0)
            else:
                a.append(1)
        A.append(a)

    matrix = []
    for i in range(1, rows+1):
        row = []
        for j in range(1, cols+1):
            row.append(A[i-1][j]+A[i+1][j]+A[i][j-1]+A[i][j+1])
        matrix.append(row)
    return matrix
                