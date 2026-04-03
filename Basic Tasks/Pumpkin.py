import FarmFunctions
change_hat(Hats.Wizard_Hat)
FarmFunctions.moveTo(0,0)
FarmFunctions.fullFarmTillV2(Grounds.Soil)
while (num_items(Items.Carrot) > 0):
	FarmFunctions.moveTo(0,0)
	FarmFunctions.fullFarmPlant(Entities.Pumpkin)
	failedToGrow = FarmFunctions.getEmptyCellsOnFullMapV2()
	while (not (len(failedToGrow) == 0)):
		#failedToGrow = FarmFunctions.order_cells_toroidal(failedToGrow)
		FarmFunctions.plantAtTargets(failedToGrow, Entities.Pumpkin)
		failedToGrow = FarmFunctions.getEmptyCells(failedToGrow)
	harvest()