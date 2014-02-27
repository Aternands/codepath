


def sprinkler_story_increase(variables):


	if variables["has_sprinkler"] == "no":
		print ("Your building doesn't have an approved sprinker system throughout, so"
				" your building numbers won't get a sprinkler system story increase.\n")
		return variables



	# 504.2 Exception 1

	exception_one_list = [ "iib", "iiia", "iiib", "iv", "va", "ba"]

	if variables["has_sprinkler"] == "yes" and variables["group"] == "i2" and variables["cons_type"] in exception_one_list:
		print "Unfortunately, you can't get a sprinkler system story increase with an I-2 occupancy and a %s construction type.\n" % variables["cons_type"]
		return variables

	# 504.2 Exception 2

	exception_two_list = [ "h1", "h2", "h3", "h5"]

	if variables["group"] in exception_two_list:
		print "Unfortunately, you can't get a sprinker system story increase with a %s occupancy.\n" % variables["group"]
		return variables

	if variables["sprinkler_for_fire_resistance_rating"] == "yes":
		print ("Because you're using the sprinkler system to substitute for rated construction, you can't"
				" use it to increase your building's maximum number of stories.\n")
		return variables


	else:

		residential_occ_list = ["r1", "r2", "r3", "r4"]

		if variables["group"] in residential_occ_list: 

			if variables["max_stories"] >= 4:
				variables["max_stories"] = 4
				print "You don't get a sprinkler system story increase, because R occupancies are limited to 4 stories.\n"
				

			elif variables["max_stories"] < 4:
				variables["max_stories"] += 1
				print "Great. You got a sprinkler system story increase. Now your building's maximum number of stories is %i.\n" % max_stories

			return variables



		else:

			variables["max_stories"] += 1  

			print ("Great. You got a sprinkler system story increase. Now your building's"
					" maximum number of stories is %i.\n") % variables["max_stories"]

			return variables
























