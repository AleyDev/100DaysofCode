"""
    from random import randint
    dice_images = ["1", "2", "3", "4", "5", "6"]
    dice_num = randint(1,6)
    print(dice_images[dice_num])
"""

# Reproduce the Bug
# IndexError: list index out of range

from random import randint
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)  # Change range to 0-5 for valid indices
print(dice_images[dice_num])
