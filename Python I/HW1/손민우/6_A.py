def f1(n):
	for line in range(1, n+1):
		for i in range(line):
			print(i+1, end=' ')
		print()


def f2(n):
	ans = 1
	for line in range(1, n+1):
		for i in range(line):
			print(ans, end=' ')
			ans += 1
		print()


def f3(n):
	ans = 1
	for line in range(1, n + 1):
		for i in range(line):
			print(ans, end=' ')
			ans += 1
		print()
	start = ans - n
	for line in range(n-1, 0, -1):
		start -= line
		ans = start
		for i in range(line):
			print(ans, end=' ')
			ans += 1
		print()


def f4(n):
	ans = 1
	for line in range(1, n + 1):
		for i in range(line):
			print(ans, end=' ')
			ans += 1
		print()
	for line in range(n-1, 0, -1):
		for i in range(line):
			print(ans, end=' ')
			ans += 1
		print()


def f5(data):
	for each_data in data:
		summ = 0
		for i in each_data:
			summ += i
		print(summ)


def f6(data):
	for i in range(len(data)):
		print(data[i][i])


def f7(data):
	for each_data in data:
		summ = 0
		for i in each_data:
			summ += i
		print(summ)


def f8(data):
	summ = 0
	for each_data in data:
		for i in each_data:
			summ += i
	print(summ)


def f9(data):
	ans = 1
	for real in data:
		for i in real:
			ans *= i
	return ans


def f10(data):
	for each_data in data:
		dd = []
		for i in each_data:
			if i % 2 != 0:
				dd.append(i)
		print(*dd)


def f11(matrix1, matrix2):
	col = len(matrix1)
	row = len(matrix1[0])
	ans = matrix1
	for i in range(col):
		for j in range(row):
			ans[i][j] = matrix1[i][j] + matrix2[i][j]
	return ans


def f12(mat1, mat2): #TODO:: fix
	ans = [len(mat2[0]) * [0] for i in range(len(mat1))]

	for i in range(len(ans)):
		for j in range(len(ans[i])):
			for k in range(len(mat1[i])):
				ans[i][j] += mat1[i][k] * mat2[k][j]
	return ans


def f13(matrix):
	ans = True
	col = len(matrix)
	for i in range(col):
		for j in range(col):
			if i == j:
				if matrix[i][j] != 1:
					ans = False
			else:
				if matrix[i][j]:
					ans = False
	return ans


def f14(rows, cols):
	ans = [[0 for _ in range(cols)] for _ in range(rows)]
	for i in range(cols):
		for j in range(rows):
			cnt = 0
			if i-1 >= 0:
				cnt += 1
			if i+1 < cols:
				cnt += 1
			if j-1 >= 0:
				cnt += 1
			if j+1 < rows:
				cnt += 1
			ans[j][i] = cnt
	return ans

if __name__ == '__main__':
	data1 = [[1,2,3],[4,5,6],[7,8,9]]
	data2 = [[1,2,3],[4,5,6]]
	data3 = [[1],[2],[3],[4]]
	#f12([[1,2,3],[4,5,6]], [[-1,-1],[-1,-1],[-1,-1]])
	# f12([[4,3,2,1]],[[1],[2],[3],[4]])
	f12([[1,0],[0,1]],[[1,0],[0,1]])