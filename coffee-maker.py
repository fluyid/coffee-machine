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
    print(f"M")


def prepare_espresso():
    checking()
    if resources["water"] >= 50 and resources["coffee"] >= 18:
        print("Your espresso is now being prepared")
        resources["water"] -= 50
        resources["coffee"] -= 18
        preparing()
    elif resources["water"] < 50:
        low_resource("water")
    elif resources["coffee"] < 18:
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
        print(f"Sorry we dont currently serve {coffee}. In case you choose the right coffee, make sure there is no typo")




coffee_machine_status = "on"

while coffee_machine_status == "on":
    input_coffee = input("What kind of coffee would you like? We currently have Cappuccino, Espresso and Latte? \n").lower()
    if input_coffee == "off":
        coffee_machine_status = "off"
    else:
        prepare_coffee(input_coffee)
        time.sleep(3)