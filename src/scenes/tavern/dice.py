import random

from utils.pygame_loads import load_image

DICE_IMG_PATH = "D:/Projects/Python-studies/shop_shop_manager/images/ui/dice/"


class Dice:
    # The cup with the dice is in Button class
    def __init__(self, n=1):
        self.dice_images = {
            i: (DICE_IMG_PATH + f"{i}.png", load_image(DICE_IMG_PATH + f"{i}.png"))
            for i in range(1, 7)
        }
        self.default_image = self.dice_images.get(n, self.dice_images[1])[1]
        self.current_image = self.default_image

    def roll(self):
        """Rolls the dice, updates the current face image, and returns its path."""
        face_number = random.randint(1, 6)
        self.current_image = self.dice_images[face_number][1]
        return self.dice_images[face_number][0]
