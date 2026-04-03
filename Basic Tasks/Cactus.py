import FarmFunctions

def sort_and_harvest_cactus_field():
	size = get_world_size()

	# Pass 1: sort each row (line by line, West to East)
	for y in range(size):
		#FarmFunctions.moveTo(0, y)
		for i in range(size):
			FarmFunctions.moveTo(0, y)
			swapped = False
			# after i passes, last i elements are already in place
			for j in range(0, size - i - 1):
				if measure() > measure(East):
					swap(East)
					swapped = True
				move(East)
			# if no swaps happened this pass, the list is sorted
			if swapped == False:
				break
				

	# Pass 2: sort each column (top to bottom, South to North)
	for x in range(size):
		#FarmFunctions.moveTo(0, y)
		for i in range(size):
			FarmFunctions.moveTo(x, 0)
			swapped = False
			# after i passes, last i elements are already in place
			for j in range(0, size - i - 1):
				if measure() > measure(North):
					swap(North)
					swapped = True
				move(North)
			# if no swaps happened this pass, the list is sorted
			if swapped == False:
				break

change_hat(Hats.Cactus_Hat)
FarmFunctions.moveTo(0,0)
FarmFunctions.fullFarmTillV2(Grounds.Soil)

while num_items(Items.Pumpkin) > 0:
	FarmFunctions.moveTo(0,0)
	FarmFunctions.fullFarmPlant(Entities.Cactus)
	FarmFunctions.moveTo(0,0)
	sort_and_harvest_cactus_field()
	harvest()