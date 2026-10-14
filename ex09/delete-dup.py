def delete_dup( numbers_dup:list[int] ):
	numbers = []
	for n in numbers_dup:
		if n not in numbers:
			numbers.append( n )
	return numbers

def main():
	numbers_dup = [
		9,1,1,4,4,9,9,9,2,2,1,1,0
	]
	numbers = delete_dup(numbers_dup)
	print( numbers )

if __name__ == '__main__':
	main()
