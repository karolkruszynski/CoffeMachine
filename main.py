import data
import random


def customer_input():
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_choice == "off":
        print("")
    elif customer_choice == "report":
        for i in data.resources:
            if i == "coffee":
                print(f"{i}: {data.resources[i]}g")
            else:
                print(f"{i}: {data.resources[i]}ml")
    return customer_choice

is_resources = False
def resources_sufficient(customer_answer):
    global is_resources
    if customer_answer == "espresso":
        if data.resources["water"] > data.MENU["espresso"]["ingredients"]["water"]:
            if data.resources["coffee"] > data.MENU["espresso"]["ingredients"]["coffee"]:
                print("Oto ESPRESSO!")
                data.resources["water"] -= 50
                data.resources["coffee"] -= 18
                data.resources["money"] += 1.5
                print(data.resources["water"])
                print(data.resources["coffee"])
                print(data.resources["money"])
                is_resources = True
            else:
                    print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    if customer_answer == "latte":
        if data.resources["water"] > data.MENU["latte"]["ingredients"]["water"]:
            if data.resources["coffee"] > data.MENU["latte"]["ingredients"]["coffee"]:
                if data.resources["coffee"] > data.MENU["latte"]["ingredients"]["coffee"]:
                    print("Oto LATTE!")
                    data.resources["water"] -= 200
                    data.resources["milk"] -= 150
                    data.resources["coffee"] -= 24
                    data.resources["money"] += 2.5
                    print(data.resources["water"])
                    print(data.resources["milk"])
                    print(data.resources["coffee"])
                    print(data.resources["money"])
                else:
                        print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough water.")
    if customer_answer == "cappuccino":
        if data.resources["water"] > data.MENU["cappuccino"]["ingredients"]["water"]:
            if data.resources["coffee"] > data.MENU["cappuccino"]["ingredients"]["coffee"]:
                if data.resources["coffee"] > data.MENU["cappuccino"]["ingredients"]["coffee"]:
                    print("Oto CAPUCCINO!")
                    data.resources["water"] -= 250
                    data.resources["milk"] -= 100
                    data.resources["coffee"] -= 24
                    data.resources["money"] += 3.0
                    print(data.resources["water"])
                    print(data.resources["milk"])
                    print(data.resources["coffee"])
                    print(data.resources["money"])
                else:
                    print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough water.")


def process_coins(customer_answer,is_resources):
    quarters = int(input("How much quarters do you have?: "))
    dimes = int(input("How much dimes do you have?: "))
    nickles = int(input("How much nickles do you have?: "))
    pennies = int(input("How much pennies do you have?: "))
    sum_of_customer_money = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return_for_customer = 0
    espresso_cost = data.MENU["espresso"]["cost"]
    if customer_answer == "espresso" and is_resources == True:
        if sum_of_customer_money > data.MENU["espresso"]["cost"]:
            # sum_of_customer_money - espresso_cost = return_for_customer
            print('x')

test = False
while test == False:
    customer_answer = customer_input()
    resources_sufficient(customer_answer)
    process_coins(customer_answer, is_resources)

