import FarmFunctions

size = get_world_size()

def cactPlantLine():
	for i in range(get_world_size()):
		if get_entity_type() != Entities.Cactus:
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
		move(East)

def orderRow(y):
	for i in range(size):
		FarmFunctions.moveTo(0, y)
		swapped = False
		for j in range(0, size - i - 1):
			if measure() > measure(East):
				swap(East)
				swapped = True
			move(East)
		if swapped == False:
			break

def orderColumn(x):
	for i in range(size):
		FarmFunctions.moveTo(x, 0)
		swapped = False
		for j in range(0, size - i - 1):
			if measure() > measure(North):
				swap(North)
				swapped = True
			move(North)
		if swapped == False:
			break

change_hat(Hats.Cactus_Hat)
FarmFunctions.moveTo()
for i in range(size-1):
	def makemap():
		cactPlantLine()
		orderRow(i)
	spawn_drone(makemap)
	move(North)

cactPlantLine()
orderRow(size-1)
while num_drones() != 1:
	pass

for i in range(size-1):
	def secondPhase():
		orderColumn(i)
	spawn_drone(secondPhase)
orderColumn(size-1)

while num_drones() != 1:
	pass
harvest()