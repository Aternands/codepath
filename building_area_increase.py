


def building_area_increase(variables):

	print "First, we'll look at frontage....when the code for this part is written....\n"

	#add frontage code here

	frontage_area_increase = 0








	print "Next, we'll look at sprinklers.\n"

	if variables["has_sprinkler"] == "no":
		sprinkler_area_increase = 0
		print ("Your building isn't equipped throughout with an approved sprinkler system, so you won't get"
				"a building area increase from sprinklers.\n")

	elif variables["has_sprinkler"] == "yes":
		if variables["group"] == "h1":
			sprinkler_area_increase = 0
			print ("Your building has an H-1 occupancy. Buildings with H-1 occupancies"
					" don't get allowable building area increases from sprinklers.\n")

		# 506.3 exception 2 for H-2 and H-3 occupancies. figure out and add this condition

		if variables["sprinkler_for_fire_resistance_rating"] == "yes":
			sprinkler_area_increase = 0
			print ("You're using the sprinkler system to substitute for 1-hour rated construction, so "
					"you cannot use it to increase your allowable building area.\n")


		else: 
			if variables["actual_stories"] < 2:
				sprinkler_area_increase = 3
			
			elif variables["actual_stories"] >= 2:
				sprinkler_area_increase = 2

			print "Your sprinkler system qualifies you for a building area increase.\n"

	initial_area_value = variables["max_area"]

	variables["max_area"] = variables["max_area"] + (variables["max_area"] * frontage_area_increase) + (variables["max_area"] * sprinkler_area_increase)

	if initial_area_value == variables["max_area"]:
		print ("You didn't qualify for sprinker or frontage increases to your building area."
				"Your allowable building area remains %s square feet.\n") % variables["max_area"]


	elif initial_area_value < variables["max_area"]:
		print "Great. Your allowable building area increased to %s square feet.\n" % variables["max_area"]


	return variables
				


























