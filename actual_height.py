

def actual_height(variables):

	variables["actual_height"] = raw_input('We figured out that your buildings maximum allowable height is ' + str(variables["max_height"]) + 
								' feet. Now enter the actual height.\n') 

	print "\n"

	variables["actual_height"]  = int(variables["actual_height"] )

	if variables["actual_height"] > variables["max_height"]:
		print "You chose a height that's higher than the allowable height. Let's try again.\n"
		return actual_height(variables)

	else:
		print "Okay, your building's height is %s feet.\n" % variables["actual_height"]
		return variables










