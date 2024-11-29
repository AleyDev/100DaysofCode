import random
import hangman_art
import hangman_words

# Display the Hangman logo
print(hangman_art.logo)

# Select a random word from the word list
chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)  # Debugging: remove this line to hide the chosen word

# Create placeholders for the word to guess
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder) 
  
# Initialize lives and game state
lives = 6
game_over = False
correct_letters = []

while not game_over:
    print(f"*****************************{lives}/6 LIVES LEFT*****************************")
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters: 
      print(f"You've already guessed {guess}")
      
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: ", display)
    
    # Check if the guess was incorrect
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        if lives == 0:
            game_over = True
            print(F"***************IT WAS {chosen_word}! YOU LOSE***************")
    
    # Check if the player has guessed the whole word 
    if "_" not in display:
        game_over = True
        print("********************YOU WİN********************")
        
    # Show the current Hangman stage
    print(hangman_art.stages[lives])