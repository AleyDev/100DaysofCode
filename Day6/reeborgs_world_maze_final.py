def turn_right():
    turn_left()
    turn_left()
    turn_left()

def wall():
    # Move forward until encountering a wall
    while front_is_clear():
        move()
    turn_left()  # Turn left to navigate around the wall
    
    while not at_goal():  # Continue navigating until the goal is reached
        if right_is_clear():  # Prioritize turning right if possible
            turn_right()
            move()
        elif wall_in_front():  # If there's a wall ahead, turn left
            turn_left()
        elif not right_is_clear():  # If right is not clear, move forward
            move()          
        elif front_is_clear() and right_is_clear():  # Handle open paths
            turn_right()

# Start navigating
wall()
