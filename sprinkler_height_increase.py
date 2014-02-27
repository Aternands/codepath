


def sprinkler_height_increase(variables):


	if variables["has_sprinkler"] == "no":
		print ("Your building doesn't have an approved sprinker system throughout, so"
				" your building numbers won't get a sprinkler system height increase.\n")
		return variables


	# 504.2 Exception 1

	exception_one_list = [ "iib", "iiia", "iiib", "iv", "va", "ba"]

	if variables["has_sprinkler"] == "yes" and variables["group"] == "i2" and variables["cons_type"] in exception_one_list:
		print "Unfortunately, you can't get a sprinkler system height increase with an I-2 occupancy and a %s construction type.\n" % variables["cons_type"]
		return variables

	# 504.2 Exception 2

	exception_two_list = [ "h1", "h2", "h3", "h5"]

	if variables["group"] in exception_two_list:
		print "Unfortunately, you can't get a sprinker system height increase with a %s occupancy.\n" % variables["group"]
		return variables

	# 504.2 Exception 3

	if variables["sprinkler_for_fire_resistance_rating"] == "yes":
		print ("Because you're using the sprinkler system to substitute for rated construction, you can't"
				" use it to increase your building's maximum height.\n")
		return variables



	else:
		residential_occ_list = ["r1", "r2", "r3", "r4"]

		if variables["group"] in residential_occ_list: 

			#CODE QUESTION!!!! Can r occupancies exceed 60 feet....table 503 says they can in some construction types... 
			#but 504.2 says no. I am assuming no in lines below.

			if variables["max_height"] >= 60:
				variables["max_height"] = 60
				print "You don't get a sprinkler system height increase, because R occupancies are limited to 60 foot building heights.\n"

			elif variables["max_height"] < 60 and variables["max_height"] > 40:
				variables["max_height"] = 60
				print "Great. You got a sprinkler system height increase. Now your building's maximum height is %i.\n" % variables["max_height"]

			elif variables["max_height"] < 40:
				variables["max_height"] += 20
				print "Great. You got a sprinkler system height increase. Now your building's maximum height is %i.\n" % variables["max_height"]

			return variables



		else:

			variables["max_height"] += 20

			print ("Great. You got a sprinkler system height increase. Now your building's maximum height is "
					 "%i feet.\n") % variables["max_height"]

			return variables
























