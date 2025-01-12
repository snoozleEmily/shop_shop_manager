import pygame

from .clickables import Clickables
from .pygame_loads import (
    FONT_BUTTON,
    load_image,
    load_sound,
)

# All buttons are declared in declared_buttons.py


COINS_PATH = r"D:\\Projects\\Python-studies\\shop_shop_manager\\images\\ui\\other\\coins.png"
SOUND_EFFECTS_PATH = r"D:/Projects/Python-studies/shop_shop_manager/music/sound_effects/"


class Interactables(Clickables):
    def __init__(self, x, y, text, type_tag):
        super().__init__(x, y, text, type_tag)
        
        # type_tag = "coin" Do I need this here?
        # Should I add more Interactables?
        
        self.default_image = load_image(COINS_PATH)
        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))  # Add rect initialization
        self.click_sound = load_sound(SOUND_EFFECTS_PATH + "coin.mp3")
        self.font = FONT_BUTTON
        self.text_surface = self.font.render(text, True, (255, 255, 255))

    def draw_screen(self, surface: pygame.Surface):
        super().draw_screen(surface)
        
    def animate(self, event: pygame.event.Event) -> bool:
        
        return self.register_click(event, 1)
