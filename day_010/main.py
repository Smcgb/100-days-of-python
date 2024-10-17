import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "You cannot divide by zero"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():

    num1 = float(input("What's the first number?: "))
    operation = input("Pick an operation from the following: +, -, *, /: ")
    while operation not in operations.keys():
        operation = input("Invalid operation. Please pick an operation from the following: +, -, *, /: ")
    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")


def main():
    print(art.logo)
    calculator()
    while input("Do you want to continue calculating? Type 'y' or 'n': ") == "y":
        calculator()
    print("Goodbye!")

if __name__ == "__main__":
    main()

