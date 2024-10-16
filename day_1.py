'''Create a greeting for your program.
Ask the user for the city that they grew up in and store it in a variable.
Ask the user for the name of a pet and store it in a variable.
Combine the name of their city and pet and show them their band name.'''

def get_city():
    city = input("Where did you grow up?\n")
    return city

def get_pet():
    pet = input("What is your pet's name?\n")
    return pet

def get_band(city, pet):
    return f'Your band name could be {city} {pet}'

def main():
    print(get_band(get_pet(), get_city()))

if __name__ == "__main__":
    main()
