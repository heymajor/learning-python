# Paste your code into this box 
# s = 'azcbobobegghakl'
s = 'aopcapgcqocrswaxjyjqoafc'
letters = list(map(str,s))

vowels = ['a', 'e', 'i', 'o', 'u']
counter = 0

for letter in letters:
    for vowel in vowels:
        if vowel == letter:
            counter+=1
        else:
            pass
        
print("Number of vowels: " + str(counter))