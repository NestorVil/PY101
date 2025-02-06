# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# It will print [{"first": 42}, {"second": "value2"}, 3, 4, 5] since .copy() creates a shallow copy of nested dictionaries

# There are two kinds of copy operations when working with lists: a deep copy and a shallow copy.

# A shallow copy only makes a duplicate of the outermost values in an object. If we perform a shallow copy 
# on my_list1, we end up with two different lists, but we still only have one occurrence each of { first: 42 } 
# and { second: 'value2' }. In this case, both my_list1[0] and my_list2[0] point to the same dictionary in memory. 
# Likewise, my_list1[1] and my_list2[1] point to the { second: 'value2' } dictionary.

# my_list1[0] and my_list2[0] point to the same dictionary, { first: "value1" }. 
# Thus, when we replace the value of the first property by using my_list2[0]['first'], 
# the change shows up in my_list1 as well. 