# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the operation to preform.
# Preform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    
    return False

prompt("Welcome to Calculator!")

prompt("What's the first number?:")
number1 = input()

while invalid_number(number1):
    prompt(f"{number1} is not valid.")
    number1 = input()

prompt("What's the second number?:")
number2 = input()

while invalid_number(number2):
    prompt(f"{number2} is not valid.")
    number2 = input()

prompt("What operation would you like to preform?\n"
      "1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
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

prompt(f"The result is: {result:.2f}")