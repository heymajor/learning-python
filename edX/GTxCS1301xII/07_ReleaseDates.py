#Write a function called valid_release_date. The function
#should have two parameters: a date and a string. The
#string will represent a type of media release: "Game",
#"Movie", "Album", "Show", and "Play".
#
#valid_release_date should check to see if the date is
#a valid date to release that type of media according to
#the following rules:
#
# - Albums should be released on Mondays.
# - Games should be released on Tuesdays.
# - Shows should be released on Wednesdays or Sundays.
# - Movies should be released on Fridays.
# - Plays should be released on Saturdays.
#
#valid_release_date should return True if the date is
#valid, False if it's not.
#
#The date will be an instance of Python's date class. If
#you have an instance of date called a_date, you can
#access an integer representing the day of the week with
#a_date.weekday(). a_date.weekday() will return 0 if the
#day is Monday, 1 if it's Tuesday, 2 if it's Wednesday,
#up to 6 if it's Sunday.
#
#If the type of release is not one of these strings,
#the release date is automatically invalid, so return
#False.

from datetime import date

#Write your function here!

def valid_release_date( a_date , media ):

    if media == "Album":
        if a_date.weekday() == 0:
            return True
        else:
            return False

    elif media == "Game":
        if a_date.weekday() == 1:
            return True
        else:
            return False
        
    elif media == "Show":
        if a_date.weekday() == 2 or a_date.weekday() == 6:
            return True
        else:
            return False
        
    elif media == "Movie":
        if a_date.weekday() == 4:
            return True
        else:
            return False
        
    elif media == "Play":
        if a_date.weekday() == 5:
            return True
        else:
            return False

    else:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, False, each on their own line.
print(valid_release_date(date(2018, 7, 11), "Show"))
print(valid_release_date(date(2018, 7, 11), "Movie"))
print(valid_release_date(date(2018, 7, 11), "Pancake"))




