# Will the code raise an error?
numbers = [1, 2, 3]
numbers[6] = 5

# It will raise an IndexError since numbers only goes up to 2

# It will raise an error. This error is a result of 6 being an out of 
# range index: the only indexes currently defined for the numbers list 
# are 0, 1, and 2. Any attempt to access or modify an element at an 
# index that does not exist will result in an IndexError exception.