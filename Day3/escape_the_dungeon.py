""" Escape the Dungeon 🏰
The player is trapped in a dark and dangerous dungeon and must find a way to escape. Every decision they make will determine their fate—whether they find the way out or fall into a deadly trap.
"""


print('''_________________________________________________________
 /|     -_-                                             _-  |\
/ |_-_- _                                         -_- _-   -| \   
  |                            _-  _--                      | 
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |          
  |   /   |   ()        \      U      /   |    ()       \   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |  
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -        lc \
/   -_- _ -             _- _---                       -_-  -_ \
 ''')
print("Welcome to Escape the Dungeon!")
print("Your goal is to escape the dark and dangerous dungeon alive.\n")

choice1 = input('You wake up in a dark cell. There\'s a door and a window. '
                'What do you choose?\nType "door" or "window":\n').lower()

if choice1 == "door":
    choice2 = input("The door creaks open to reveal two paths. "
                    "One path is lit by torches, and the other is pitch black. "
                    "\nType \"light\" to take the lit path or \"dark\" to take the dark path:\n").lower()
    if choice2 == "light":
        print("You are caught by guards patrolling the lit path. Game Over!")
    elif choice2 == "dark":
        choice3 = input("You stumble through the darkness and find a chest. "
                        "Do you open it?\nType \"yes\" or \"no\":\n").lower()
        if choice3 == "yes":
            print("You find a key inside the chest and escape the dungeon. You win!")
        else:
            print("Without the key, you remain trapped. Game Over!")
    else:
        print("Invalid choice. Game Over!")
elif choice1 == "window":
    print("You climb out of the window and fall into a pit. Game Over!")
else:
    print("Invalid choice. Game Over!")


