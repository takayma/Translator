def translator (num, system_from, system_to):
	num = [int(i) for i in str(num)] 
	total = 0
	for i in range(len(num)):
		if system_from == 16:
			if num[i] == 'A': num[i] = 10
			if num[i] == 'B': num[i] = 11
			if num[i] == 'C': num[i] = 12
			if num[i] == 'D': num[i] = 13
			if num[i] == 'E': num[i] = 14
			if num[i] == 'F': num[i] = 15
		total += system_from ** (len(num) - 1 - i) * num[i]

	num = total
	total = []
	while num >= system_to:
		rem = num % system_to
		if system_to == 16:
			if rem == 10: rem = 'A'
			if rem == 11: rem = 'B'
			if rem == 12: rem = 'C'
			if rem == 13: rem = 'D'
			if rem == 14: rem = 'E'
			if rem == 15: rem = 'F'
		total.insert(0, f'{rem}')
		num //= system_to
	total = ''.join([str(num)] + total)
	return total

print(translator(1101010100101, 2, 16))
