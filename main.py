from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

is_off = False

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def prompt():
    return input(f"What would you like? ({menu.get_items()}): ")


while not is_off:

    user_input = prompt()

    if user_input == "off":
        off = True
    elif user_input == "report":
        coffee_machine.report()
        if money_machine.profit > 0:
            money_machine.report()
    else:
        drink = menu.find_drink(user_input)
