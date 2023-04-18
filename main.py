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

print()
def resources_sufficient(customer_answer):
    if customer_answer == "espresso":
        if data.resources["water"] > data.MENU["espresso"]["ingredients"]["water"]:
            print("Oto espresso!")

customer_answer = customer_input()
resources_sufficient(customer_answer)


