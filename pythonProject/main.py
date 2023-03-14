from art import logo
from menu import MENU, resources

print(logo)

print("COFFEE MACHINE")

# constants for the coffee ingredients and cost
WATER_FOR_ESPRESSO = MENU["espresso"]["ingredients"]["water"]
COFFEE_FOR_ESPRESSO = MENU["espresso"]["ingredients"]["coffee"]
COST_FOR_ESPRESSO = MENU["espresso"]["cost"]

WATER_FOR_LATTE = MENU["latte"]["ingredients"]["water"]
MILK_FOR_LATTE = MENU["latte"]["ingredients"]["milk"]
COFFEE_FOR_LATTE = MENU["latte"]["ingredients"]["coffee"]
COST_FOR_LATTE = MENU["latte"]["cost"]

WATER_FOR_CAPP = MENU["cappuccino"]["ingredients"]["water"]
MILK_FOR_CAPP = MENU["cappuccino"]["ingredients"]["milk"]
COFFEE_FOR_CAPP = MENU["cappuccino"]["ingredients"]["coffee"]
COST_FOR_CAPP = MENU["cappuccino"]["cost"]

# variables for resources
total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]
total_money = resources["money"]


# check if there are enough resources before purchasing the drink
def check_resources():
    if choice == "1":
        if total_water - WATER_FOR_ESPRESSO < 0 or total_coffee - COFFEE_FOR_ESPRESSO < 0:
            print("Sorry, not enough resources for an espresso. Need to refill.")
            return False
    elif choice == "2":
        # drink = "latte"
        if total_water - WATER_FOR_LATTE < 0 or total_coffee - COFFEE_FOR_LATTE < 0 or total_milk - MILK_FOR_LATTE < 0:
            print("Sorry, not enough resources for a latte. Need to refill.")
            return False
    else:
        if total_water - WATER_FOR_CAPP < 0 or total_coffee - COFFEE_FOR_CAPP < 0 or total_milk - MILK_FOR_CAPP < 0:
            print("Sorry, not enough resources for a cappuccino. Need to refill.")
            return False
    return True


# function to calculate cost of the drink
def calculate_cost(water, milk, coffee, money):
    print("Please insert coins.")
    num_quarters = int(input("How many quarters? "))
    num_dimes = int(input("How many dimes? "))
    num_nickels = int(input("How many nickels? "))
    num_pennies = int(input("How many pennies? "))

    value_quarters = 0.25 * num_quarters
    value_dimes = 0.10 * num_dimes
    value_nickels = 0.05 * num_nickels
    value_pennies = 0.01 * num_pennies

    total_value = value_quarters + value_dimes + value_nickels + value_pennies

    drink = "espresso"
    cost_of_drink = COST_FOR_ESPRESSO
    water_for_drink = WATER_FOR_ESPRESSO
    coffee_for_drink = COFFEE_FOR_ESPRESSO
    milk_for_drink = MILK_FOR_LATTE

    if choice == "1":
        change = str(round(total_value - cost_of_drink, 2))
        if total_value == cost_of_drink or total_value > COST_FOR_ESPRESSO:
            print(f"Here is ${change} in change.")
            print("Here is your espresso ☕️. Enjoy!\n")
            # subtract ingredients from total resources
            water -= WATER_FOR_ESPRESSO
            coffee -= COFFEE_FOR_ESPRESSO
            # add money to total in resources
            money += COST_FOR_ESPRESSO
        else:
            print("Sorry that's not enough money. Money refunded.\n")
    elif choice == "2":
        change = str(round(total_value - COST_FOR_LATTE, 2))
        if total_value == COST_FOR_LATTE or total_value > COST_FOR_LATTE:
            print(f"Here is ${change} in change.")
            print("Here is your latte ☕️. Enjoy!\n")
            # subtract ingredients from total resources
            water -= WATER_FOR_LATTE
            coffee -= COFFEE_FOR_LATTE
            milk -= MILK_FOR_LATTE
            # add money to total in resources
            money += COST_FOR_LATTE
        else:
            print("Sorry that's not enough money. Money refunded.\n")
    elif choice == "3":
        change = str(round(total_value - COST_FOR_CAPP, 2))
        if total_value == COST_FOR_CAPP or total_value > COST_FOR_CAPP:
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino ☕️. Enjoy!\n")
            # subtract ingredients from total resources
            water -= WATER_FOR_CAPP
            coffee -= COFFEE_FOR_CAPP
            milk -= MILK_FOR_CAPP
            # add money to total in resources
            money += COST_FOR_CAPP
        else:
            print("Sorry that's not enough money. Money refunded.\n")
    return water, milk, coffee, money


end_of_transaction = False

while not end_of_transaction:
    print("Please select from the following: \n"
          f"1. espresso - ${COST_FOR_ESPRESSO}\n"
          f"2. latte - ${COST_FOR_LATTE}\n"
          f"3. cappuccino - ${COST_FOR_CAPP}\n"
          "4. resources report"
          )
    print("Please enter 'off' to turn off the machine")
    choice = input().lower()

    if choice == "off":
        end_of_transaction = True
    elif choice == "4":
        print("Resources Report:")
        print("-----------------")
        for key, value in resources.items():
            if key == "coffee":
                print(f"{key}: {total_coffee}" + "g")
            elif key == "money":
                print(f"{key}: ${total_money}\n")
            elif key == "water":
                print(f"{key}: {total_water}" + "ml")
            else:
                print(f"{key}: {total_milk}" + "ml")
    elif choice == "1" or choice == "2" or choice == "3":
        if check_resources():
            total_water, total_milk, total_coffee, total_money = \
                calculate_cost(total_water, total_milk, total_coffee, total_money)
    else:
        print("Invalid input. Please try again.")
