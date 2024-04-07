from data import resources, MENU
import time


def checking():
    print("Hang on while we check if we have enough resources")
    time.sleep(3)


def preparing():
    time.sleep(3)
    print("Your coffee is almost ready")
    time.sleep(2)
    print("Your coffee is ready ^^")
    print("Enjoy!")


def low_resource(resource):
    print(f"Sorry we are low on {resource}")
    print("Here is your refund")


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")


# Espresso details
espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]

# Latte details
latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]

# Cappuccino details
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = MENU["cappuccino"]["cost"]


def calculating_currency():
    pass


def prepare_espresso():
    checking()
    if resources["water"] >= espresso_water and resources["coffee"] >= espresso_coffee:
        print("Your espresso is now being prepared")
        resources["water"] -= espresso_water
        resources["coffee"] -= espresso_coffee
        preparing()
    elif resources["water"] < espresso_water:
        low_resource("water")
    elif resources["coffee"] < espresso_coffee:
        low_resource("coffee")
    else:
        low_resource("resources")


def prepare_latte():
    checking()
    if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
        print("Your latte is now being prepared")
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        preparing()
    elif resources["water"] < 200:
        low_resource("water")
    elif resources["milk"] < 150:
        low_resource("milk")
    elif resources["coffee"] < 24:
        low_resource("coffee")
    else:
        low_resource("resources")


def prepare_cappuccino():
    checking()
    if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
        print("Your cappuccino is now being prepared")
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        preparing()
    elif resources["water"] < 250:
        low_resource("water")
    elif resources["milk"] < 100:
        low_resource("milk")
    elif resources["coffee"] < 24:
        low_resource("coffee")
    else:
        low_resource("resources")


def prepare_coffee(coffee):
    if coffee == "latte":
        prepare_latte()
    elif coffee == "espresso":
        prepare_espresso()
    elif coffee == "cappuccino":
        prepare_cappuccino()
    else:
        print(f"Sorry we dont currently serve {coffee}. Make sure there is no typo")


coffee_machine_status = "on"

while coffee_machine_status == "on":
    input_coffee = input("We currently have Cappuccino, Espresso and Latte? \n").lower()
    if input_coffee == "off":
        coffee_machine_status = "off"
    elif input_coffee == "report":
        print_report()
    else:
        prepare_coffee(input_coffee)
        time.sleep(3)
