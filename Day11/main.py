from art import logo
import random

# Display the logo at the start of the game
print(logo)

def calculate_score(cards):
    """
    Calculate the total score of the cards.
    Handles the special case of the Ace card (11 or 1).
    Returns 0 if the hand is a Blackjack.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack condition
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert Ace from 11 to 1
    return sum(cards)

def compare_scores(player_score, computer_score):
    """
    Compare the scores of the player and the computer.
    Returns the result of the game as a string.
    """
    if player_score == computer_score:
        return "It's a draw! 🤝"
    elif computer_score == 0:
        return "Computer wins with a Blackjack! 🖥️"
    elif player_score == 0:
        return "You win with a Blackjack! 🎉"
    elif player_score > 21:
        return "You went over. You lose!😭 Computer wins! 🖥️"
    elif computer_score > 21:
        return "Computer went over. You win! 🎉"
    elif player_score > computer_score:
        return "You win! 🎉"
    else:
        return "Computer wins! 🖥️"

def blackjack():
    """
    The main function that runs the Blackjack game.
    Handles player and computer turns, score calculations, and the game loop.
    """
    # Start the game loop
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        # Initialize player and computer hands
        player_cards = [random.choice(cards) for _ in range(2)]
        computer_cards = [random.choice(cards) for _ in range(2)]
        
        is_game_over = False
        
        # Player's turn
        while not is_game_over:
            player_score = calculate_score(player_cards)
            computer_score = calculate_score(computer_cards)

            # Display current hands and scores
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            # Check for Blackjack or Bust
            if player_score == 0 or computer_score == 0 or player_score > 21:
                is_game_over = True
            else:
                # Ask the player if they want another card
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    player_cards.append(random.choice(cards))
                else:
                    is_game_over = True

        # Computer's turn
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(random.choice(cards))
            computer_score = calculate_score(computer_cards)

        # Display the final results
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare_scores(player_score, computer_score))

        # Ask the player if they want to play again
        if input("Would you like to play again? Type 'yes' or 'no': ").lower() != "yes":
            break

# Deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Start the game
blackjack()
