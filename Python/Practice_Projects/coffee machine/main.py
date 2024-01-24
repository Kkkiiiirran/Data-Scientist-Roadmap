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

def ask_coins():
    quarters = float(input("How many quarter?"))
    dimes = float(input("How many dimes?"))
    nickels = float(input("How many nickels?"))
    pennies = float(input("How many pennies?"))
    total = 0
    total += quarters * .25
    total += dimes * .01
    total+= nickels * .05
    total+= pennies * .001
    return total

machine = True
while machine:
    order = input("what would you like latte, cappucino, espresso?")

    if order == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")

    else:
        water = MENU[order]["ingredients"]["water"]
        coffee = MENU[order]["ingredients"]["coffee"]

        if order != "espresso":
            milk = MENU[order]["ingredients"]["milk"]
            if milk <= resources["milk"]:
                resources["milk"] -= milk
            else:
                print("not sufficient milk")
                continue

        if water <= resources["water"] and coffee <= resources["coffee"]:
            resources["water"] -= water
            resources["coffee"] -= coffee
            money = ask_coins()
            if money == MENU[order]["cost"]:
                print(f"Here's your {order}")
            elif money > MENU[order]["cost"]:
                change = money - MENU[order]["cost"]
                print(f"Here's your {order} and your change: ${change}")
            else:
                print("Money not sufficient")
        else:
            print("not sufficient resources")
    
    


