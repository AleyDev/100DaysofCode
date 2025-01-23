def turn_right():
    # Turn right by turning left three times.
    turn_left()
    turn_left()
    turn_left()
    
def loop():
    # Follow a specific path to overcome the hurdle.
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
number_of_hurdles = 6  # Total number of hurdles to overcome.
while number_of_hurdles > 0:
    while at_goal() == True:
        # Task is complete if the goal is reached.
        done()
    loop()  # Overcome one hurdle.
    number_of_hurdles -= 1  # Decrease the remaining hurdle count.
    print(number_of_hurdles)  # Print the remaining number of hurdles.
