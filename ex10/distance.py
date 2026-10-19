from math import sqrt

def distance(
		coordinate1:tuple[int,int],
		coordinate2:tuple[int,int]
	):
	#print( f"FROM={coordinate1} :: TO={coordinate2}" )
	delta_x = abs(coordinate2[0] - coordinate1[0])
	delta_y = abs(coordinate2[1] - coordinate1[1])
	#print( f"DELTA_X={delta_x} :: DELTA_Y={delta_y}" )
	distance = sqrt( (delta_x**2) +(delta_y**2) )
	#print( f"DISTANCE={distance}" )
	return distance

def total_distance( coordinates:list[tuple[int,int]] ):
	if coordinates:
		prev_coordinate = coordinates[0]

	else:
		print( f"erreur: coordonnees manquantes." )
		exit(1)

	total_distance:float = 0.0
	for coordinate in coordinates[1:]:
		total_distance += distance(
			coordinate1=prev_coordinate,
			coordinate2=coordinate
		)
		prev_coordinate = coordinate
	return total_distance
		

def main():
	coordinates = [
		(1,2),
		(4,8),
		(14,45),
		(-10,-3),
		(-34,54)
	]
	result = total_distance( coordinates=coordinates )
	print( f"Distance totale = '{result:.2f}'" )

if __name__ == '__main__':
	main()
