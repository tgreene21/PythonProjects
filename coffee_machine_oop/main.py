from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffeeMaker = CoffeeMaker()
profit = MoneyMachine()
my_menu = Menu()

def coffee_machine():
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == 'report':
        my_coffeeMaker.report()
        profit.report()
        coffee_machine()
    elif drink == "off":
        print("Turning off")
    else:
        current_order = my_menu.find_drink(drink)
        if my_coffeeMaker.is_resource_sufficient(current_order) and profit.make_payment(current_order.cost):
            my_coffeeMaker.make_coffee(current_order)
            coffee_machine()
        else:
            coffee_machine()


coffee_machine()