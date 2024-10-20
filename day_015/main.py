MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0
}

def user_order():
    orderables = ["espresso","latte","cappuccino", "report", "off"]
    order = input("What would you like? espresso/latte/cappuccino\n").lower()
    while order not in orderables:
        order = input("What would you like? espresso/latte/cappuccino\n").lower()
    if order == "off":
        turn_off()
    if order == "report":
        return print_report()
    return order

def print_report():
    print("Generating resource report: \n")
    for k, v in resources.items():
        print(f"{k}: {v}\n")

def turn_off():
    print("shutting down")
    quit()

def check_resources(order):
    for k, v in MENU[order]['ingredients'].items():
        if resources[k] < v:
            print(f"Sorry, there is not enough {k}.")
            return False
    return process_transaction(order)


def process_transaction(order, resources_dict=resources):
    payment = process_coins(order, resources_dict)
    if payment:
        for k, v in MENU[order]['ingredients'].items():
            resources[k] -= v
        resources["Money"] += MENU[order]['cost']
        print(f"Here is your {order}. Enjoy!")
        return True
    else:
        print("Transaction failed.")
        return False

def process_coins(order, resources_dict):
    cost = MENU[order]["cost"]
    print(f"That will cost {cost}. Please input coins into the slot")

    try:
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
    except:
        print("Malfunction, non coin object inserted. Please contact a maintenance official. Shutting down")
        quit()

    money_input  = round((quarters * 0.25) + (dimes * .1) + (nickles * .05) + (pennies * .01), 2)

    if money_input >= cost:
        change = round(money_input - cost, 2)
        print(f"Dispensing change: ${change}")
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False

def coffee_machine():
    while True:
        order = user_order()
        if order and order != "report":
            check_resources(order)


coffee_machine()