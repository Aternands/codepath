from code_table import ha_matrix


# Initial values of variables

global group
group = "undefined"

global cons_type
cons_type = "undefined"

#---------------------------------------

global max_height
max_height = "undefined"

global max_stories
max_stories = "undefined"

global max_area
max_area = "undefined"

#---------------------------------------

global actual_height
actual_height = "undefined"

global actual_stories
actual_stories = "undefined"

global actual_area
actual_area = "undefined"

#---------------------------------------

global has_sprinkler
has_sprinkler = "undefined"

global sprinkler_for_fire_resistance_rating
sprinkler_for_fire_resistance_rating = "undefined"





#QUESTION What is best way to deal with variables going in and out of specific functions....global?....local?

#QUESTION should ha_matrix dictionary keys and values be strings or something else?

def initial_numbers(ha_matrix):

	global group

	global cons_type 

	global max_height

	global max_stories

	global max_area

	group = raw_input('What is your occupancy group? Your choices are: \n\
		a1, a2, a3, a4, a5, b, e, f1, f2, h1, h2, h3, h4, h5,\n\
		i1, i2, i3, i4, m, r1, r2, r3, r4, s1, s2, u\n'
		'\n')  

	print "\n"

	valid_groups = ["a1", "a2", "a3", "a4", "a5", "b", "e", "f1", "f2", "h1", "h2", "h3", "h4", "h5",
						"i1", "i2", "i3", "i4", "m", "r1", "r2", "r3", "r4", "s1", "s2", "u"]

	if group not in valid_groups:
		print ("You didn't chose a valid occupancy group. Please select a new occupancy group and construction type.\n"
				"\n")
		initial_numbers(ha_matrix)

	

	cons_type = raw_input('What is your construction type? \n\
		Your choices are: ia, ib, iia, iib, iiia, iiib, iv, va, vb\n'
		'\n')

	print "\n"

	valid_cons_types = ["ia", "ib", "iia", "iib", "iiia", "iiib", "iv", "va", "vb"]

	if cons_type not in valid_cons_types:
		print ("You didn't chose a valid construction type. Please select a new occupancy group and construction type.\n"
				'\n')
		initial_numbers(ha_matrix)

	table_entry = str(group + "_" + cons_type)

	a = ha_matrix[table_entry]


	if "np" in a:
		print "You aren't allowed to use that construction type with that occupancy. Please choose a different combination.\n"
		initial_numbers(ha_matrix)

	

	else:  

		if a[0] == "unlimited":
			max_height = "unlimited"

		else:
			max_height = int(a[0])                        

		

		if a[1] == "unlimited":
			max_stories = "unlimited"

		else:
			max_stories = int(a[1])  


		

		if a[2] == "unlimited":
			max_area = "unlimited"

		else:
			max_area = int(a[2])    



		print ("Okay, we've determined some initial building limitations based on what you've entered.\n"
				"\n"
				"Your building's maximum height is %s feet.\n"
				"\n"
				"Your building's maximum number of stories is %s stories.\n"
				"\n"
				"Your building's maximum area per story is %s.\n"
				"\n") % (max_height, max_stories, max_area)

		return group, cons_type, max_height, max_stories, max_area


		







initial_numbers(ha_matrix)





def sprinkler_height_story_increase():

	global group

	global cons_type

	global max_height

	global max_stories

	global has_sprinkler

	global sprinkler_for_fire_resistance_rating



	has_sprinkler = raw_input('Is your building equipped throughout with an approved sprinkler system? Enter yes or no.\n')

	print "\n"   

	valid_yes_no = ["yes", "no"]

	if has_sprinkler not in valid_yes_no:
		print "You didn't enter yes or no. Let's try for a sprinkler increase again.\n"
		sprinkler_height_story_increase()

	if has_sprinkler == "no":
		print "Okay, your building numbers won't get a sprinkler system increase.\n"
		return max_height, max_stories




	# 504.2 Exception 1

	exception_one_list = [ "iib", "iiia", "iiib", "iv", "va", "ba"]

	if has_sprinkler == "yes" and group == "i2" and cons_type in exception_one_list:
		exceptions = "yes"
		print "Unfortunately, you can't get a sprinkler system increase with an I-2 occupancy and a %s construction type.\n" % cons_type
		return max_height, max_stories

	# 504.2 Exception 2

	exception_two_list = [ "h1", "h2", "h3", "h5"]

	if has_sprinkler == "yes" and group in exception_two_list:
		exceptions = "yes"
		print "Unfortunately, you can't get a sprinker system increase with a %s occupancy.\n" % group
		return max_height, max_stories

	else:
		exceptions = "no"






	if has_sprinkler == "yes" and exceptions == "no":

		# 504.2 Exception 3

		sprinkler_for_fire_resistance_rating = raw_input('Are you using the sprinkler system to substitute for 1-hour rated construction? '
		'If so, you cannot use it to increase your allowable numbers. Enter yes or no.\n') #table 601 note d

		print "\n"

		if sprinkler_for_fire_resistance_rating not in valid_yes_no:
			print "You didn't enter yes or no. Let's try for a sprinkler increase again.\n"
			sprinkler_height_story_increase()

		if sprinkler_for_fire_resistance_rating == "yes":
			print "Okay, your allowable numbers won't get a sprinkler system increase.\n"
			return max_height, max_stories




		elif sprinkler_for_fire_resistance_rating == "no":

			residential_occ_list = ["r1", "r2", "r3", "r4"]

			if group in residential_occ_list: 

				#CODE QUESTION!!!! Can r occupancies exceed 60 feet....table 503 says they can in some construction types... 
				#but 504.2 says no. I am assuming no in lines below.

				if max_height >= 60:
					max_height = 60
					print "You don't get a sprinkler system height increase, because R occupancies are limited to 60 foot building heights.\n"

				elif max_height < 60 and max_height > 40:
					max_height = 60
					print "Great. You got a sprinkler system height increase. Now your building's maximum height is %s.\n" % max_height

				elif max_height < 40:
					max_height += 20
					print "Great. You got a sprinkler system height increase. Now your building's maximum height is %s.\n" % max_height





				if max_stories >= 4:
					max_stories = 4
					print "You don't get a sprinkler system story increase, because R occupancies are limited to 4 stories.\n"
					


				elif max_stories < 4:
					max_stories += 1
					print "You got a sprinkler system story increase. Now your building's maximum number of stories is %s.\n" % max_stories

				return max_height, max_stories



			else:

				max_height += 20

				max_stories += 1  

				print ("Great. You got a sprinkler system height and story increase. Now your building's maximum height is "
						 "%s feet, and your building's maximum number of stories is %s.\n") % (max_height, max_stories)

				return max_height, max_stories






