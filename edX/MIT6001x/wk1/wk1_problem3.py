s = 'abcbcd'

last_letter = ""
long_string = ""
current_string = ""

for current_letter in s:
    if current_letter >= last_letter:
        current_string += current_letter
    if len(current_string) > len(long_string):
            long_string = current_string
    else:
        current_string = current_letter
    last_letter = current_letter

print('Longest substring in alphabetical order is: ' + long_string)


https://www.google.com/search?ei=kMP5XK7mJ8uusAXnt6nYBw&q=python+find+alphabetic+subsstrings&oq=python+find+alphabetic+subsstrings&gs_l=psy-ab.3..0i22i30.111699.114993..115114...3.0..0.211.2132.0j15j1......0....1..gws-wiz.......0i71j0j33i160j33i299j0i8i13i30.rQxmpoj3Aug

https://codereview.stackexchange.com/questions/188033/longest-substring-in-alphabetical-order

https://docs.python.org/3/library/functions.html?highlight=alphabet#filter