def increment( x=0 ):
	x = x + 1
	return x

def main():
	user_input = 0
	try:
		user_input = int(input( "Veuillez entrer un chiffre: " ))
	except:
		print( "La valeur saisie n'est pas un nombr: default: 0" )
	
	print( increment( user_input ) )

if __name__ == '__main__':
	main()
