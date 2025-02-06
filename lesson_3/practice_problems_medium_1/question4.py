# What will the following two lines of code output?

print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)

# Line 3 prints 0.9 while line 4 prints False. This is because floating point numbers lack precision because of some arcane reason


# Python uses floating point numbers for all numeric operations. Most floating point 
# representations used on computers lack a certain amount of precision, and that can yield unexpected results like these.

# The details of why this happens aren't crucial right now -- it's just something you need to be aware of. 
# One way around the problem is to use the math.isclose function: