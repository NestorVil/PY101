# What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)   # [1, 2]
print(dictionary) # ['first': [1,2]]

# Since num_list is a reference to the original list in dictionary, appending to num_list modifies the list. Thus, the original dictionary is also updated.

# If want to modify num_list but not dictionary:
# can initialize num_list with a reference to a copy of the original list:
dictionary = {"first": [1]}
num_list = dictionary["first"].copy()
num_list.append(2)

# or use list slicing which returns a new list: 
dictionary = {"first": [1]}
num_list = dictionary["first"][:]
num_list.append(2)