import FarmFunctions

size = get_world_size()
#set_world_size(100)

change_hat(Hats.Traffic_Cone)
FarmFunctions.moveTo()
for i in range(size):
		for j in range(size):
			FarmFunctions.plantRandomPoly()
			move(North)
		move(East)
	
while (True):
	FarmFunctions.moveTo()
	for i in range(size):
		for j in range(size):
			FarmFunctions.makeCompanion()
			harvest()
			FarmFunctions.plantRandomPoly()
			if random() > 0.99:
				use_item(Items.Fertilizer)
			move(North)
		move(East)