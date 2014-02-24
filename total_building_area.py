	


def total_building_area(variables):

	print ("We've determined that the allowable building area PER STORY is %.2f." 
			" Now let's figure out the total allowable area for the building.\n") % variables["max_area"]

	print "\n"

	print ("We'll use some of the information you've already entered to determine this. Note that a single"
			" basement is not included in the total allowable building area, as long as its area"
			" does not exceed the allowable building area per story.\n")

	if variables["has_sprinkler"] == "no":

		if variables["actual_stories"] == 0:
			variables["max_area_total"] = 0
			print ("Your building consists of a basement with no stories above the grade plane."
					" Single basements aren't included in the total allowable building area, so"
					" your total allowable building area is %.1f square feet.\n") % variables["max_area_total"]

			#is the max_area_total supposed to be zero here?.....and what about buildings with more than one bsmnt

		if variables["actual_stories"] == 1:
			variables["max_area_total"] = variables["max_area"]
			print ("Your building has one story above the grade plane, so your total allowable building"
					" area is the same as your allowable building area per story. That means that"
					" your total allowable building area is %.1f square feet.\n") % variables["max_area_total"]


		if variables["actual_stories"] == 2:
			variables["max_area_total"] = variables["max_area"] * 2
			print ("Your building has two stories above the grade plane, so your total allowable building"
					" area is twice your allowable building area per story. That means that"
					" your total allowable building area is %.1f square feet.\n") % variables["max_area_total"]



		elif variables["actual_stories"] >= 3:
			variables["max_area_total"] = variables["max_area"] * 3
			print ("Your building has %i stories above the grade plane. For buildings with three or more"
					" stories above the grade plane, the total allowable building area is three times"
					" the allowable building area per story. That means that your total allowable building"
					" area is %.1f square feet.\n") % (variables["actual_stories"], variables["max_area_total"])


	elif variables["has_sprinkler"] == "yes":
		variables["max_area_total"] = variables["max_area"] * variables["actual_stories"]
		print ("Buildings equipped throughout with an approved sprinker system are allowed to"
					" have up to the maximum area per story on every story of the building."
					" Your building is sprinkled throughout and has %i stories above the grade plane."
					" That means that your total allowable building area is %.1f square feet.\n") % (variables["actual_stories"], variables["max_area_total"])


	#UNFINISHED

	#add code for 506.5 later...in 508

	return variables
				


























