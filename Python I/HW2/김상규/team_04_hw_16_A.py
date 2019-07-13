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
    

# 4.Print French Numbers 
##################################################################### 
# print french for the numbers between lo and hi (inclusive) 
def print_french(lo, hi): 
    
    for i in range(lo, hi+1):
        print(num_in_french(i))
    return None

def digit(num, pos): 
    return (num // 10**(pos-1)) % 10

def num_in_french(num): # assumes 0 <= num <= 100
    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six",
                 "sept", "huit", "neuf", "dix","onze", "douze", "treize", 
                 "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", 
                 "soixante", "soixante", "quatre-vingt", "quatre-vingt"]
       

    ones_digit = digit(num, 1)
    tens_digit = digit(num, 2)
    
#    print("Number: ", num)
#    print("tens digit: ",  tens_digit)
#    print("ones digit: ", ones_digit)
    
    if num == 100:
#        print('Number: 100')
        return str(num) + ' ' + 'cent'
    elif num >= 0 and num <= 19:
        return str(num) + ' ' + ones_list[num]  
    elif num >= 70 and num <= 79:
        if num == 71:
            return str(num) + ' ' + 'soixante et onze '
        else:
            return str(num) + ' ' + tens_list[tens_digit-1] + '-' + ones_list[num-60]
    elif num >= 90 and num <= 99: 
            return str(num) + ' ' + tens_list[tens_digit-1] + '-' + ones_list[num-80]
    elif num %10 == 0:
        if num == 80:
            return str(num) + ' ' + tens_list[tens_digit] + 's'
        else: 
            return str(num) + ' ' + tens_list[tens_digit]
    elif ones_digit == 1:
        if num == 81:
            return str(num) + ' ' + tens_list[tens_digit] + '-' + 'un'
        else: 
            return str(num) + ' ' + tens_list[tens_digit] + ' et un' 
    else:
        return str(num) + ' ' + tens_list[tens_digit] + '-' + ones_list[ones_digit]
    
    
    
# Part 1: get the ones and tens digits of num    
# Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 100
# Part 4: case when the numbers are 70, 71, 72,...79, and 90, 91, 92,...99
# Part 5: otherwise the case when the numbers are 20, 30, 40, ...
# Part 6: otherwise the case when the numbers are 21, 31, 41, ...
# Part 7: everything else, the most general case for 22, 23, ... 29, 32, 33, ..., 39, 42, ... ####################################################################################34  
    
    

    