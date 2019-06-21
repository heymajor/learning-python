#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.
#
#For example, in the dropdown in the top left you'll find a
#file named FindMedianInput.txt. There are 19 numbers in
#this file, so the median is the value at index 10 after
#sorting them: 16.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.


#Write your function here!

import os


def find_median( file ):

# Allows access to the file (was having issues opening file even thought it 
# was in the same folder)
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__ ))
    my_file = os.path.join(THIS_FOLDER, file )

# reads the file contents
    input_list = []
    inputFile = open( my_file , 'r' ) 
    # inputFile = open( file , 'r' ) 
    
# Creates list from file contents
    for i in inputFile:
        input_list.append(i)

# Replaces carriage return from list & sorts
    final_list = [x.replace('\n', '') for x in input_list]
    
    final_list = list(map(int,final_list))
    final_list.sort()
    

# Calculates the halfway point and rounds down if float
    half = int(len(final_list) / 2)

# Tests if list item is even
    if len(final_list) % 2 == 0:

# If length is even, average the 2 center numbers
        median_a = final_list[half]
        median_b = final_list[half - 1]

# Finds the average and returns the integer (removes floating point)
        avg = (median_a + median_b) / 2
        # avg = int(avg)
        return avg
    
    else:

# If length of the list is odd, return the center number
        return final_list[half]
        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16 42 53.0 25.0
print(find_median("FindMedianInput.txt"))
print(find_median("FindMedianInput1.txt"))
print(find_median("FindMedianInput2.txt"))
print(find_median("FindMedianInput3.txt"))


