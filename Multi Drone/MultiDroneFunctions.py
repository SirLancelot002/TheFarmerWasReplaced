target = 0.8
size = get_world_size()

def waterFullField():
	for i in range(size):
		for j in range(size):
			while get_water() < target:
				use_item(Items.Water)
			move(North)
		move(East)

def harvest_column():
	for _ in range(size):
		harvest()
		move(North)

def till_column(groundType):
	for _ in range(size):
		if can_harvest():
			harvest()
		if get_ground_type() != groundType:
			till()
		move(North)

def till_columnV2(groundType, plantT):
	for _ in range(size):
		if can_harvest():
			harvest()
		if get_ground_type() != groundType:
			till()
		if get_entity_type() != plantT:
			plant(plantT)
		move(North)