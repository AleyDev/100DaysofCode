# 🎮 Hangman Game ✏️💀  

Hangman is a classic word-guessing game where you try to save your character by guessing the correct word. In this Python implementation, you have six lives, and each incorrect guess gets you closer to losing. Test your vocabulary and see if you can beat the Hangman! 🎉  

---

## 📋 How to Play  
1. Run the program, and the game will randomly select a word.  
2. The selected word will be displayed as blanks (`_ _ _`) to show the word's length.  
3. Guess one letter at a time:  
   - If the guessed letter is correct, it will be revealed in the word.  
   - If the guessed letter is incorrect, you lose a life, and the hangman figure begins to form.  
4. End of the game:  
   - Guess the whole word correctly to win! 🎉  
   - Lose all your lives, and the game is over. 💀  

---

## 🛠️ Features  
- **Dynamic Word Selection**: The game randomly selects a word from a predefined list.  
- **Visual Feedback**: Incorrect guesses show the progression of the Hangman figure.  
- **Error Handling**: Prevents duplicate guesses and notifies you if you repeat a letter.  
- **Lives Counter**: Starts with 6 lives and decreases with each wrong guess.  
- **Winning Condition**: Displays a victory message when all letters are guessed correctly.  

---

## ⚙️ Setup and Installation  
1. Clone or download this repository.  
2. Ensure Python 3.x is installed on your system.  
3. Place the `hangman_art.py` and `hangman_words.py` files in the same directory as the main script.  
4. Run the game using your terminal or IDE:  
   ```bash
   python hangman.py

Good Luck!