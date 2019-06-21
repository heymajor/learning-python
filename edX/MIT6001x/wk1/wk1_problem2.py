import re

bob = len(re.findall('(?=bob)', s))
print('Number of times bob occurs is: ' + str(bob))