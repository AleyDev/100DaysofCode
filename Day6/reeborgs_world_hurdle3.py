# Turn right by turning left three times
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Navigate around a wall
def wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
     
while not at_goal():
    if wall_in_front():  # Check if there's a wall in front.
        wall()           # Navigate around the wall.
    else:
        move()           # Move forward if no wall is present.