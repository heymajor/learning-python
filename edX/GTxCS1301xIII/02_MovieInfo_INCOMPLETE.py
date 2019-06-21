#Write a function called write_movie_info. write_movie_info
#will take as input two parameters: a string and a
#dictionary.
#
#The string will represent the filename to which to write.
#
#The keys in the dictionary will be strings representing
#movie titles. The values in the dictionary will be lists
#of strings representing performers in the corresponding
#movie.
#
#write_movie_info should write the list of movies to the file
#given by the filename using the following format:
#
# Title: Actor 1, Actor 2, Actor 3, etc.
#
#The movies and the actor names should be sorted
#alphabetically.
#
#So, for this dictionary:
#
# {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
#  "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
#
#The file printed would look like this:
#
# Chocolat: Alfred Molina, Johnny Depp, Judi Dench, Juliette Binoche
# Skyfall: Daniel Craig, Javier Bardem, Judi Dench, Naomie Harris
#
# HINT: the keys() method of a Dictionary will return a list
# of the dictionary's keys. So, to get a sorted list of a_dict's
# keys, you could call key_list = a_dict.keys(), then call 
# key_list.sort().

# import os
# os.getcwd()

# Write your function here!

def write_movie_info( filename , movies ):

	movie_names = movies.keys()
	actors = movies.values()
	outputFile = open( filename , "w")

	for actor in actors:
		actor.sort()

	sorted_movie_names = dict()
	sorted_movie_names = sorted(movie_names)

	for movie_names, actor in movies.items():
		sorted_movie_names(movie_names) = actor


	for movie_names, actors in movies.items():
		outputFile.write(str(movie_names) + ": ")
		
		counter = 0

		for actor in actors:
			outputFile.write(str(actors))
			counter += 1
			if counter == len(actors):
				outputFile.write("\n")
				break
			else:
				outputFile.write(", ")
		print(str(movie_names) + ": " + str(actors))

	outputFile.close()
	# new = dict(zip( key_sort , items_sort ))
	# for i in movie_names:
	#	 x = i + ": "
	#	 outputFile.write(x)
	#	 # outputFile.write(", ".join(actor))
	#	 outputFile.write("\n")
		

		# counter = 0
		# while len(items) > counter:
		#	 print(items[counter], end = "")
		#	 counter += 1
		#	 if counter == len(items):
		#		 print("")
		#		 break
		#	 else:
		#		 print(", ", end = "")
			



	# outputFile.close()







#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movies = {"Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"], "Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], }
write_movie_info("Test.txt", movies)



