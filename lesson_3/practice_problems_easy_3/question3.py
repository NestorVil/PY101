# What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# It will print "hello there". str1 was never reassigned or mutated

# The output is hello there. In Python, assignment of one variable's value to another 
# variable makes both variables point to the same object. Thus, after running line 2, 
# both str1 and str2 reference the same string object. However, that connection between 
# the variables is broken if you assign a different object to one of the variables. 
# Thus, line 3 breaks the connection between str1 and str2. As a result, str2 now references 
# "goodbye!" while str1 continues to reference "hello there".