# 16-B1
def count_matches(lst,v):
    if not lst:
        return 0
    else:
        if lst[0]==v:
            return 1+count_matches(lst[1:],v)
        else:
            return count_matches(lst[1:],v)



# 16-B2
def double_each(some_list):
    if len(some_list) == 0:
        return []
    else:
        return some_list[0:1]*2 + double_each(some_list[1:])




# 16-B3
def sums_to(nums,k):
    if len(nums) == 0:
        if k == 0:
            return True
        else:
            return False
    else:
        return sums_to(nums[1:],k-nums[0])


#16-B4
def is_reverse(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        if len(string1)==0 and len(string2)==0:
            return True
        else:
            if string1[0] == string2[-1]:
                is_reverse(string1[1:],string2[:-1])
                return True
            else:
                return False


#16-B5
def sort_repeated(L):
    elm_set=set()
    re_elm_set=set()
    for elm in L:
        if elm in elm_set:
            re_elm_set.add(elm)
        elm_set.add(elm)
    return sorted(re_elm_set)



#16-B6
def make_Dict_number(lst):
    dict={}
    for l in lst:
        if l in dict:
            dict[l]+=1
        else:
            dict[l]=1
    return  dict



def mostFrequent(lst):
    dict={}
    for l in lst:
        if l in dict:
            dict[l]+=1
        else:
            dict[l]=1

    max=0
    sol=0
    for m,l in dict.items():
        if l > max:
            max = l
            sol = m
    return sol



def mostFrequent_get(lst):
    dict={}
    for l in lst:
        if l in dict:
            dict[l]+=1
        else:
            dict[l]=1

    max=0
    sol=0
    for i in dict.keys():
        if dict.get(i) > max:
            max = dict.get(i)
            sol = i
    return sol



#16-B7
def histogram(d):
    res_dict={}
    for elm in d.values():
        if elm in res_dict:
            res_dict[elm]+=1
        else:
            res_dict[elm]= 1
     return res_dict
