##############################
###### Strings ###############
##############################


## Creating a String

# To create a string in Python you need to use either
# single quotes or double quotes. For example:

# string
'This is also a string'

# We can also use double quote
"String built with double quotes"


# Be careful with quotes!
' I'm using single quotes, but will create an error'


# You can use combinations of double and single quotes to get the complete statement.

"Now I'm ready to use the single quotes inside a string!"


# ## Printing a String

# We can use a print statement to print a string.

print('Hello World 1')
print('Use \n to print a new line')
print('\n')

# There is no character data type in python. 
# A character is a string with length 1.

# String Basics

# len() - function to check the length of a string!

len('Hello World')


# ## String Indexing

# Assign s as a string
s = 'Hello World'

# Let's start indexing!
# Show first element (in this case a letter)
print(s[0])

# Next element
print(s[1])

# Next Element
print(s[2])


# We can use a : to perform *slicing* which grabs everything
# up to a designated point. For example:

# Grab everything past the first term all the way to the length of s which is len(s)

print(s[1:])

# String are immutable so original string is not mutated
print(s)

#Grab everthing from 6 UP TO but not including 11
print(s[6:11])

# Grab everything UP TO but not including the 3rd index 
print(s[:3])

#Everything
print(s[:])


# We can also use negative indexing to go backwards.
# Last letter (one index behind 0 so it loops back around)
s[-1]

# Grab everything but the last letter
s[:-1]


# We can also use index and slice notation to grab elements of a sequence by a
# specified step size (the default is 1). For instance we can use two colons in
# a row and then a number specifying the frequency to grab elements. For example:

# Grab everything, but go in steps size of 1
s[::1]

# Grab everything, but go in step sizes of 2
s[::2]

# We can use this to print a string backwards
s[::-1]
print(s[::-1])


# ## String Properties
# Its important to note that strings are immutable.
# This means that once a string is created, the elements within
# it can not be changed or replaced. For example:


# Let's try to change the first letter to 'x' results in an error
s[0] = 'x'

# Something we can do is concatenate strings!

# Concatenate strings!
s + ' concatenate me!'

# We can reassign s completely though!
s = s + ' concatenate me!'

print(s)

# We can use the multiplication symbol to create repetition!

letter = 'z'

letter*10


# ## Basic Built-in String methods

# Objects in Python usually have built-in methods which can be called on the objects.


# Methods are in the form: object.method(parameters)

# Here are some examples of built-in methods in strings:

# Upper Case a string
s.upper()

# Lower case
s.lower()

# Split a string by blank space (this is the default)
s.split()

# Split by a specific element (doesn't include the element that was split on)
s.split('W')

# There are many more methods than the ones covered here.

########################
### Print Formatting ###
########################

# We can use the .format() method to add formatted objects to printed string statements.
#
# The easiest way to show this is through an example:

'Insert another string with curly brackets: {}'.format('The inserted string')

# Using the string .format() method
# The best way to format objects into your strings for print statements is using
# the format method. The syntax is:
#
#  'String here {var1} then also {var2}'.format(var1='something1',var2='something2')
#
# Lets see some examples:


print('This is a string with an {p}'.format(p='insert'))

# Multiple times:
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))


# Several Objects:
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))

