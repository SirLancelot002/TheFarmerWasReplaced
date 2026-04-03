import FarmFunctions

change_hat(Hats.Straw_Hat)
FarmFunctions.fullFarmTillV2(Grounds.Soil)
FarmFunctions.moveTo(1,0)
change_hat(Hats.Dinosaur_Hat)
dir = West

while num_items(Items.Cactus) > 1000:
	for j in range(get_world_size()):
		if dir == West:
			dir = East
		else:
			dir = West
		for i in range(get_world_size()-2):
			#if can_harvest():
			#	harvest()
			move(dir)
		if get_pos_y() < get_world_size()-1:
			move(North)
	FarmFunctions.moveToDumb(0, 0)
	move(East)
	dir = West
	