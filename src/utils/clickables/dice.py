from utils.clickables.clickables import Clickable
from utils.pygame_loads import load_image, load_sound

DICE_IMG_PATH = "D:/Projects/Python-studies/shop_shop_manager/images/clickables/dice/"
DICE_SOUND_PATH = (
    "D:/Projects/Python-studies/shop_shop_manager/music/sound_effects/rolling_dice.mp3"
)


class Dice(Clickable):
    def __init__(self, x, y, n=1):
        super().__init__(x, y, "", "dice")
        self.dice_images = {
            1: load_image(DICE_IMG_PATH + "1.png"),
            2: load_image(DICE_IMG_PATH + "2.png"),
            3: load_image(DICE_IMG_PATH + "3.png"),
            4: load_image(DICE_IMG_PATH + "4.png"),
            5: load_image(DICE_IMG_PATH + "5.png"),
            6: load_image(DICE_IMG_PATH + "6.png"),
        }
        self.default_image = self.dice_images.get(n, self.dice_images[1])
        self.current_image = self.default_image
        self.click_sound = load_sound(DICE_SOUND_PATH)
        self.rect = self.current_image.get_rect(topleft=(x, y))

    def get_die_face(self) -> int:
        """
        Returns the current die face number.
        """
        for face_number, image in self.dice_images.items():
            if self.current_image == image:
                return face_number
        return -1  # Return -1 if no match is found
