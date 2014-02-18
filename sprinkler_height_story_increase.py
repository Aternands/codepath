



def sprinkler_height_story_increase(variables):



	variables["has_sprinkler"] = raw_input('Is your building equipped throughout with an approved sprinkler system? Enter yes or no.\n')

	print "\n"   

	valid_yes_no = ["yes", "no"]

	if variables["has_sprinkler"] not in valid_yes_no:
		print "You didn't enter yes or no. Let's try for a sprinkler increase again.\n"
		sprinkler_height_story_increase(variables)

	if variables["has_sprinkler"] == "no":
		print "Okay, your building numbers won't get a sprinkler system increase.\n"
		return variables




	# 504.2 Exception 1

	exception_one_list = [ "iib", "iiia", "iiib", "iv", "va", "ba"]

	if variables["has_sprinkler"] == "yes" and variables["group"] == "i2" and variables["cons_type"] in exception_one_list:
		print "Unfortunately, you can't get a sprinkler system increase with an I-2 occupancy and a %s construction type.\n" % variables["cons_type"]
		return variables

	# 504.2 Exception 2

	exception_two_list = [ "h1", "h2", "h3", "h5"]

	if variables["cons_type"] == "yes" and variables["group"] in exception_two_list:
		print "Unfortunately, you can't get a sprinker system increase with a %s occupancy.\n" % variables["group"]
		return variables

	else:
		variables["sprinkler_for_fire_resistance_rating"] = raw_input('Are you using the sprinkler system to substitute '
		'for 1-hour rated construction? If so, you cannot use it to increase your allowable numbers. Enter yes or no.\n') #table 601 note d

		print "\n"

		if variables["sprinkler_for_fire_resistance_rating"] not in valid_yes_no:
			print "You didn't enter yes or no. Let's try for a sprinkler increase again.\n"
			sprinkler_height_story_increase(variables)

		if variables["sprinkler_for_fire_resistance_rating"] == "yes":
			print "Okay, your allowable numbers won't get a sprinkler system increase.\n"
			return variables




		elif variables["sprinkler_for_fire_resistance_rating"] == "no":

			residential_occ_list = ["r1", "r2", "r3", "r4"]

			if variables["group"] in residential_occ_list: 

				#CODE QUESTION!!!! Can r occupancies exceed 60 feet....table 503 says they can in some construction types... 
				#but 504.2 says no. I am assuming no in lines below.

				if variables["max_height"] >= 60:
					variables["max_height"] = 60
					print "You don't get a sprinkler system height increase, because R occupancies are limited to 60 foot building heights.\n"

				elif variables["max_height"] < 60 and variables["max_height"] > 40:
					variables["max_height"] = 60
					print "Great. You got a sprinkler system height increase. Now your building's maximum height is %s.\n" % max_height

				elif variables["max_height"] < 40:
					variables["max_height"] += 20
					print "Great. You got a sprinkler system height increase. Now your building's maximum height is %s.\n" % max_height





				if variables["max_stories"] >= 4:
					variables["max_stories"] = 4
					print "You don't get a sprinkler system story increase, because R occupancies are limited to 4 stories.\n"
					


				elif variables["max_stories"] < 4:
					variables["max_stories"] += 1
					print "You got a sprinkler system story increase. Now your building's maximum number of stories is %s.\n" % max_stories

				return variables



			else:

				variables["max_height"] += 20

				variables["max_stories"] += 1  

				print ("Great. You got a sprinkler system height and story increase. Now your building's maximum height is "
						 "%s feet, and your building's maximum number of stories is %s.\n") % (variables["max_height"], variables["max_stories"])

				return variables
























