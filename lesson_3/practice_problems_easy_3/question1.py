# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

numbers.clear()

# or

while numbers:
    numbers.pop()

# can write del numbers[:]
# .clear() most effective I think

print(numbers)