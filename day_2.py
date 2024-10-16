def get_bill_amount():
    try:
        bill_amount = round(float(input("What was the total bill? $")), 2)
        assert type(bill_amount) == float
        return bill_amount
    except ValueError:
        print("Please enter a valid number.")
        return get_bill_amount()

def get_tip_percentage():
    print("What percentage tip would you like to give?")
    print('For example, you can enter 10 for 10%')
    try:
        tip_percentage = int(input("Tip percentage: "))
        assert type(tip_percentage) == int
        return tip_percentage / 100 + 1
    except ValueError:
        print("Please enter a valid number.")
        return get_tip_percentage()

def get_number_of_people():
    print("How many people to split the bill?")
    try:
        number_of_people = int(input("Number of people: "))
        assert type(number_of_people) == int
        return number_of_people
    except ValueError:
        print("Please enter a valid number.")
        return get_number_of_people()

def calculate_bill(bill_amount, tip_percentage, number_of_people):
    print(f"Calculating bill for {number_of_people} people for bill of {bill_amount} and a tip of {round((tip_percentage - 1) * 100, 2)}.")
    bill_per_person = round(bill_amount * tip_percentage / number_of_people, 2)
    return bill_per_person

def main():
    bill_per_person = calculate_bill(get_bill_amount(), get_tip_percentage(), get_number_of_people())
    print(f"Each person should pay: ${bill_per_person}")

if __name__ == "__main__":
    main()
