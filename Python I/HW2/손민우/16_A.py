def check_perpect_squre(n):
	check = n ** 0.5
	try:
		if int(check) == check:
			return True
	except TypeError:
		return False
	return False


def first_perfect_square(lst):
	for i in range(len(lst)):
		if check_perpect_squre(lst[i]):
			return i
	return -1


def num_perfect_squares(lst):
	ans = 0
	for n in lst:
		if check_perpect_squre(n):
			ans += 1
	return ans


def second_largest(lst):
	maxx = lst[0]
	max_idx = 0
	for i in range(len(lst)):
		if lst[i] > maxx:
			maxx = lst[i]
			max_idx = i

	new_lst = lst[:max_idx] + lst[max_idx+1:]
	maxx = new_lst[0]
	for i in new_lst:
		if i > maxx:
			maxx = i

	return maxx



def print_french(lo, hi):

	for i in range(lo, hi+1):
		num_in_french(i)


def digit(num, pos):
	return (num // 10**(pos-1)) % 10


def num_in_french(num): # assumes 0 <= num <= 100
	ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix","onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
	tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

	### Step 1
	one = digit(num, 1)
	ten = digit(num, 2)
	hundred = digit(num, 3)

	if hundred:
		print("100 cent")
	elif 0 <= num <= 19:
		print('{} {}'.format(num, ones_list[one]))
	elif 20 <= num <= 69:
		if one == 0:
			print('{} {}'.format(num, tens_list[ten]))
		elif one == 1:
			print('{} {} et un'.format(num, tens_list[ten]))
		else:
			print('{} {}-{}'.format(num, tens_list[ten], ones_list[one]))
	elif 70 <= num <= 79:
		if one == 0:
			print('{} {}-dix'.format(num, tens_list[6]))
		else:
			print('{} {}-{}'.format(num, tens_list[6], ones_list[one + 10]))
	elif 80 <= num <= 89:
		if num == 80:
			print('{} {}-{}s'.format(num, ones_list[4], tens_list[2]))
		else:
			print('{} {}-{}-{}'.format(num, ones_list[4], tens_list[2], ones_list[one]))
	else:
		print('{} {}-{}-{}'.format(num, ones_list[4], tens_list[2], ones_list[one + 10]))
