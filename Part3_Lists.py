# # Lists
#
# Lists can be thought of the most general version of a "sequence" in Python. 
# Lists in Python tend to be more flexible than arrays in other languages for a
# two good reasons: they have no fixed size (meaning we don't have to specify
# how big a list will be), and they have no fixed type constraint 
#


# Assign a list to an variable named my_list
my_list = [1,2,3]


# A list with different object types
my_list = ['A string',23,100.232,'o']


# Just like strings, the len() function will tell you how
# many items are in the sequence of the list.
len(my_list)


##############################
#### Indexing and Slicing ####
##############################

# Indexing and slicing works just like in strings. 

my_list = ['one','two','three',4,5]

# Grab element at index 0
my_list[0]

# Grab index 1 and everything past it
my_list[1:]

# Grab everything UP TO index 3
my_list[:3]

# We can also use + to concatenate lists

my_list = my_list + ['add new item permanently']

print(my_list) #['one', 'two', 'three', 4, 5, 'add new item permanently']

# We can also use the * for a duplication method similar to strings:

# Make the list double
my_list * 2

# Again doubling not permanent
my_list


#############################
#### Basic List Methods #####
#############################

# Create a new list
listOne = [1,2,3]
listTwo = ['x',  'y', 'z']

# Use the .append() method to permanently add an item to the end of a list:

# Append

listOne.append(listTwo)
print( listOne) #[1, 2, 3, ['x', 'y', 'z']]


# Extend the lists

listThree = ["m", "n", "o" ]

listOne.extend(listThree)
print(listOne) #[1, 2, 3, ['x', 'y', 'z'], 'm', 'n', 'o']


# Use "pop" to "pop off" an item from the list. By default pop takes off the last
# index, but you can also specify which index to pop off. Let's see an example:

# Pop off the 0 indexed item
listOne.pop(0)

# Show
print(listOne) #[2, 3, ['x', 'y', 'z'], 'm', 'n', 'o']

# Assign the popped element, remember default popped index is -1
popped_item = listOne.pop()

print(popped_item)

# Show remaining list
print(listOne) #[2, 3, ['x', 'y', 'z'], 'm', 'n']


# It should also be noted that lists indexing will return an error if there is
# no element at that index. For example:
print(listOne[100])


# We can use the **sort** method and the **reverse** methods
# to also effect your lists:

new_list = ['a','e','x','b','c']

#Show
print(new_list)

# Use reverse to reverse order (this is permanent!)
new_list.reverse()

print(new_list)

# Use sort to sort the list (in this case alphabetical order,
# but for numbers it will go ascending)
new_list.sort()

print(new_list)


#######################
#### Nesting Lists ####
#######################
# A list inside a list.
#

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

# Show
print(matrix)


# Now we can again use indexing to grab elements, but now there are two levels
# for the index. The items in the matrix object, and then the items inside that list!

# Grab first item in matrix object
matrix[0]

# Grab first item of the first item in the matrix object
matrix[0][0]


###########################
### List Comprehensions ###
###########################

# Python has an advanced feature called list comprehensions. They allow for
# quick construction of lists. 

# Build a list comprehension by deconstructing a for loop within a []
# the for loop retrives each array in matrix one at a time and then we 
# retrive the element at the 0th index position to construct the new list
first_col = [row[0] for row in matrix]

print(first_col) #[1, 4, 7]