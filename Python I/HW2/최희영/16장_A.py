def first_perfect_square(lst):
    for i in range(len(lst)):
        if lst[i]>=0 and int((lst[i])**0.5)==(lst[i])**0.5:
            return i
    else:
        return -1

def num_perfect_squares(lst):
    hap=0
    for i in range(len((lst))):
        if lst[i]>=0 and int((lst[i])**0.5)==(lst[i])**0.5:
            hap= hap+1
    return hap


def second_largest(lst):
    max=lst[0]
    snd=lst[0]
    for ele in lst:
        if ele>=max:
            snd=max
            max=ele
        else:
            if ele>=snd:
                snd=ele
    return snd
