##################################
## Tuples, Sets, and Booleans ####
##################################


# Tuple is a collection which is ordered and immutable.
# Tuples represent things that shouldn't be changed, 
# such as days of the week, or dates on a calendar.


############################
#### Constructing Tuples ###
############################
#
# The construction of a tuples use () with elements separated by commas. For example:

# Can create a tuple with mixed types
t = (1,2,3)

# Check len just like a list
len(t)

# Can also mix object types
t = ('one',2)

# Show
t

# Use indexing just like we did in lists
t[0]

# Slicing just like a list
t[-1]

############################
### Basic Tuple Methods ####
############################

# Tuples have built-in methods, but not as many as lists do.

# Use .index to enter a value and return the index
t.index('one')

# Use .count to count the number of times a value appears
t.count('one')

####################
### Immutability ###
####################

# Tuples are immutable.

t[0]= 'change' #results in error

# Because of this immutability, tuples can't grow.
# Once a tuple is made we can not add to it.

t.append('nope') #results in error


########################################################
########################################################
############## SETS AND BOOLEANS #######################
########################################################
########################################################
#
# 
#
############
### Sets ###
############

# Sets are an unordered collection of *unique* elements. We can construct them
# by using the set() function. 

x = set()

# We add to sets with the add() method
x.add(1)

#Show
print(x)


# We know that a set has only unique entries. So what happens when we try to add
# something that is already in a set?

# Add a different element
x.add(2)

#Show
print(x)

# Try to add the same element
x.add(1)

#Show
print(x)


# Notice how it won't place another 1 there. That's because a set is only
# concerned with unique elements! We can cast a list with multiple repeat
# elements to a set to get the unique elements. For example:

# Create a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
set(l)

##########################
######## Booleans ########
##########################
# Python comes with Booleans (with predefined True and False displays that are
# basically just the integers 1 and 0). It also has a placeholder object called
# None. 

# Set object to be a boolean
a = True

#Show
a

# We can also use comparison operators to create booleans. We will go over all
# the comparison operators later on in the course.

# Output is boolean
1 > 2


# We can use None as a placeholder for an object that we don't want to reassign yet:

# None placeholder
b = None
