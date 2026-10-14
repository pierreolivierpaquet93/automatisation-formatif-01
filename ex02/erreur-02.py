number = 10
try:
	number = int( input( "Veuillez saisir un nombre: " ) )
except:
	print( "La valeur saisie est invalide: default: 10" )

if number%2 != 0:
	print( f'Le nombre {number} est impair.' )
else:
	print( f'Le nombre {number} est pair.' )
