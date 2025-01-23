age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
    
""" 
age = int(input("How old are you? "))  
# If the user enters "twelve" (a string), the `int()` function will fail to convert it to an integer.
# This will raise a `ValueError` because "twelve" is not a valid numeric input.
if age > 18:
    print(f"You can drive at age {age}.")
"""  

# Fixing Errors and Watching for Red Underlines

try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

