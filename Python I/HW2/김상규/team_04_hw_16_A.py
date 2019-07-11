# 1. Searching
def first_perfect_square(numbers):
    perfect_number = []
    flag = 0
    for i in range(len(numbers)):     
        if numbers[i] >= 0:            
            if numbers[i]**0.5 == int(numbers[i]**0.5):
                perfect_number.append(i)
                flag = 1
    if flag == 1:
        return perfect_number[0]
    else:
        return -1
            

# 2. Counting
def num_perfect_squares(numbers):
    perfect_number = []
    cnt = 0
    for i in range(len(numbers)):     
        if numbers[i] >= 0:            
            if numbers[i]**0.5 == int(numbers[i]**0.5):
                perfect_number.append(i)
                cnt = cnt+1
    return cnt
    
# 3. Second Largest Element
def second_largest(values):
    max = values[0]
    max_idx = 0
    for i in range(len(values)):
        if max < values[i]:
            max = values[i]
            max_idx = i
    values2 = values[:max_idx]+values[max_idx+1:]
    max2 = values2[0]
    for i in range(len(values2)):
        if max2 < values2[i]:
            max2 = values2[i]            
    print(max2)
    
    