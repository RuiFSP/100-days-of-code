from menudrinks import MenuDrinks
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# build objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_menu = MenuDrinks()

is_machine_working = True

while is_machine_working:

    order = input(f"\n What would you like? ({coffee_menu.get_items()}): ")

    if order == "off":
        is_machine_working = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # find resources for drink
        coffee_choice = coffee_menu.find_drink(order_name=order)

        # check if there are enough resources and money to process order
        if coffee_maker.is_resource_sufficient(drink=coffee_choice) \
                and money_machine.make_payment(cost=coffee_choice.cost):
            coffee_maker.make_coffee(order=coffee_choice)
