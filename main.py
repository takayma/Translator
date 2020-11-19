def to_ten (num, system):
	num = list(str(num))
	total = 0
	i = 0
	while i < len(num):
		num[i] = int(num[i])
		if num[i] >= system:
			raise ValueError(f'Error in def to_ten, {num[i]} is bigger than system ({system})')
		total += system ** (len(num) - 1 - i) * num[i]
		i += 1
	return total

def from_ten (num, system):
	total = []
	while num > system:
		total.insert(0, f'{num % system}')
		num //= system
	total.insert(0, f'{num}')
	total = ''.join(total)
	return total

def translator (num, system1, system2):
	if system1 != 10:
		num = to_ten(num, system1)
	num = from_ten(num, system2)
	return num