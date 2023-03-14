from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

'''
1. present menu to customer (drinks + report)
2. ask for input
3. if resources - print out resources
4. if drink - check if drink exists in menu, check if resources sufficient
5. ask for payment
6. if payment is >= cost, return change, else refund money
7. give the customer their drink
8. if off - turn machine off 
'''

'''
MenuItem.


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
        '''

