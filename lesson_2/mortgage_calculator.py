import json

with open("mortgage_messages.json", "r") as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError
    except ValueError:
        return True

    return False

def valid_loan(number_str):
    try:
        number = float(number_str)
        if number < 0:
            raise ValueError
    except ValueError:
        return True

    return False

def get_loan():
    prompt(messages("loan_prompt"))
    loan_amount = input()

    while invalid_number(loan_amount):
        prompt(messages("valid_positive"))
        loan_amount = input()

    return loan_amount


def get_interest():
    prompt(messages("interest_prompt"))
    interest_rate = input()

    while valid_loan(interest_rate):
        prompt(messages("valid_loan"))
        interest_rate = input()

    return interest_rate

def get_loan_term():
    prompt(messages("valid_length"))
    loan_duration = input()

    while invalid_number(loan_duration):
        prompt(messages("valid_positive"))
        loan_duration = input()

    return loan_duration


def get_monthly_payment(amount, rate, duration):
    rate = float(rate)
    duration = float(duration)
    amount = float(amount)

    if rate == 0:
        return float(amount) / duration

    rate /= 100
    apr = rate / 12
    return amount * (apr / (1 - (1 + apr) ** (-duration)))

def another_calculation():
    answer = input().lower()
    while True:
        if answer.startswith("n") or answer.startswith("y"):
            break

        prompt(messages("starts_with"))
        answer = input().lower()

    return  answer[0] == "n"

def main():
    running = True

    prompt(messages("welcome"))

    while running:
        loan_amount = get_loan()

        interest_rate = get_interest()

        loan_duration = get_loan_term()

        monthly_payment = get_monthly_payment(
            loan_amount, interest_rate, loan_duration)

        prompt(f"Your monthly payment is ${monthly_payment:.2f}")

        prompt(messages("another_calc"))

        if another_calculation():
            prompt(messages("bye"))
            running = False

main()