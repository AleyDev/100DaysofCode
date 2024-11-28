def turn_right():
    turn_left()
    turn_left()
    turn_left()

def variable_jump():
    turn_left()
    # Move up until there's no wall on the right
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    # Descend until reaching the ground
    while front_is_clear():
        move()
    # Turn left only if the goal has not been reached
    if not at_goal():
        turn_left()

while not at_goal():
    # Move forward until a wall is encountered
    while front_is_clear():
        move()
    # Jump over the encountered wall
    variable_jump()
