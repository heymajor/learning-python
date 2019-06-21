days_since_release = 16
original_price = 60
greatest_hits = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a conditional that determines the price of a
#newly-released game, movie, or album based on the time since
#it was released.
#
#Assume that a new release loses $2 off its price for every
#full week since it was released. So, two full weeks (14 days)
#after a $60 game is released, it will cost $56.
#
#However, if the release is considered a "greatest hit", it
#loses value half as fast: after two weeks, it will be $58
#instead of $56.
#
#No release will ever fall to below $20, however, no matter
#how fast it loses value or whether it's a greatest hit.
#
#Add some code below to print the current price of the release.
#For example, with the values above, it would print $58.


#Add your code here! Make sure to print the dollar sign, too.

if greatest_hits == True:
    loss = int(days_since_release / 7)
else:
    loss = 2 * int(days_since_release / 7)

original_price -= loss

if original_price < 20:
    original_price = 20

print('$' + str(original_price))





