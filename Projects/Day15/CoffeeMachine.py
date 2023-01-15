from data import resources
from data import MENU

# Global variables
machine_working = True
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def print_report():
    # 3. Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values. e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # functions
    for item in resources:
        if item == 'water' or item == 'milk':
            print(f"{item.capitalize()}: {resources[item]}ml")
        elif item == 'coffee':
            print(f"{item.capitalize()}: {resources[item]}g")
        else:
            print(f"{item.capitalize()}: ${resources[item]}")


def check_resources(choice):
    # 4. Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
    # resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    # not continue to make the drink but print: “ Sorry there is not enough water. ”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.

    resource_ok = True

    for item in MENU[choice]['ingredients']:

        amount_needed = int(MENU[choice]['ingredients'][item])
        amount_in_resources = int(resources[item])

        if item in resources and amount_needed > amount_in_resources:
            print(f"Sorry there is not enough {item}. ")
            resource_ok = False

    return resource_ok


def process_coins():
    # 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should
    # prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    money_inserted = {'quarter': round(int(input("how many quarters?: ")) * QUARTER, 2),
                      'dimes': round(int(input("how many dimes?: ")) * DIME, 2),
                      'nickel': round(int(input("how many nickles?: ")) * NICKEL, 2),
                      'pennies': round(int(input("how many pennies?: ")) * PENNY, 2)}

    return round(sum(money_inserted.values()), 2)


def check_transaction(money, choice):
    # 6. Check transaction successful?
    # a. Check that the user has inserted enough money to purchase the drink they selected.
    # E..g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    # program should say “ Sorry that's not enough money. Money refunded. ”.
    # b. But if the user has inserted enough money, then the cost of the drink gets added to the
    # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # c. If the user has inserted too much money, the machine should offer change.
    # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
    # places
    transaction_success = True

    cost_of_item = MENU[choice]['cost']

    if cost_of_item < money:
        if "money" in resources:
            resources["money"] += cost_of_item
        else:
            resources["money"] = cost_of_item

        money_change = round(money - cost_of_item, 2)
        print(f"Here is ${money_change} in change.")

    else:
        print(" Sorry that's not enough money. Money refunded. ")
        transaction_success = False

    return transaction_success


def make_coffee(choice):
    # 7. Make Coffee.
    # a. If the transaction is successful and there are enough resources to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.
    # E.g. report before purchasing latte:
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $0
    # Report after purchasing latte:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    # latte was their choice of drink.
    for item in MENU[choice]['ingredients']:
        amount_needed = int(MENU[choice]['ingredients'][item])
        if item in resources:
            resources[item] -= amount_needed

    print(f"Here is your {choice} ☕. Enjoy!")


while machine_working:
    # 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    answer = input("\n What would you like? (espresso/latte/cappuccino): ")

    # a. Check the user’s input to decide what to do next.
    if answer == 'espresso' or answer == 'latte' or answer == 'cappuccino':
        if check_resources(choice=answer):
            consumer_payed = process_coins()
            transaction_ok = check_transaction(money=consumer_payed, choice=answer)
            if transaction_ok:
                make_coffee(choice=answer)

        # 2. Turn off the Coffee Machine by entering “ off ” to the prompt
        # a). For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        # the machine. Your code should end execution when this happens
    elif answer == "off":
        # b. The prompt should show every time action has completed, e.g. once the drink is
        # dispensed. The prompt should show again to serve the next customer.
        machine_working = False

    elif answer == "report":
        print_report()

    else:
        print(f"Incorrect input try again")
