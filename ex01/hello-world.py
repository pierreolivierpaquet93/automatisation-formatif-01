def print_hi( name='' ):
	print( f"Bonjour, {name}!" )

def main():
	user_input = input( "name: " )
	print_hi( user_input )

if __name__ == "__main__":
	main()
