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
}

profit = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(drink_choice):
    drink_choice_water = MENU[drink_choice]["ingredients"]["water"]
    drink_choice_coffee = MENU[drink_choice]["ingredients"]["coffee"]

    if drink_choice == "espresso":
        drink_choice_milk = 0
    else:
        drink_choice_milk = MENU[drink_choice]["ingredients"]["milk"]

    if resources["water"] - drink_choice_water < 0:
        print("Sorry there is not enough water")
        return False
    elif resources["milk"] - drink_choice_milk < 0:
        print("Sorry there is not enough milk")
        return False
    elif resources["coffee"] - drink_choice_coffee < 0:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

    return total

def transaction(drink_choice, money):

    if money < MENU[drink_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        change = round(money - MENU[drink_choice]["cost"], 2)
        global profit
        profit += MENU[drink_choice]["cost"]
        print(f"Here is your change of ${change}")
        return True


def espresso():
    resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    print("Here is your Espresso. Enjoy!")

def latte():
    resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
    print("Here is your latte. Enjoy!")

def cappuccino():
    resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
    print("Here is your Cappuccino. Enjoy!")

def coffee_machine():
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "report":
        report()
        coffee_machine()
    elif drink == "off":
        print("Turning off")
    elif drink == "cappuccino":
        if check_resources("cappuccino"):
            if transaction("cappuccino", process_coins()):
                cappuccino()
        coffee_machine()
    elif drink == "espresso":
        if check_resources("espresso"):
            if transaction("espresso", process_coins()):
                espresso()
        coffee_machine()
    elif drink == "latte":
        if check_resources("latte"):
            if transaction("latte", process_coins()):
                latte()
        coffee_machine()
    else:
        print("Invalid Response. Please try again")
        coffee_machine()

coffee_machine()