# In Python, every object has a unique identifier that can be accessed using the id() function. 
# This function returns the identity of an object, which is guaranteed to be unique for the object's 
# lifetime. For certain basic immutable data types like short strings or integers, Python might reuse 
# the memory address for objects with the same value. This is known as "interning".

# Given the following code, predict the output:

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# True since 42 lies in the range of integers that have the same id. C is also equal to a

# Here, a and c reference the same object in memory, so their ids are the same. b will, in this case, 
# have the same id as a and c due to interning. Therefore, the code will output True.

# In Python, there's a predefined range of integers, specifically from -5 to 256, for which 
# memory locations are pre-assigned. When you reference an integer within this span, Python consistently points to the same memory spot.