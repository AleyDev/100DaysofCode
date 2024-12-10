"""
number = int(input("Which number do you want to check? "))

if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
"""

# Debugging Odd or Even
# Spot the problems 🐞. - Modify the code to fix the program. Fix the code so that it works and passes the tests when you submit.

def odd_or_even(number):
    if number % 2 == 0: # ==
        return "This is an even number."
    else:
        return "This is an odd number."