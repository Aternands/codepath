from code_table import ha_matrix


# variable dictionary with initial values

variables = {

"group": None, 

"cons_type": None,

#---------------------------------------

"max_height": None,

"max_stories": None,

"max_area": None,

#---------------------------------------

"actual_height": None,

"actual_stories": None,

"actual_area": None,

#---------------------------------------

"has_sprinkler": None,

"sprinkler_for_fire_resistance_rating": None,

}








#QUESTION should ha_matrix dictionary keys and values be strings or something else?

def initial_numbers(ha_matrix, variables):

	

	variables["group"] = raw_input('What is your occupancy group? Your choices are: \n\
		a1, a2, a3, a4, a5, b, e, f1, f2, h1, h2, h3, h4, h5,\n\
		i1, i2, i3, i4, m, r1, r2, r3, r4, s1, s2, u\n'
		'\n')  

	print "\n"

	valid_groups = ["a1", "a2", "a3", "a4", "a5", "b", "e", "f1", "f2", "h1", "h2", "h3", "h4", "h5",
						"i1", "i2", "i3", "i4", "m", "r1", "r2", "r3", "r4", "s1", "s2", "u"]

	if variables["group"] not in valid_groups:
		print ("You didn't chose a valid occupancy group. Please select a new occupancy group and construction type.\n"
				"\n")
		initial_numbers(ha_matrix, variables)
	

	variables["cons_type"] = raw_input('What is your construction type? \n\
		Your choices are: ia, ib, iia, iib, iiia, iiib, iv, va, vb\n'
		'\n')

	print "\n"

	valid_cons_types = ["ia", "ib", "iia", "iib", "iiia", "iiib", "iv", "va", "vb"]

	if variables["cons_type"] not in valid_cons_types:
		print ("You didn't chose a valid construction type. Please select a new occupancy group and construction type.\n"
				'\n')
		initial_numbers(ha_matrix, variables)

	table_entry = str(variables["group"] + "_" + variables["cons_type"])

	a = ha_matrix[table_entry]


	if "np" in a:
		print "You aren't allowed to use that construction type with that occupancy. Please choose a different combination.\n"
		initial_numbers(ha_matrix, variables)

	

	else:  

		if a[0] == "unlimited":
			variables["max_height"] = "unlimited"

		else:
			variables["max_height"] = int(a[0])                        

		

		if a[1] == "unlimited":
			variables["max_stories"] = "unlimited"

		else:
			variables["max_stories"] = int(a[1])  


		

		if a[2] == "unlimited":
			variables["max_area"] = "unlimited"

		else:
			variables["max_area"] = int(a[2])    



		print ("Okay, we've determined some initial building limitations based on what you've entered.\n"
				"\n"
				"Your building's maximum height is %s feet.\n"
				"\n"
				"Your building's maximum number of stories is %s stories.\n"
				"\n"
				"Your building's maximum area per story is %s.\n"
				"\n") % (variables["max_height"], variables["max_stories"], variables["max_area"])

		return variables

		




initial_numbers(ha_matrix, variables)





def sprinkler_height_story_increase(variables):



	variables["has_sprinkler"] = raw_input('Is your building equipped throughout with an approved sprinkler system? Enter yes or no.\n')

	print "\n"   

	valid_yes_no = ["yes", "no"]

	if variables["has_sprinkler"] not in valid_yes_no:
		print "You didn't enter yes or no. Let's try for a sprinkler increase again.\n"
		sprinkler_height_story_increase()

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
		variables["sprinkler_for_fire_resistance_rating"] = raw_input('Are you using the sprinkler system to substitute'
		'for 1-hour rated construction? If so, you cannot use it to increase your allowable numbers. Enter yes or no.\n') #table 601 note d

		print "\n"

		if variables["sprinkler_for_fire_resistance_rating"] not in valid_yes_no:
			print "You didn't enter yes or no. Let's try for a sprinkler increase again.\n"
			sprinkler_height_story_increase()

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






if all(x == "unlimited" for x in (variables["max_height"], variables["max_stories"], variables["max_area"])):
	print ("Based on the occupancy group and construction type you chose, your building's height, number of stories," 
			"and area are all unlimited, so we don't need to do any more calculations to improve these numbers.\n")

else:
	print ("Now we'll try to improve these numbers. First, let's see if you can get an allowable building height"
			" and story increase due to a sprinkler system.\n")

	sprinkler_height_story_increase(variables)


# there are some minor things affecting allowable building height, stories, and area in ch. 4- need to add these
# add a print statement about mezzanines





def actual_height(variables):

	variables["actual_height"] = raw_input('We figured out that your buildings maximum allowable height is ' + str(variables["max_height"]) + 
								' feet. Now enter the actual height.\n')#% max_height 

	print "\n"

	variables["actual_height"]  = int(variables["actual_height"] )

	if variables["actual_height"] > variables["max_height"]:
		print "You chose a height that's higher than the allowable height. Let's try again.\n"
		actual_height(variables)

	else:
		print "Okay, your building's height is %s feet.\n" % variables["actual_height"]
		return variables






def actual_stories(variables):

	variables["actual_stories"] = raw_input('We figured out that the allowable number of stories for your building is ' + str(variables["max_stories"]) + 
								'. Now enter the actual number of stories above the grade plane.\n') 

	print "\n"

	variables["actual_stories"] = int(variables["actual_stories"])


	if variables["actual_stories"] > variables["max_stories"]:
		print "You chose a number of stories that's larger than the allowable number. Let's try again.\n"
		actual_stories(variables)

	else:
		print "Okay, your building has %s stories above the grade plane.\n" % variables["actual_stories"]
		return variables




actual_height(variables)

actual_stories(variables)







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
				







			

if all(x == "unlimited" for x in (variables["max_height"], variables["max_stories"], variables["max_area"])):
	pass

else:
	print ("Next, let's see if you can increase your allowable building area. We'll check for a sprinkler increase "
			"and a frontage increase.\n")
	building_area_increase(variables)



















