def distance(
		coordinate1:tuple[int,int],
        coordinate2:tuple[int,int]
	):
	print( f"FROM={coordinate1} :: TO={coordinate2}" )

def total_distance( coordinates:list[tuple[int,int]] ):
	if coordinates:
		prev_coordinate = coordinates[0]
	else:
		print( f"erreur: coordonnees manquantes." )
		exit(1)
	for coordinate in coordinates[1:]:
		prev_coordinate = coordinate
		distance(
			coordinate1=prev_coordinate,
			coordinate2=coordinate
		)
		

def main():
	coordinates = [
		(1,2),
		(1,2),
		(3,4),
		(-5,-6),
		(-7,8)
	]
	total_distance( coordinates=coordinates )

if __name__ == '__main__':
	main()
