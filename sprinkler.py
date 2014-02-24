

def sprinkler(variables):


	variables["has_sprinkler"] = raw_input('Is your building equipped throughout with an approved sprinkler system? Enter yes or no.\n')

	print "\n"   

	valid_yes_no = ["yes", "no"]

	if variables["has_sprinkler"] not in valid_yes_no:
		print "You didn't enter yes or no. Let's try again.\n"
		return sprinkler(variables)

	elif variables["has_sprinkler"] == "no":
		print "Okay, your building does not have an approved sprinkler system throughout.\n"
		return variables

	elif variables["has_sprinkler"] == "yes":
		variables["sprinkler_for_fire_resistance_rating"] = raw_input('Are you using the sprinkler system to substitute '
		'for 1-hour rated construction? Enter yes or no.\n') #table 601 note d

		print "\n"

		if variables["sprinkler_for_fire_resistance_rating"] not in valid_yes_no:
			print "You didn't enter yes or no. Let's try again.\n"
			return sprinkler(variables)

		elif variables["sprinkler_for_fire_resistance_rating"] == "yes":
			print "Okay, we'll use the sprinkler system to substitute for 1-hour rated construction.\n"
			return variables

		elif variables["sprinkler_for_fire_resistance_rating"] == "no":
			print "Okay, we won't use the sprinkler system to substitute for 1-hour rated construction.\n"
			return variables

















