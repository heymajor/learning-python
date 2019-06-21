letters = list(map(str, s))
const = 0
vowels = 'aeiou'

for letter in letters:
    if letter in vowels:
        const += 1

print('Number of times bob occurs is: ' + str(const))


