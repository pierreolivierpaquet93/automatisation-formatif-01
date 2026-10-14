def print_hi( name='' ):
	print( f"Bonjour, {name}!" )

def main():
	user_input = input( "name: " )
	print_hi( user_input )

'''
	La variable __name__ est une variable speciale qui vaut '__main__' si le
	script est execute directement, et prend le nom du module s'il est importe.
'''
if __name__ == "__main__":
	main()
