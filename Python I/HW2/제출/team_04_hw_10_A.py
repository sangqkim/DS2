def f1(lst):
	if len(lst) == 0:
		return 0
	else:
		return lst[0] + f1(lst[1:])


def f2(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		if n % 2 == 0:
			return f2(n//2) + 1
		else:
			return f2((3*n) + 1) + 1


def f3(lst):
	if len(lst) == 0:
		return
	else:
		f3(lst[1:])
		print(lst[0])


def f4(lst):
	if not lst:
		return
	else:
		if lst[0] % 2:
			print(lst[0]*3)
		f4(lst[1:])


def f5(lst):
	if len(lst) == 0:
		return
	else:
		f5(lst[1:])
		if lst[0] % 2 == 0:
			print(lst[0])
		else:
			print(lst[0] * 3)


def f6(lst):
	if not lst:
		return []
	else:
		if type(lst[0]) != list:
			return lst[0:1] + f6(lst[1:])
		else:
			return f6(lst[0]) + f6(lst[1:])


def f7(n):
	if n == 0:
		return 2
	elif n == 1:
		return 1
	else:
		return f7(n-1) + f7(n-2)


def f8(s):
	if len(s) == 0 or len(s) == 1:
		return True
	else:
		if s[0] == s[-1]:
			return f8(s[1:-1])
		else:
			return False


def f9(n):
	if n == 0:
		return 1
	else:
		return f9(n-1) * n


def f10(lst):
	if len(lst) == 0:
		return 0
	else:
		return 1 + f10(lst[1:])


def f11(lst):
	if len(lst) == 0:
		return
	elif len(lst) == 1:
		return(lst[0])
	else:
		return f11(lst[1:])


def f12(n):
	if n == 0 :
		return
	else:
		print(n)
		f12(n-1)


def f13(n):
	if n//10 == 0:
		return 1
	else:
		return f13(n//10) + 1


def f14(lst):
	if not lst:
		return None
	else:
		if lst[0] % 2:
			return lst[0]
		else:
			return f14(lst[1:])


def f15(lst):
	if not lst:
		return 0
	if lst[0] % 2 == 0:
		return f15(lst[1:])
	else:
		return lst[0] + f15(lst[1:])


def f16(lst):
	if not lst:
		return lst
	else:
		if lst[0] % 2:
			return lst[0:1] + f16(lst[1:])
		else:
			return f16(lst[1:])


def f17(lst):
	if len(lst) == 2:
		return lst[0]
	else:
		return f17(lst[1:])


def f18(a, b):
	if b == 0:
		return a
	else:
		return f18(b, a%b)


def f19(l1, l2):
	if not l1 or not l2:
		if not l1:
			return l2
		if not l2:
			return l1
	if l1[0] < l2[0]:
		return l1[0:1] + f19(l1[1:], l2)
	else:
		return l2[0:1] + f19(l1, l2[1:])


def f20(lst):
	if len(lst) == 0 or len(lst) == 1:
		return lst[:len(lst)]

	halfway = len(lst) // 2

	list1 = lst[0:halfway]
	list2 = lst[halfway:]

	newlist1 = f20(list1)
	newlist2 = f20(list2)

	newlist = f19(newlist1, newlist2)
	return newlist