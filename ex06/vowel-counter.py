VOWELS = "AaEeIiOoUuYy"

def vowel_counter( user_input:str ):
	if not user_input:
		return 0
	counter = 0
	for char in user_input:
		if char in VOWELS:
			counter += 1
	return counter
	
def main():
	user_input = input( "Veuillez saisir une phrase: " )
	count = vowel_counter( user_input )
	print( f"La phrase contient {count} voyelles." )

if __name__ == "__main__":
	main()
