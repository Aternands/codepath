from code_table import ha_matrix
from initial_numbers import initial_numbers
from sprinkler import sprinkler
from sprinkler_height_increase import sprinkler_height_increase
from sprinkler_story_increase import sprinkler_story_increase
from actual_height import actual_height
from actual_stories import actual_stories
from building_area_increase import building_area_increase
from total_building_area import total_building_area
from results import results



# variable dictionary with initial values

variables = {

"group": None, 

"cons_type": None,

#---------------------------------------

"max_height": None,

"max_stories": None,

"max_area": None,  #max area per floor

"max_area_total": None, #max area of building

#---------------------------------------

"actual_height": None,

"actual_stories": None,

"actual_area": None,

"actual_area_total": None,

#---------------------------------------

"has_sprinkler": None,

"sprinkler_for_fire_resistance_rating": None,

}



# FUTURE CODE: section that asks whether building is separated into multiple separated areas
# 				that are considered separate buildings. Evaluated these one by one and then
#				show total combined numbers.



# add new variable and print statement about applicable code (2009 ibc model code for now)


initial_numbers(ha_matrix, variables)


print "Sprinkler systems can change many of your building's code limits. Let's check on this before moving forward.\n"

sprinkler(variables)


if all(x == "unlimited" for x in (variables["max_height"], variables["max_stories"], variables["max_area"])):
	print ("Based on the occupancy group and construction type you chose, your building's height, number of stories," 
			"and area are all unlimited, so we don't need to do any more calculations to improve these numbers.\n")

else:

	print "In the next step, we'll look at ways to improve your initial numbers.\n"


	if variables["max_height"] == "unlimited":
		print ("Based on the occupancy group and construction type you chose, your building's allowable height is already"
			" unlimited, so we don't need to do any more calculations to try increasing it.\n")

	elif variables["max_height"] != "unlimited":
		print "First, let's see if you can get an allowable building height increase due to a sprinkler system.\n"
		sprinkler_height_increase(variables)


	if variables["max_stories"] == "unlimited":
		print ("Based on the occupancy group and construction type you chose, your building's allowable number of stories"
			" is already unlimited, so we don't need to do any more calculations to try increasing it.\n")

	elif variables["max_stories"] != "unlimited":
		print "Let's see if you can get an allowable stories increase due to a sprinkler system.\n"
		sprinkler_story_increase(variables)


# there are some minor things affecting allowable building height, stories, and area in ch. 4- need to add these
# add a print statement about mezzanines



actual_height(variables)

actual_stories(variables)


			

if all(x == "unlimited" for x in (variables["max_height"], variables["max_stories"], variables["max_area"])):
	pass


else:

	if variables["max_area"] == "unlimited":
			print ("Based on the occupancy group and construction type you chose, your building's allowable area per story"
				" is already unlimited, so we don't need to do any more calculations to try increasing it.\n")

	elif variables["max_area"] != "unlimited":
			print "Let's see if you can increase your building's allowable area per story.\n"
			building_area_increase(variables)




total_building_area(variables)


results(variables)

print "Your building's code analysis is complete. You can view your building's data in results.txt."













