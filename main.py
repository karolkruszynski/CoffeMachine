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
            elif i == "money":
                print(f"{i}: {data.resources[i]}$")
            else:
                print(f"{i}: {data.resources[i]}ml")
    return customer_choice

is_resources = False
def resources_sufficient(customer_answer):
    global is_resources

    if customer_answer == "espresso":
        if data.resources["water"] > data.MENU["espresso"]["ingredients"]["water"]:
            if data.resources["coffee"] > data.MENU["espresso"]["ingredients"]["coffee"]:
                print("Enough resources")
                is_resources = True
                data.resources["water"] -= 50
                data.resources["coffee"] -= 18
                data.resources["money"] += 1.5
                # print(data.resources["water"])
                # print(data.resources["coffee"])
                # print(data.resources["money"])
            else:
                print("Sorry there is not enough coffee.")
                is_resources = False
        else:
            print("Sorry there is not enough water.")
            is_resources = False

    if customer_answer == "latte":
        if data.resources["water"] > data.MENU["latte"]["ingredients"]["water"]:
            if data.resources["coffee"] > data.MENU["latte"]["ingredients"]["coffee"]:
                if data.resources["coffee"] > data.MENU["latte"]["ingredients"]["coffee"]:
                    print("Enough resources")
                    is_resources = True
                    data.resources["water"] -= 200
                    data.resources["milk"] -= 150
                    data.resources["coffee"] -= 24
                    data.resources["money"] += 2.5
                    # print(data.resources["water"])
                    # print(data.resources["milk"])
                    # print(data.resources["coffee"])
                    # print(data.resources["money"])
                else:
                    print("Sorry there is not enough coffee.")
                    is_resources = False
            else:
                print("Sorry there is not enough milk.")
                is_resources = False
        else:
            print("Sorry there is not enough water.")
            is_resources = False

    if customer_answer == "cappuccino":
        if data.resources["water"] > data.MENU["cappuccino"]["ingredients"]["water"]:
            if data.resources["coffee"] > data.MENU["cappuccino"]["ingredients"]["coffee"]:
                if data.resources["coffee"] > data.MENU["cappuccino"]["ingredients"]["coffee"]:
                    print("Enough resources")
                    is_resources = True
                    data.resources["water"] -= 250
                    data.resources["milk"] -= 100
                    data.resources["coffee"] -= 24
                    data.resources["money"] += 3.0
                    # print(data.resources["water"])
                    # print(data.resources["milk"])
                    # print(data.resources["coffee"])
                    # print(data.resources["money"])
                else:
                    print("Sorry there is not enough coffee.")
                    is_resources = False
            else:
                print("Sorry there is not enough milk.")
                is_resources = False
        else:
            print("Sorry there is not enough water.")
            is_resources = False


def process_order(customer_answer,is_resources):
    credits = 0.0
    print(f"Yours credits: {credits}$")

    quarters = int(input("How much quarters do you have?: "))
    credits = quarters * 0.25
    print(f"Yours credits: {credits}$")
    dimes = int(input("How much dimes do you have?: "))
    credits += dimes * 0.10
    print(f"Yours credits: {credits}$")
    nickles = int(input("How much nickles do you have?: "))
    credits += nickles * 0.05
    print(f"Yours credits: {credits}$")
    pennies = int(input("How much pennies do you have?: "))
    credits += pennies * 0.01
    print(f"Yours credits: {credits}$")

    sum_of_customer_money = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return_for_customer = 0.0
    espresso_cost = data.MENU["espresso"]["cost"]
    latte_cost = data.MENU["latte"]["cost"]
    cappuccino_cost = data.MENU["cappuccino"]["cost"]

    if customer_answer == "espresso" and is_resources == True:
        if sum_of_customer_money >= espresso_cost:
            return_for_customer = round(sum_of_customer_money - espresso_cost,2)
            print(f"Please this is yours {customer_answer}.")
            print(f"And this is yours change {return_for_customer}$")

    elif customer_answer == "latte" and is_resources == True:
        if sum_of_customer_money >= latte_cost:
            return_for_customer = round(sum_of_customer_money - latte_cost,2)
            print(f"Please this is yours {customer_answer}.")
            print(f"And this is yours change {return_for_customer}$")

    elif customer_answer == "cappuccino" and is_resources == True:
        if sum_of_customer_money >= cappuccino_cost:
            return_for_customer = round(sum_of_customer_money - cappuccino_cost,2)
            print(f"Please this is yours {customer_answer}.")
            print(f"And this is yours change {return_for_customer}$")

    elif is_resources == False:
        print("Sorry there is not enough resources")    #todo: Dodadanie komunikatu czego dokładnie brakuje np. water
        print(f"This is yours change {sum_of_customer_money}")

test = False
while test == False:
    customer_answer = customer_input()
    resources_sufficient(customer_answer)
    if is_resources == True:
        process_order(customer_answer, is_resources)

