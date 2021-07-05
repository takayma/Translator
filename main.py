def f (a):
	arr1 = ['A', 'B', 'C', 'D', 'E', 'F']
	arr2 = [10, 11, 12, 13, 14, 15]
	if a in arr1:
		return arr2[arr1.index(a)]
	elif a in arr2:
		return arr1[arr2.index(a)]
	return a

def translator (num, system_from, system_to):
	num = [int(i) for i in str(num)] 
	total = 0
	for i in range(len(num)):
		num[i] = f(num[i])
		total += system_from ** (len(num) - 1 - i) * num[i]

	num = total
	total = []
	while num >= system_to:
		rem = num % system_to
		rem = f(rem)
		total.insert(0, f'{rem}')
		num //= system_to
	total = ''.join([str(num)] + total)
	return total

print(translator(1101010100101, 2, 16))
