# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the operation to preform.
# Preform the operation on the two numbers.
# Print the result to the terminal.
import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

with open("calculator_message.json", "r") as file:
    MESSAGES = json.load(file)

prompt(messages("welcome"))

running = True

while running:
    prompt(messages("number_prompt_1"))
    number1 = input()

    while invalid_number(number1):
        prompt(messages("invalid_number"))
        prompt(messages("number_prompt_1"))
        number1 = input()

    prompt(messages("number_prompt_2"))
    number2 = input()

    while invalid_number(number2):
        prompt(messages("invalid_number"))
        prompt(messages("number_prompt_2"))
        number2 = input()

    prompt(messages("operation_prompt"))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages("invalid_operation"))
        prompt(messages("operation_prompt"))
        operation = input()

    match operation:  # 1 Add, 2 subtract, 3 multiply, 4 divide
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)

    prompt(messages("result").format(output=output))

    prompt(messages("another_operation"))
    answer = input().lower()
    if answer and answer[0].lower() != "y":
        running = False