# Alan wrote the following function, which was intended to return all of the factors of number:

# def factors(number):
#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# Alyssa noticed that this code would fail when the input is a negative number, and asked Alan 
# to change the loop. How can he make this work? Note that we're not looking to find the factors 
# for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.

# Bonus Question: What is the purpose of number % divisor == 0 in that code?

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:               # dividing the number by the divisor and checking if the reaminder is 0. Only executes if it is
            result.append(number // divisor)
        divisor -= 1
    return result

# Bonus Answer: It determines whether dividing the integer number is by the integer divisor leaves 
# a remainder of 0. That is, number % divisor == 0 is truthy if number is a factor of divisor.