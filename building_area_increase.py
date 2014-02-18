	


def building_area_increase(variables):


	#Building Area increase from frontage


	print "First, we'll look at frontage.\n"

	perimeter = raw_input("Please enter the length in feet of your building's perimeter.\n")

	print "\n"

	perimeter = float(perimeter)

	print "Okay, your building's perimeter length is %.2f feet.\n" % perimeter

	print "\n"




	frontage = raw_input("Your qualified frontage is the length of your building's perimeter"
							" that fronts on a public way, or on an open space with a minimum"
							" width of 20 feet. Please enter this length.\n")

	print "\n"


	frontage = float(frontage)

	if frontage > perimeter:
		print ("That can't be right... You've entered a frontage length that's larger than"
				" the overall perimeter length. Let's try for a building area increase again.\n")

	print "Okay, your building's frontage length is %.2f feet.\n" % frontage

	print "\n"

	min_frontage_percentage = .25

	actual_frontage_percentage = (float(frontage)/float(perimeter))

	if actual_frontage_percentage < min_frontage_percentage:
		frontage_increase_amount = 0
		print ("To qualify for a building area increase from frontage, at least"
				" 25 percent of your building's perimeter must have qualified frontage on a public way or"
				" qualified open space. Only %.2f percent of your building's perimeter has qualified frontage,"
				" so you won't get an increase.\n") % actual_frontage_percentage

		print "\n"

	else:

		width_consistent = raw_input("Is the frontage width consistent over the entire qualified frontage?"
				" Enter yes or no\n")

		print "\n"

		valid_yes_no = ["yes", "no"]

		if width_consistent not in valid_yes_no:
			print "You didn't enter yes or no. Let's try for a building area increase again.\n"

			print "\n"

			building_area_increase(variables)


		if width_consistent == "yes":
			width = raw_input("Please enter the width of the qualified public way/open space"
							" along the building's frontage.\n")

			print "\n"

			width = float(width)

			if width < 20:
				print "This width must be at least 20 feet. Let's try for a building area increase again.\n"

				print "\n"

				building_area_increase(variables)

			if 20 <= width <= 30:
				print "Okay, your width is %.2f.\n" % width

				print "\n"

			if 30 < width:
				width = 30
				print ("The maximum width we can use for the calculation is 30 feet, so that's what"
						" we'll use here.\n")

				print "\n"


		if width_consistent == "no":
			width = raw_input("Please enter the WEIGHTED AVERAGE width of the qualified public way/open space"
							" along the building's frontage. Use a width of 30 for any portion of the frontage"
							" whose width is greater than 30 feet.\n")

			print "\n"

			width = float(width)

			if width < 20:
				print ("That can't be right... all widths along the frontage must be at least 20 feet."
						" Let's try for a building area increase again.\n")

				print "\n"

				building_area_increase(variables)

			if 20 <= width <= 30:
				print "Okay, your width is %s.\n" % width

				print "\n"

			if 30 < width:
				print ("That can't be right...you should use a width of 30 for any portion of the frontage"
						" whose width is greater than 30 feet. Let's try for a building area increase again.\n")

				print "\n"

				building_area_increase(variables)



		frontage_area_increase = ((frontage/perimeter) - min_frontage_percentage) * (width/30)


		frontage_increase_amount = (variables["max_area"] * frontage_area_increase)

		print ("Great. The frontage calculation increased your allowable building"
				" area by %.2f square feet.\n") % frontage_increase_amount

		print "\n"





	# Building Area increase from sprinklers


	print "Next, we'll look at sprinklers.\n"

	print "\n"

	if variables["has_sprinkler"] == "no":
		sprinkler_increase_amount = 0
		print ("Your building isn't equipped throughout with an approved sprinkler system, so you won't get"
				"a building area increase from sprinklers.\n")

		print "\n"

	elif variables["has_sprinkler"] == "yes":
		if variables["group"] == "h1":
			sprinkler_increase_amount = 0
			print ("Your building has an H-1 occupancy. Buildings with H-1 occupancies"
					" don't get allowable building area increases from sprinklers.\n")

			print "\n"

		# 506.3 exception 2 for H-2 and H-3 occupancies. figure out and add this condition

		if variables["sprinkler_for_fire_resistance_rating"] == "yes":
			sprinkler_increase_amount = 0
			print ("You're using the sprinkler system to substitute for 1-hour rated construction, so "
					"you cannot use it to increase your allowable building area.\n")

			print "\n"


		else: 
			if variables["actual_stories"] < 2:
				sprinkler_area_increase = 3
			
			elif variables["actual_stories"] >= 2:
				sprinkler_area_increase = 2

			sprinkler_increase_amount = (variables["max_area"] * sprinkler_area_increase)

			print ("Great, your sprinkler system qualifies you for a building area increase."
					"Based on the information you've already entered, the sprinkler calculation increased"
					" your allowable building area by %s.\n") % sprinkler_increase_amount

			print "\n"





	# combined calculation

	initial_area_value = variables["max_area"]

	variables["max_area"] = variables["max_area"] + frontage_increase_amount + sprinkler_increase_amount

	if initial_area_value == variables["max_area"]:
		print ("You didn't qualify for either the sprinker or the frontage increase to your building area."
				"Your allowable building area remains %s square feet.\n") % variables["max_area"]

		print "\n"


	elif initial_area_value < variables["max_area"]:
		print ("Okay, based on the frontage and sprinkler calculations,"
				" your, allowable building area increased to %s square feet.\n") % variables["max_area"]

		print "\n"


	return variables
				


