if all(x == "unlimited" for x in (max_height, max_stories, max_area)):
	print ("Based on the occupancy group and construction type you chose, your building's height, number of stories," 
			"and area are all unlimited, so we don't need to do any more calculations to improve these numbers.\n")

else:
	print ("Now we'll try to improve these numbers. First, let's see if you can get an allowable building height"
			" and story increase due to a sprinkler system.\n")

	sprinkler_height_story_increase()


# there are some minor things affecting allowable building height, stories, and area in ch. 4- need to add these
# add a print statement about mezzanines





def actual_height():

	
	global group

	global cons_type

	global max_height

	global max_stories

	global max_area

	global actual_height

	global actual_area

	global actual_stories

	global has_sprinkler

	global sprinkler_for_fire_resistance_rating




	actual_height = raw_input('We figured out that your buildings maximum allowable height is ' + str(max_height) + 
								' feet. Now enter the actual height.\n')#% max_height 

	print "\n"

	actual_height = int(actual_height)


	# if isinstance(actual_height, int) == False:
	# 	print "You didn't enter your building's height in a valid format. Let's try again."
	# 	actual_height()

	if actual_height > max_height:
		print "You chose a height that's higher than the allowable height. Let's try again.\n"
		actual_height()

	else:
		print "Okay, your building's height is %s feet.\n" % actual_height
		return actual_height






def actual_stories():

	
	global group

	global cons_type

	global max_height

	global max_stories

	global max_area

	global actual_height

	global actual_area

	global actual_stories

	global has_sprinkler

	global sprinkler_for_fire_resistance_rating




	actual_stories = raw_input('We figured out that the allowable number of stories for your building is ' + str(max_stories) + 
								'. Now enter the actual number of stories above the grade plane.\n') 

	print "\n"

	actual_stories = int(actual_stories)


	if actual_height > max_height:
		print "You chose a number of stories that's larger than the allowable number. Let's try again.\n"
		actual_stories()

	else:
		print "Okay, your building has %s stories above the grade plane.\n" % actual_stories
		return actual_stories




actual_height()

actual_stories()







def building_area_increase():

	global group

	global cons_type

	global max_height

	global max_stories

	global max_area

	global actual_height

	global actual_area

	global actual_stories

	global has_sprinkler

	global sprinkler_for_fire_resistance_rating


	print "First, we'll look at frontage....when the code for this part is written....\n"

	#add frontage code here

	frontage_area_increase = 0








	print "Next, we'll look at sprinklers.\n"

	if has_sprinkler == "no":
		sprinkler_area_increase = 0
		print ("Your building isn't equipped throughout with an approved sprinkler system, so you won't get"
				"a building area increase from sprinklers.\n")

	elif has_sprinkler == "yes":
		if group == "h1":
			sprinkler_area_increase = 0
			print ("Your building has an H-1 occupancy. Buildings with H-1 occupancies"
					" don't get allowable building area increases from sprinklers.\n")

		# 506.3 exception 2 for H-2 and H-3 occupancies. figure out and add this condition

		if sprinkler_for_fire_resistance_rating == "yes":
			sprinkler_area_increase = 0
			print ("You're using the sprinkler system to substitute for 1-hour rated construction, so "
					"you cannot use it to increase your allowable building area.\n")


		else: 
			if actual_stories < 2:
				sprinkler_area_increase = 3
			
			elif actual_stories >= 2:
				sprinkler_area_increase = 2

			print "Your sprinkler system qualifies you for a building area increase.\n"

	initial_area_value = max_area

	max_area = max_area + (max_area * frontage_area_increase) + (max_area * sprinkler_area_increase)

	if initial_area_value == max_area:
		print ("You didn't qualify for sprinker or frontage increases to your building area."
				"Your allowable building area remains %s square feet.\n") % max_area


	elif initial_area_value < max_area:
		print "Great. Your allowable building area increased to %s square feet.\n" % max_area


	return max_area
				







			

if all(x == "unlimited" for x in (max_height, max_stories, max_area)):
	pass

else:
	print ("Next, let's see if you can increase your allowable building area. We'll check for a sprinkler increase "
			"and a frontage increase.\n")
	building_area_increase()



















