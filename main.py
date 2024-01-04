from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

is_off = False

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while not is_off:

    user_input = input(f"What would you like? ({menu.get_items()}): ")

    if user_input == "off":
        is_off = True
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
