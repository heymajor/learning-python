# Make a dictionary containing three major rivers and the country each river runs through.
river_dictionary = { 'river1' : 'country1', 'river2' : 'country2', 'river3': 'country3'}


# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river in river_dictionary:
	print(river.title() + " runs through " + river_dictionary[river].title())

# Use a loop to print the name of each river included in the dictionary.
for river in river_dictionary:
	print(river.title())


# Use a loop to print the name of each country included in the dictionary.

for country in river_dictionary:
	print(river_dictionary[country].title())


