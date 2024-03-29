#Imagine you're playing a game in which every action you
#take grants you some number of experience points. There is
#an item called a Lucky Egg that, when used, doubles the
#number of experience points you earn. The company behind
#the game also runs occasional events where they increase
#how many experience points you earn for each action by 50%,
#100%, or even 200%.
#
#Write a function called find_total_exp. find_total_exp
#should have one positional parameter, a base number of
#experience points. It should also have two keyword
#parameters: lucky_egg, whose default value is False, and
#event_multiplier, whose default value is 1.
#
#The function should return the number of experience
#points earned based on these two variables. The base number
#of experience points should always be multiplied by the
#event multiplier, and then doubled if lucky_egg is True.
#
#You should convert the final result from a float to an
#integer before returning it. This will automatically round
#down.


#Add your code here!

def find_total_exp( exp , lucky_egg = False , multiplier = 1):
    
    exp *= multiplier

    if lucky_egg == True:
        exp *= 2
    
    return int(exp)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#100
#200
#150
#300
print(find_total_exp(100))
print(find_total_exp(100, lucky_egg = True))
print(find_total_exp(100, multiplier = 1.5))
print(find_total_exp(100, lucky_egg = True, multiplier = 1.5))






