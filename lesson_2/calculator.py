# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the operation to preform.
# Preform the operation on the two numbers.
# Print the result to the terminal.
print("Welcome to Calculator!")

print("What's the first number?:")
number1 = input()
print("What's the second number?:")
number2 = input()

print("What operation would you like to preform?\n"
      "1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

match operation:  # 1 Add, 2 subtract, 3 multiply, 4 divide
    case "1":
        result = float(number1) + float(number2)
    case "2":
        result = float(number1) - float(number2)
    case "3":
        result = float(number1) * float(number2)
    case "4":
        result = float(number1) / float(number2)

print(f"The result is: {result:.2f}")