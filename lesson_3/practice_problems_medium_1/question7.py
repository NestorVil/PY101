# One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:
mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail. Did the family's data get ransacked? Why or why not?

# Yes. Dictionaries are mutable so accessing their keys in a function still changes the dictionary munsters.

# Why? In Python, dictionaries are mutable, and when passed to a function, a reference to the dictionary 
# is passed, not a copy. Thus, Spot's demo_dict starts off pointing to the munsters object. 
# As a result, the changes made within the function directly affect the munsters dictionary. 
# The key aspect here is that the nested dictionaries (the individual family members' data) are 
# the ones being mutated. Each family member's dictionary ({"age": x, "gender": y}) is accessed and modified. 
# Since these nested dictionaries are part of the larger munsters dictionary, the changes are reflected in the original data structure.