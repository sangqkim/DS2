# 1
def count_matches(some_list, value) :
    if len(some_list) == 0:
        return 0
    else:
        if some_list[0] == value:
            return 1 + count_matches(some_list[1:], value)
        else:
            return count_matches(some_list[1:], value) 
    