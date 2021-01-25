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

# TODO: 1. print report of all coffee machine resources

def get_report():
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource}:{resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource}:{resources[resource]}g")
        else:
            print(f"{resource}: ${resources[resource]}")





def prepare_drink(order):
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] >= MENU[order]["ingredients"][ingredient]:
            pass
        else:
            print(f"Sorry, there is not enough {ingredient}.")


def insert_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters? ")) * .25
    total += int(input("how many dimes? ")) * .10
    total += int(input("how many nickels? ")) * .05
    total += int(input("how many pennies? ")) * .01
    return total


def transaction(total, order):
    if total >= MENU[order]["cost"]:
        if total > MENU[order]["cost"]:
            print(f'Your change is ${round(total - MENU[order]["cost"],2)}😀')
        for ingredient in MENU[order]['ingredients']:
            resources[ingredient] -= MENU[order]['ingredients'][ingredient]
        if "money" in resources:
            resources["money"] += MENU[order]["cost"]
        else:
            resources["money"] = float(MENU[order]["cost"])
    else:
        print("Sorry, that's not enough money. Money refunded. ")








turn_on_machine = True
while turn_on_machine:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'report':
        get_report()
    elif order == 'off':
        turn_on_machine = False
    else:
        prepare_drink(order)
        total = insert_coin()
        transaction(total, order)
        print(f"Here is your {order}☕, enjoy!")




