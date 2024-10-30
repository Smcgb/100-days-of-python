from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
register = MoneyMachine()
coffee_maker = CoffeeMaker()

def start_order():
    order = input(f"What would you like to order?\n{menu.get_items()}\n")
    if order.lower() == "off":
        print("system exiting")
        quit()
    elif order.lower() == "report":
        coffee_maker.report()
        register.report()
        start_order()
    else:
        if not menu.find_drink(order):
            start_order()

    return menu.find_drink(order)


def main():
    while True:
        order = start_order()
        if coffee_maker.is_resource_sufficient(order):
            print(f"That will be {order.cost}")
            pay = register.make_payment(order.cost)
            if pay:
                coffee_maker.make_coffee(order)
        else:
            print("Insufficient resources. Please contact maintenance to refill resources.")
            print("Shutting Down")
            quit()



if __name__ == "__main__":
    main()