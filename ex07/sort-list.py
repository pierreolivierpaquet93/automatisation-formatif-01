
def user_input():
	user_input = input(
		"Veuillez saisir des nombres (separes par un espaces):"
	)
	user_input_lst = user_input.split( sep=' ' )
	numbers = []
	for i in user_input_lst:
		number = None
		try:
			number = int( i )
		except:
			pass
		if number:
			numbers.append( number )
	return numbers

def main():
	numbers = user_input()
	print( sorted(numbers) )

if __name__ == '__main__':
	main()
