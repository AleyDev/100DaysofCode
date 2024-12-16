# Menu dictionary containing coffee types, their ingredients, and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,      # Amount of water required for espresso in ml
            "coffee": 18,     # Amount of coffee required for espresso in grams
        },
        "cost": 1.5,          # Cost of espresso in dollars
    },
    "latte": {
        "ingredients": {
            "water": 200,     # Amount of water required for latte in ml
            "milk": 150,      # Amount of milk required for latte in ml
            "coffee": 24,     # Amount of coffee required for latte in grams
        },
        "cost": 2.5,          # Cost of latte in dollars
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,     # Amount of water required for cappuccino in ml
            "milk": 100,      # Amount of milk required for cappuccino in ml
            "coffee": 24,     # Amount of coffee required for cappuccino in grams
        },
        "cost": 3.0,          # Cost of cappuccino in dollars
    }
}

# Variable to track the machine's total profit
profit = 0

# Dictionary containing the machine's current resources
resources = {
    "water": 300,  # Initial amount of water in ml
    "milk": 200,   # Initial amount of milk in ml
    "coffee": 100, # Initial amount of coffee in grams
}

# Function to check if there are sufficient resources to make the chosen drink
def is_resource_sufficient(order_ingredients):
    """Returns True if resources are sufficient for the order, False otherwise."""
    for item in order_ingredients:  # Loop through each required ingredient
        if order_ingredients[item] > resources[item]:  # Check if the resource is enough
            print(f"​Sorry there is not enough {item}.")  # Inform user about insufficient resource
            return False
    return True  # If all resources are sufficient, return True

# Function to process coins entered by the user
def process_coins():
    """Returns the total value of coins inserted by the user."""
    print("Please insert coins.")  # Prompt user to insert coins
    total = int(input("how many quarters?: ")) * 0.25  # Count quarters and calculate total value
    total += int(input("how many dimes?: ")) * 0.1     # Count dimes and calculate total value
    total += int(input("how many nickles?: ")) * 0.05  # Count nickels and calculate total value
    total += int(input("how many pennies?: ")) * 0.01  # Count pennies and calculate total value
    return total  # Return the total value of coins

# Function to check if the transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment is sufficient, otherwise refunds money and returns False."""
    if money_received >= drink_cost:  # Check if payment is enough for the drink
        change = round(money_received - drink_cost, 2)  # Calculate and round change
        print(f"Here is ${change} in change.")  # Inform user about the change
        global profit  # Access the global profit variable
        profit += drink_cost  # Add the cost of the drink to the total profit
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")  # Insufficient payment message
        return False

# Function to make the selected coffee and deduct used resources
def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources and serve the coffee."""
    for item in order_ingredients:  # Loop through each ingredient required
        resources[item] -= order_ingredients[item]  # Deduct the used amount from resources
    print(f"Here is your {drink_name} ☕️. Enjoy!")  # Serve the coffee to the user

# Main program loop to keep the coffee machine running
is_on = True  # Flag to track if the machine is on

while is_on:
    # Prompt the user to choose an action or a drink
    choice = input("​What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":  # Secret code to turn off the machine
        is_on = False  # Stop the loop to shut down the machine
        print("Turning off the coffee machine. Goodbye!")  # Inform user

    elif choice == "report":  # Command to print the machine's current resources
        print(f"Water: {resources['water']}ml")  # Display remaining water
        print(f"Milk: {resources['milk']}ml")    # Display remaining milk
        print(f"Coffee: {resources['coffee']}g") # Display remaining coffee
        print(f"Money: ${profit}")               # Display total profit

    elif choice in MENU:  # If the user selects a valid drink
        drink = MENU[choice]  # Get the selected drink's data from the menu
        if is_resource_sufficient(drink["ingredients"]):  # Check if resources are sufficient
            payment = process_coins()  # Process coins inserted by the user
            if is_transaction_successful(payment, drink["cost"]):  # Check if transaction is successful
                make_coffee(choice, drink["ingredients"])  # Make the selected drink

    else:
        print("Invalid input. Please choose a valid option.")  # Handle invalid inputs
