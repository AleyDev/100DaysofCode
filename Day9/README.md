# 🕵️‍♂️ Secret Auction Program

This program simulates a secret auction where multiple participants can place anonymous bids. Once all bids are collected, the program announces the winner with the highest bid. 🎉

## 🛠️ How It Works?

1. **Logo Display**:
   The program starts by showing a logo from the `art.py` file.

2. **Bidding Process**:
   - Users are prompted to enter their **name** and **bid amount**.
   - Each bid is stored in a dictionary with the participant's name as the key and the bid amount as the value.

3. **Check for Additional Bidders**:
   - After each bid, the program asks if there are any additional participants.
   - If yes, the screen is cleared for privacy and the next participant can enter their details. 🧹
   - If no, the program proceeds to determine the winner.

4. **Announcing the Winner**:
   The program finds the highest bid and announces the winner with their bid amount. 🏆

5. **Screen Clearing**:
   The program clears the terminal screen for a smoother user experience.

## 🔍 Code Explanation

### Functions
- **`find_highest_bidder(bidding_dictionary)`**:
  - Iterates through the bids dictionary.
  - Finds the highest bid and the corresponding bidder.
  - Prints the winner's name and bid amount.

- **`clear_screen()`**:
  - Clears the terminal screen by printing multiple blank lines.

### Data Structures
- **`bids`**:
  - A dictionary storing each participant's name as the key and their bid amount as the value.

## 🚀 Example Workflow

1. **Starting the Program**:
   A logo is displayed, and the first participant is prompted to enter their name and bid.

2. **Entering Bids**:
   Participants input their details, and the program asks if there are additional participants.

3. **Determining the Winner**:
   Once all bids are collected, the program announces the winner. 🥳

## ⚙️ Requirements

- Python 3.x
- The `art.py` file containing the logo (optional).

## 💻 How to Run

1. Save the program as `main.py` and ensure the `art.py` file is in the same directory.
2. Run the program using:
   ```bash
   python main.py
