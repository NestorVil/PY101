# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(list(reversed(numbers)))  #reversed() returns a lazy sequence (an iterator), so need to convert that iterator to a list
print(numbers[::-1])