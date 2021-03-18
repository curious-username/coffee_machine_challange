water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def machine_buy_option():
    """Choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino."""

    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()

    if choice == '1' or choice == 'espresso':
        espresso_supply_checker()

    elif choice == '2' or choice == 'latte':
        latte_supply_checker()

    elif choice == '3' or choice == 'cappuccino':
        cappuccino_supply_checker()

    elif choice == 'back':
        print()
    else:
        print()


def espresso_supply_checker():
    global water, milk, coffee_beans, cups, money

    if water < 250:
        print("Sorry, not enough water!\n")
    elif coffee_beans < 16:
        print("Sorry, not enough coffee beans\n")
    elif cups < 1:
        print("Sorry, not enough cups!\n")
    else:
        print("I have enough resources, making you a coffee!\n")
        water -= 250
        coffee_beans -= 16
        money += 4
        cups -= 1


def latte_supply_checker():
    global water, milk, coffee_beans, cups, money

    if water < 350:
        print("Sorry, not enough water!\n")
    elif milk < 75:
        print("Sorry, not enough milk!\n")
    elif coffee_beans < 20:
        print("Sorry, not enough coffee beans\n")
    elif cups < 1:
        print("Sorry, not enough cups!\n")
    else:
        print("I have enough resources, making you a coffee!\n")
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7


def cappuccino_supply_checker():
    global water, milk, coffee_beans, cups, money

    if water < 200:
        print("Sorry, not enough water!\n")
        return
    elif milk < 100:
        print("Sorry, not enough milk!\n")
    elif coffee_beans < 12:
        print("Sorry, not enough coffee beans\n")
    elif cups < 1:
        print("Sorry, not enough cups!\n")
    else:
        print("I have enough resources, making you a coffee!\n")
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6


def machine_fill_option():
    """ Asking user how much water, milk, coffee and how many disposable cups they want to add into the coffee machine. """
    global water, milk, coffee_beans, cups

    print("\nWrite how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())
    print()

    # coffee_machine_stats()


def machine_take_funds():
    """Give -->#ALL<-- the money that it earned from selling coffee."""
    global money
    print(f"\nI gave you ${money}")
    money -= money
    print()
    # coffee_machine_stats()


def coffee_machine_stats():
    """Displays machine stats"""
    global water, milk, coffee_beans, cups, money
    print()
    print("The coffee machine has:")
    if money == 0:
        print(f"{water} of water\n{milk} of milk\n{coffee_beans} of coffee beans\n{cups} of disposable cups\n{money} of money")
    else:
        print(f"{water} of water\n{milk} of milk\n{coffee_beans} of coffee beans\n{cups} of disposable cups\n${money} of money")

    print()


def start_here():
    """Initial starting point, a kind of main menu"""
    # coffee_machine_stats()

    print("Write action (buy, fill, take, remaining, exit):")
    user_choice = input()

    if user_choice == 'buy':
        machine_buy_option()
    elif user_choice == 'fill':
        machine_fill_option()
    elif user_choice == 'take':
        machine_take_funds()
    elif user_choice == 'remaining':
        coffee_machine_stats()
    elif user_choice == 'exit':
        global exit_time
        exit_time = 'gremlins'
    else:
        print("Invalid input, try again.")
        print()


exit_time = 'unicorns'

while exit_time is 'unicorns':
    start_here()



