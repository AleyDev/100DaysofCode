import art

# Display the program logo
print(art.logo)

# Function to find the highest bidder and declare the winner
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    # Loop through the dictionary to find the highest bid
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # Print the winner's name and their bid amount
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# Function to clear the screen (simulated with multiple blank lines)
def clear_screen():
    print("\n" * 100)

# Dictionary to store bids
bids = {}

# Variable to control the bidding loop
continue_bidding = True
while continue_bidding:
    # Ask for the user's name and bid amount
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price  # Add the bid to the dictionary

    # Ask if there are other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if should_continue == "no":
        # End the loop and declare the winner
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clear the screen before the next bidder
        clear_screen()
