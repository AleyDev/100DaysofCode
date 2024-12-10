year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a  millennial.")
elif year > 1994:
    print("You are a Gen Z.")
    
    
# Play Computer and Evaluate Each Line
# The user inputs a year: 1994.

"""
year = int(input("What's your year of birth? "))  # The user inputs a year 1994. The value is converted to an integer and stored in the variable `year`.

# Step 1: Check the first condition.
if year > 1980 and year < 1994:  # The computer checks if both conditions are True:
    # - `year > 1980`: This is True because 1994 > 1980.
    # - `year < 1994`: This is False because 1994 is not less than 1994.
    # Since the `and` operator requires both conditions to be True, this entire condition is False.
    print("You are a millennial.")  # This line is skipped because the condition is False.

# Step 2: Check the second condition.
elif year > 1994:  # The computer now checks if the year is greater than 1994.
    # - `year > 1994`: This is False because 1994 is not greater than 1994.
    # Since the condition is False, the code inside this block is also skipped.
    print("You are a Gen Z.")  # This line is not executed.

# Step 3: No conditions are True.
# Since neither the `if` nor the `elif` condition is True, the computer does nothing further.
# As a result, no output is produced when the input is 1994.
"""



##  This is called "thinking like a computer." ☺