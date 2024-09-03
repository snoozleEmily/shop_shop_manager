import random

from utils.pygame_loads import load_image

DICE_IMG_PATH = "D:/Projects/Python-studies/shop_shop_manager/images/ui/dice/"


class Dice:
    die_face = None
    minigame_active = False

    # The rolling cup (with the dice in it) is in the Button class
    def __init__(self, n=1):
        self.dice_images = {
            # Iterate through numbers 1 to 6 (representing dice faces)
            i: (
                # Construct the file path for the dice face image
                DICE_IMG_PATH + f"{i}.png",
                # Load the image from the file path
                load_image(DICE_IMG_PATH + f"{i}.png"),
            )
            # Create a dictionary entry for each dice face number
            for i in range(1, 7)
        }

        # Set the default image, using 'n' or face '1' if 'n' is invalid
        self.default_image = self.dice_images.get(n, self.dice_images[1])[1]
        self.current_image = self.default_image

    def roll(self):
        """Rolls the dice, updates the current face image, and returns its path."""
        face_number = random.randint(1, 6)
        self.current_image = self.dice_images[face_number][1]
        new_face_path = self.dice_images[face_number][0]
        return new_face_path
