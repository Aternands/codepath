from code_table import ha_matrix
from initial_numbers import initial_numbers
from sprinkler_height_story_increase import sprinkler_height_story_increase
from actual_height import actual_height
from actual_stories import actual_stories
from building_area_increase import building_area_increase



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



# FUTURE CODE: section that asks whether building is separated into multiple separated areas
# 				that are considered separate buildings. Evaluated these one by one and then
#				show total combined numbers.



# QUESTION should ha_matrix dictionary keys and values be strings or something else?
# QUESTION do i need .pyc files....can they go somewhere else






initial_numbers(ha_matrix, variables)




if all(x == "unlimited" for x in (variables["max_height"], variables["max_stories"], variables["max_area"])):
	print ("Based on the occupancy group and construction type you chose, your building's height, number of stories," 
			"and area are all unlimited, so we don't need to do any more calculations to improve these numbers.\n")

else:
	print ("Now we'll try to improve these numbers. First, let's see if you can get an allowable building height"
			" and story increase due to a sprinkler system.\n")

	sprinkler_height_story_increase(variables)


# there are some minor things affecting allowable building height, stories, and area in ch. 4- need to add these
# add a print statement about mezzanines




actual_height(variables)

actual_stories(variables)


			

if all(x == "unlimited" for x in (variables["max_height"], variables["max_stories"], variables["max_area"])):
	pass

else:
	print ("Next, let's see if you can increase your allowable building area. We'll check for a sprinkler increase "
			"and a frontage increase.\n")
	building_area_increase(variables)



















