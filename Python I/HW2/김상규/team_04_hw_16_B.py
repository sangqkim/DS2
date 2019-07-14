# 1
def count_matches(some_list, value) :
    if len(some_list) == 0:
        return 0
    else:
        if some_list[0] == value:
            return 1 + count_matches(some_list[1:], value)
        else:
            return count_matches(some_list[1:], value) 

# 2
def double_each(some_list):
    if len(some_list) == 0:
        return []
    else:
        return some_list[0:1]*2 + double_each(some_list[1:])
    

# 3
def sums_to(nums, k):
    if len(nums) == 0:
        return False
    else:
        if nums[0] == k:
            return True
        else:
#            print("Nums: ", nums[1:], " k: ", k-nums[0] )
            return sums_to(nums[1:], k-nums[0])
    
# 4
def is_reverse(string1, string2):
    if len(string1) != len(string2):
        return False
    else: 
        if len(string1) == 0 and len(string2) == 0:
            return True
        else:
            if string1[0] == string2[-1]:
                return True and is_reverse(string1[1:], string2[:-1])
            else:
                return False
    
# 5
def sort_repeated(L):
    result = []
    while(L):
        for i in range(1, len(L)):
            if L[0] == L[i]:
                result.append(L[0])
        L = L[1:]
#    print(result)
    return list(set(result))
#    print(repeated_num)
    

 # 6
def make_Dict_number(lst):
    element = set(lst)
    dic = {}
    for i in element: 
        dic[i] = 1
    while(lst):
        for i in range(1, len(lst)):
            if lst[0] == lst[i]:
                dic[lst[0]] = dic[lst[0]] + 1
        lst = lst[1:]
    return dic
            
        
        
#def most_Frequent(lst):   
        
        
    
