USER_INT_MIN = 1
USER_INT_MAX = 10

def user_input_int():
	user_input:int = -1
	try:
		user_input = int(
			input(
				f"Veuillez saisir un nombre entre"
				f" {USER_INT_MIN} et {USER_INT_MAX}: "
			)
		)
	except:
		print( "erreur: la valeur saisie est invalide." )
		exit( 1 )
	return( user_input )

def enter_valid_number():
	valid = False
	while not valid:
		number = user_input_int()
		if number >= USER_INT_MIN and number <= USER_INT_MAX:
			valid = True
			print( f"La valeur {number} est valide!" )
			return number

def main():
	number = enter_valid_number()
	exit( 0 )

if __name__ == '__main__':
	main()
