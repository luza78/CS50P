# My second solution. Probably the intended one!

word = input("Hey :\n").strip().replace(" ", "...")

print(word)


# My first solution

# Make str into a list of str
'''
word = input("Heyyy: \n").split()
'''

# Adds ... to all the words, except the last element
'''
for words in word[0:-1]:
    print(f"{words}...", end="")
print(word[-1])
'''