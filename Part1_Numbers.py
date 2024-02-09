#####################################
#### Numbers and more in Python! ####
#####################################

# Types of numbers
#
# Python has various "types" of numbers (numeric literals). We'll mainly focus on
# integers and floating point numbers.
#
# Integers are just whole numbers, positive or negative. 
# 
# Floating point numbers in Python either have a decimal point
# in them, or use an exponential (e) to define the number. For example 1.0 and -1.1
# are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is
# also an example of a floating point number in Python.
#

# Basic Arithmetic
# Addition
print(2+1)

# Subtraction
print(2-1)

# Multiplication
print(2*2)


# Division
print(3/2)

# Powers
print(2**3)

# Can also do roots this way
print(4**0.5)


## Variable Assignments

# You also don't need to specify the keyword var while declaring variables
# The names you use when creating these labels need to follow a few rules:
#
#     1. Names can not start with a number.
#     2. There can be no spaces in the name, use _ instead.
#     3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
#     3. It's considered best practice (PEP8) that the names are lowercase.
#

my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

# Show my taxes!
print(my_taxes)


