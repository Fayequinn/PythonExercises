# Question1
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

# cheese += 'Oke'

print(cheese)

# This has added each character of the string 'Oke' as seperate elements to the 'cheese' list
# You cannot append a string with +=; it's not the whole string that gets added to the list but
# each character in the string individually

# How it should be added...
cheese.append('Oke')
print(cheese)

# append can only be used for one item. To add two items using one command...

cheese.extend(['Edam','Comte'])
print(cheese)

# or...
cheese += ['Brie', 'Wensleydale']
print(cheese)
# we can use += because we are adding a list to a list

# Question2
tup='Hello'
print(len(tup))
# prints the length of the string 'tup'

tup = 'Hello',
print(len(tup))
# tup in a tuple with 1 element so the length of 'tup' is 1