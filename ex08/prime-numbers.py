INT_MIN=1
INT_MAX=1000

def prime_numbers(threshold=1):
	prime_nums = []
	limit = 0
	for i in range(INT_MIN,INT_MAX):
		divider = 2
		while divider <= i:
			if divider == i:
				limit += 1
				prime_numbers.append(i)
			division = i/divider
			tmp = divider*int(division)
			if tmp == i:
				break
			divider += 1
		if limit == threshold:
			break
	return prime_nums

def main():
	print( prime_numbers(25) )

if __name__ == '__main__':
	main()
