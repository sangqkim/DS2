def check_perpect_squre(n):
	check = n ** 0.5
	if int(check) == check:
		return True
	return False
def first_perfect_square(lst):
	for i in range(len(lst)):
		if check_perpect_squre(lst[i]):
			return i
	return -1

if __name__ == '__main__':
	print(first_perfect_square([6,8,10,12,9]))