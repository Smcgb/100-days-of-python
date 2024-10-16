import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_password_complexity():
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    return nr_letters, nr_symbols, nr_numbers

def generate_password(nr_letters, nr_symbols, nr_numbers):

    password = []

    password.extend(random.choice(letters) for _ in range(nr_letters))
    password.extend(random.choice(symbols) for _ in range(nr_symbols))
    password.extend(random.choice(numbers) for _ in range(nr_numbers))

    random.shuffle(password)

    return password

def main():

    print("Welcome to the PyPassword Generator!")
    print(''.join((generate_password(*get_password_complexity()))))

if __name__ == "__main__":
    main()
