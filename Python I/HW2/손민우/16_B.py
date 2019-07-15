def double_each(some_list):
	if not some_list:
		return []
	else:
		return (some_list[0:1] * 2) + double_each(some_list[1:])


def is_reverse(s1, s2):
	if len(s1) == 0 or len(s2) == 0:
		return
	else:
		if s1[0] == s2[-1]:
			is_reverse(s1[1:], s2[:-1])
			return True
		else:
			return False