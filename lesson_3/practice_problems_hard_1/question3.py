# Given the following similar sets of code, what will each code snippet print?

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # one
print(f"two is: {two}")     # two
print(f"three is: {three}") # three

# Variables one, two, and three passed in as reference into the mess_with vars function
# but one two three are new local variables only in the function's scope and don't return anything
# because of this the values of one two and three in the global scope never change

# Since variables one, two, and three in the mess_with_vars function are local, reassigning them does not affect the original lists.

#############################################################################

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")         # ["one"]
print(f"two is: {two}")         # ["two"]
print(f"three is: {three}")     # ["three"]

# Similar to the first snippet, in the mess_with_vars function it is merely creating local variables that
# dont return anything or mutate the one two three variables in the global scope

# Again, the local variables in the mess_with_vars function are being reassigned, but this doesn't change the original lists.


#############################################################################

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # two
print(f"two is: {two}")     # three
print(f"three is: {three}") # one

# The global variables one two three are lists which are passed in as reference into the function mess_with_vars
# Within that funcion each variable is mutated with indexing [] and so the global variables are changed to reflect that

# In this case, the mess_with_vars function modifies the content of the lists directly. 
# Since lists in Python are mutable and passed by object reference, the changes are reflected outside the function.