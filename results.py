

def results(variables):

	translate = {

	"group": "Occupancy Group:", 

	"cons_type": "Construction Type:",

	#-------------------------------------

	"max_height": "Maximum Building Height:",

	"max_stories": "Maximum Number of Stories:",

	"max_area": "Maximum Area per Story:",  #max area per floor

	"max_area_total": "Maximum Area of Building:", #max area of building

	#---------------------------------------

	"actual_height": "Actual Height:",

	"actual_stories": "Actual Number of Stories:",

	"actual_area": "Actual Area of Largest Story:",

	"actual_area_total": "Actual Area of Building",

	#---------------------------------------

	"has_sprinkler": "Is Building Sprinklered (yes/no):",

	"sprinkler_for_fire_resistance_rating": "Is Sprinkler Used For Fire Rating Increase:",

	}


	fin = open("Results.txt", "w")

	fin.write("Here are the results of your building's code analysis:\n")

	fin.write("\n")

	fin.write("\n")
	
	fin.write("%s %s\n" % (translate["group"], variables["group"]))

	fin.write("\n")

	fin.write("%s %s\n" % (translate["cons_type"], variables["cons_type"]))

	fin.write("\n")
	
	fin.write("-----------------------------------------------\n")

	fin.write("\n")

	fin.write("%s %s\n" % (translate["has_sprinkler"], variables["has_sprinkler"]))

	fin.write("\n")
	
	fin.write("-----------------------------------------------\n")

	fin.write("\n")

	if variables["max_height"] == "unlimited":

		fin.write("%s unlimited\n" % translate["max_height"])

	elif variables["max_height"] != "unlimited":

		fin.write("%s %i feet\n" % (translate["max_height"], variables["max_height"]))

	fin.write("\n")

	fin.write("%s %.1f feet\n" % (translate["actual_height"], variables["actual_height"]))

	fin.write("\n")

	if variables["max_stories"] == "unlimited":

		fin.write("%s unlimited\n" % translate["max_stories"])

	elif variables["max_stories"] != "unlimited":
		
		fin.write("%s %i\n" % (translate["max_stories"], variables["actual_stories"]))

	fin.write("\n")

	fin.write("%s %i\n" % (translate["actual_stories"], variables["actual_stories"]))

	fin.write("\n")

	if variables["max_area"] == "unlimited":

		fin.write("%s unlimited\n" % translate["max_area"])

	elif variables["max_area"] != "unlimited":

		fin.write("%s %.1f square feet\n" % (translate["max_area"], variables["max_area"]))

	fin.write("\n")

	fin.write("%s %s square feet\n" % (translate["actual_area"], variables["actual_area"]))  # change to float when code for this is written

	fin.write("\n")

	if variables["max_area_total"] == "unlimited":

		fin.write("%s unlimited\n" % translate["max_area_total"])

	elif variables["max_area_total"] != "unlimited":

		fin.write("%s %.1f square feet\n" % (translate["max_area_total"], variables["max_area_total"]))

	fin.write("\n")

	fin.write("%s %s square feet\n" % (translate["actual_area_total"], variables["actual_area_total"]))  # change to float when code for this is written

	fin.write("\n")








	fin.close()


