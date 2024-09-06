import pygame

from .clickables import Clickables
from .pygame_loads import (
    Screen,
    FONT_BUTTON,
    load_image,
    load_sound,
)

# All buttons are declared in declared_buttons.py


BUTTONS_PATH = "D:/Projects/Python-studies/shop_shop_manager/images/ui/buttons/"
DICE_CUP_PATH = "D:/Projects/Python-studies/shop_shop_manager/images/ui/dice/"
SOUND_EFFECTS_PATH = "D:/Projects/Python-studies/shop_shop_manager/music/sound_effects/"


class Button(Clickables):
    checkbox_toggle = False

    def __init__(self, x, y, text, type_tag):
        super().__init__(x, y, text, type_tag)

        if type_tag in [
            "caption_btn",
            "checkbox_off",
            "checkbox_on",
            "exit",
            "dice_cup",
        ]:
            self.has_hover = True
            # In order for the hover effect to work, the new button
            # must be added to the 'buttons_in_scene' dictionary
            # in the trigger_hover.py file

        # Long button with text (e.g. "Play Game")
        if type_tag == "caption_btn":
            self.default_image = load_image(BUTTONS_PATH + "button_image.png")
            self.hover_image = load_image(BUTTONS_PATH + "button_image_hover.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "button_click.mp3")
            self.font = FONT_BUTTON
            self.text_surface = self.font.render(text, True, (255, 255, 255))

        # Door at the right top corner
        elif type_tag == "exit":
            self.default_image = load_image(BUTTONS_PATH + "exit_default_btn.png")
            self.hover_image = load_image(BUTTONS_PATH + "exit_hover_btn.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "exit_scene_click.mp3")

        # Box that leads to scenes or has some action (in settings)
        elif type_tag == "default":
            self.default_image = load_image(BUTTONS_PATH + "default_btn.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "default_click.mp3")

        # Checkbox in the settings
        elif type_tag == "checkbox_off":
            self.default_image = load_image(BUTTONS_PATH + "unchecked_default_btn.png")
            self.hover_image = load_image(BUTTONS_PATH + "unchecked_hover_btn.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "default_click.mp3")

        elif type_tag == "checkbox_on":
            self.default_image = load_image(BUTTONS_PATH + "checked_default_btn.png")
            self.hover_image = load_image(BUTTONS_PATH + "checked_hover_btn.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "default_click.mp3")

        # Engine at the left top corner
        elif type_tag == "settings":
            self.default_image = load_image(BUTTONS_PATH + "settings_default.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "settings_click.mp3")

        # To start the dice minigame in tavren
        elif type_tag == "dice_cup":
            self.default_image = load_image(DICE_CUP_PATH + "dice_cup.png")
            self.hover_image = load_image(DICE_CUP_PATH + "rolling_dice_cup.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "rolling_dice.mp3")

        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))

        # If the button is a checkbox, update the checkbox_toggled state
        if type_tag == "checkbox_off" or type_tag == "checkbox_on":
            Button.checkbox_toggle = type_tag == "checkbox_on"
            self.update_checkbox()

    def update_checkbox(self):
        """Update the checkbox image based on the checkbox_toggled state."""
        if Button.checkbox_toggle:
            self.default_image = load_image(BUTTONS_PATH + "checked_default_btn.png")
            self.hover_image = load_image(BUTTONS_PATH + "checked_hover_btn.png")
        else:
            self.default_image = load_image(BUTTONS_PATH + "unchecked_default_btn.png")
            self.hover_image = load_image(BUTTONS_PATH + "unchecked_hover_btn.png")

    def draw_screen(self, surface: pygame.Surface):
        # Update the checkbox image if the button is a checkbox
        if self.type_tag in ["checkbox_off", "checkbox_on"]:
            self.update_checkbox()

        # Sets exit button default as black
        if self.type_tag == "exit":
            self.default_image = load_image(BUTTONS_PATH + "exit_default_btn.png")
            self.hover_image = load_image(BUTTONS_PATH + "exit_hover_btn.png")

        # Makes exit button white
        if Screen.is_too_dark:
            if self.type_tag == "exit":
                self.default_image = load_image(BUTTONS_PATH + "exit_white_btn.png")
                self.hover_image = load_image(BUTTONS_PATH + "exit_hover_white_btn.png")
                Screen.is_too_dark = False

        # Draws the button image and text on the screen
        super().draw_screen(surface)
        if self.type_tag == "caption_btn":
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            surface.blit(self.text_surface, text_rect)
