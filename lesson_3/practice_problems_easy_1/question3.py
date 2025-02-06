# Starting with the string:
famous_words = "seven years ago..."
# Show two different ways to create a new string with "Four score and " 
# prepended to the front of the string referenced by famous_words.

new_string = "Four score and "

print(new_string + famous_words)          # String concatenation
print(f"Four score and {famous_words}")   # String interpolation