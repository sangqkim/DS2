def double_each(some_list):
	if not some_list:
		return []
	else:
		return (some_list[0:1] * 2) + double_each(some_list[1:])