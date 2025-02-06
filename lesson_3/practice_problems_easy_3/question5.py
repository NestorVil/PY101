# The following function unnecessarily uses two return statements to return boolean values. 
# Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False



def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return color in ["blue", "green"]

# In functions that return a boolean value, you often don't need separate return statements for the True and False cases. 
# Instead, you can return the value of a conditional expression directly.
# You can also use the in operator to check if the color exists in a list: