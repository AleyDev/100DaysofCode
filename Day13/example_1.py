"""
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
            
my_function()
"""

# Describe the Problem - Write your asnwers as comments: 
# 1. What is the for loop doing?
# 2. When is the function mean to print "You got it"?
# 3. What are your assumptions about the value of it?


"""
def my_function():
    for i in range(1, 20):  # 1. The for loop iterates through numbers from 1 to 19 (inclusive).
        if i == 20:  # 2. The function is meant to print "You got it" when the value of `i` is 20.
            print("You got it")
my_function()

# 3. Assumptions:
# - The loop does not include 20 in its range because `range(1, 20)` generates numbers from 1 to 19.
# - Therefore, the condition `i == 20` is never met, and the message "You got it" will not be printed.

"""


def my_function():
    for i in range(1, 21):  # Change the range to include 20.
        if i == 20:
            print("You got it")

my_function()