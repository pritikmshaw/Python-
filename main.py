MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 28,
        },
        "cost": 1.50,
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
    "water": 500,
    "milk": 450,
    "coffee": 500,
}

should_continue = True
profit = 0


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry. There is not enough {item}")
            return False
    return True


def compare_amount(decision, income):
    global profit
    print("Insert Coins in Quarters, Dimes, Nickles & Pennies ONLY!")
    quarters = float(input("How many quarters:  "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    penny = float(input("How many penny: "))
    amount_inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + penny * 0.01
    if amount_inserted < decision:
        print(f"Sorry. That's not enough money. Money Refunded. \n\t" +
              "Inserted amount is: {amount_inserted}. \nb\t Amount Needed: {decision}")
        return False
    else:
        change = round((amount_inserted - decision), 2)
        print(f"Here is ${change} in change.")
        income += decision
        profit = income
        print(profit)  # Return Profit solve
        return True


def is_transaction_successful(order_resources):
    for item in order_resources:
        resources[item] -= order_resources[item]


while should_continue:
    choice = input(
        "What would you like to have? \n1.Cappuccino\t$3.0\n2.Latte\t\t\t$2.50\n3.Espresso\t\t$1.50\n").lower()
    if choice == "cappuccino" or choice == "espresso" or choice == "latte":
        drink = MENU[choice]
        # print(f"Drink selected:\t{choice.upper()} \n\t\t {drink}")
        if is_resources_sufficient(drink["ingredients"]):
            if compare_amount(drink["cost"], profit):
                is_transaction_successful(drink["ingredients"])
                print(f"Here is your {choice}. Enjoy!")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${profit}")
    else:
        should_continue = False
