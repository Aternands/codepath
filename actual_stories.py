


def actual_stories(variables):

	variables["actual_stories"] = raw_input('We figured out that the allowable number of stories for your building is ' + str(variables["max_stories"]) + 
								'. Now enter the actual number of stories above the grade plane.\n') 

	print "\n"

	variables["actual_stories"] = int(variables["actual_stories"])


	if variables["actual_stories"] > variables["max_stories"]:
		print "You chose a number of stories that's larger than the allowable number. Let's try again.\n"
		return actual_stories(variables)

	else:
		print "Okay, your building has %s stories above the grade plane.\n" % variables["actual_stories"]
		return variables








