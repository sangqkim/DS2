### 1
def count_matches(lst, val):
	if len(lst) == 0:
		return 0
	else:
		if lst[0] == val:
			return 1 + count_matches(lst[1:], val)
		else:
			return count_matches(lst[1:], val)


### 2
def double_each(some_list):
	if not some_list:
		return []
	else:
		return (some_list[0:1] * 2) + double_each(some_list[1:])


### 3
def sums_to(lst, k):
	if len(lst) == 0:
		if k == 0:
			return True
		else:
			return False
	else:
		return sums_to(lst[1:], k-lst[0])


### 4
def is_reverse(s1, s2):
	if len(s1) == 0 and len(s2) == 0:
		return
	else:
		if s1[0] == s2[-1]:
			is_reverse(s1[1:], s2[:-1])
			return True
		else:
			return False


### 5
def sort_repeated(lst):
	check_set = set()
	answer_set = set()

	for i in lst:
		if i in check_set:
			answer_set.add(i)
		check_set.add(i)

	return sorted(answer_set)

### 6 처음 값만 유효하고 뒤에 중복된 값이 나오면 무시
def make_Dict_number(lst):
	ans = {}
	for i in lst:
		if i in ans:
			ans[i] += 1
		else:
			ans[i] = 1
	return ans

def mostFrequent(lst):
	ans = {}
	for i in lst:
		if i in ans:
			ans[i] += 1
		else:
			ans[i] = 1
	max = 0
	max_num = None
	for i in ans.keys():
		if max < ans[i]:
			max = ans[i]
			max_num = i
	return max_num


def mostFrequent(lst):
	ans = {}
	for i in lst:
		if i in ans:
			ans[i] += 1
		else:
			ans[i] = 1
	max = 0
	max_num = None
	for i in ans.keys():
		if max < ans.get(i):
			max = ans.get(i)
			max_num = i
	return max_num


### 7
def histogram(s):
	res_dict = {}
	for elm in s.values():
		if elm in res_dict:
			res_dict[elm] += 1
		else:
			res_dict[elm] = 1
	return res_dict
