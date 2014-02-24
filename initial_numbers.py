

def initial_numbers(ha_matrix, variables):

	#add code to deal with unusual situations in section 503 and 504.1

	#CODE QUESTION: what about min areas for sprinkler systems in section 903...........add these

	

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
		return initial_numbers(ha_matrix, variables)
	

	variables["cons_type"] = raw_input('What is your construction type? \n\
		Your choices are: ia, ib, iia, iib, iiia, iiib, iv, va, vb\n'
		'\n')

	print "\n"

	valid_cons_types = ["ia", "ib", "iia", "iib", "iiia", "iiib", "iv", "va", "vb"]

	if variables["cons_type"] not in valid_cons_types:
		print ("You didn't chose a valid construction type. Please select a new occupancy group and construction type.\n"
				'\n')
		return initial_numbers(ha_matrix, variables)

	table_entry = str(variables["group"] + "_" + variables["cons_type"])

	a = ha_matrix[table_entry]


	if "np" in a:
		print "You aren't allowed to use that construction type with that occupancy. Please choose a different combination.\n"
		
		return initial_numbers(ha_matrix, variables)

	

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

		