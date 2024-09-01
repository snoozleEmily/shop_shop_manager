import pygame

from utils.clickables.clickables import Clickable
from utils.pygame_loads import FONT_BUTTON, load_image, load_sound

BUTTONS_PATH = "D:/Projects/Python-studies/shop_shop_manager/images/clickables/buttons/"
SOUND_EFFECTS_PATH = "D:/Projects/Python-studies/shop_shop_manager/music/sound_effects/"


class Button(Clickable):
    def __init__(self, x, y, text, type_tag):
        super().__init__(x, y, text, type_tag)

        if type_tag in ["caption_btn", "exit_scene"]:
            self.has_hover = True

        # Long button with text (e.g. "Play Game")
        if type_tag == "caption_btn":
            self.default_image = load_image(BUTTONS_PATH + "button_image.png")
            self.hover_image = load_image(BUTTONS_PATH + "button_image_hover.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "button_click.mp3")
            self.font = FONT_BUTTON
            self.text_surface = self.font.render(text, True, (255, 255, 255))

        # Door at the right top corner
        elif type_tag == "exit_scene":
            self.default_image = load_image(
                BUTTONS_PATH + "exit_scene_default_image.png"
            )
            self.hover_image = load_image(BUTTONS_PATH + "exit_scene_hover_image.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "exit_scene_click.mp3")

        # Box that leads to scenes or has some action (in settings)
        elif type_tag == "default":
            self.default_image = load_image(BUTTONS_PATH + "default.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "default_click.mp3")

        # Engine at the left top corner
        elif type_tag == "settings":
            self.default_image = load_image(BUTTONS_PATH + "settings_default.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "settings_click.mp3")

        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))

    def draw_screen(self, surface: pygame.Surface):
        # Draws the button image and text on the screen
        super().draw_screen(surface)
        if self.type_tag == "caption_btn":
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            surface.blit(self.text_surface, text_rect)
