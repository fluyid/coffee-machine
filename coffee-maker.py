from data import resources, MENU
import time

# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
income = 0


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
    print(f"Income: ${income:.2f}")


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
    insert_quarters = int(input("Enter some quarters (25cents): "))
    insert_dimes = int(input("Enter some dimes (10cents): "))
    insert_nickles = int(input("Enter some nickles (5cents): "))
    insert_pennies = int(input("Enter some pennies (1 penny): "))
    total = 0.25 * insert_quarters + 0.1 * insert_dimes + 0.05 * insert_nickles + 0.01 * insert_pennies
    return total


def prepare_espresso():
    checking()
    total = calculating_currency()
    if resources["water"] >= espresso_water and resources["coffee"] >= espresso_coffee and total >= espresso_cost:
        print("Your espresso is now being prepared")
        resources["water"] -= espresso_water
        resources["coffee"] -= espresso_coffee
        global income
        income += espresso_cost
        preparing()
    elif resources["water"] < espresso_water:
        low_resource("water")
    elif resources["coffee"] < espresso_coffee:
        low_resource("coffee")
    elif total < espresso_cost:
        print(f"Sorry, the amount you provided is insufficient. Here is your refund of {total:.2f}")
    else:
        low_resource("resources")
    if total > espresso_cost:
        print(f"Here is your change: {(total - espresso_cost):.2f}")

def prepare_latte():
    checking()
    total = calculating_currency()
    if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24 and total >= latte_cost:
        print("Your latte is now being prepared")
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        global income
        income += latte_cost
        preparing()
    elif resources["water"] < 200:
        low_resource("water")
    elif resources["milk"] < 150:
        low_resource("milk")
    elif resources["coffee"] < 24:
        low_resource("coffee")
    elif total < latte_cost:
        print(f"Sorry, the amount you provided is insufficient. Here is your refund of {total:.2f}")
    else:
        low_resource("resources")
    if total > latte_cost:
        print(f"Here is your change: {(total - latte_cost):.2f}")


def prepare_cappuccino():
    checking()
    total = calculating_currency()
    if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24 and total >= cappuccino_cost:
        print("Your cappuccino is now being prepared")
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        global income
        income += cappuccino_cost
        preparing()
    elif resources["water"] < 250:
        low_resource("water")
    elif resources["milk"] < 100:
        low_resource("milk")
    elif resources["coffee"] < 24:
        low_resource("coffee")
    elif total < latte_cost:
        print(f"Sorry, the amount you provided is insufficient. Here is your refund of {total:.2f}")
    else:
        low_resource("resources")
    if total > cappuccino_cost:
        print(f"Here is your change: {(total - cappuccino_cost):.2f}")


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
        print("Sayonara")
        coffee_machine_status = "off"
    elif input_coffee == "report":
        print_report()
    else:
        prepare_coffee(input_coffee)
        time.sleep(3)
