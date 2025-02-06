# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))

# The output is False. nan -- not a number -- is a special numeric value that indicates that an operation that was intended to return a number failed. Python doesn't let you use == to determine whether a value is nan.

# To test whether the value is nan, you can use the math.isnan() function