from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

off = False
money = 0.00

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def prompt():
    return input("What would you like? (espresso/latte/cappuccino): ")


while not off:

    user_input = prompt()

    if user_input == "off":
        off = True
    elif user_input == "report":
        coffee_machine.report()
    elif user_input == "espresso":
        money_machine.process_coins()
    elif user_input == "latte":
        money_machine.process_coins()
    elif user_input == "cappuccino":
        money_machine.process_coins()
    else:
        print("Invalid request. Try again.")
