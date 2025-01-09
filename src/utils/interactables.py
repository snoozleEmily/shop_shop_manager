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

        # Long button with text (e.g. "Play Game")
        self.default_image = load_image(COINS_PATH)
        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))  # Add rect initialization
        self.click_sound = load_sound(SOUND_EFFECTS_PATH + "coin.mp3")
        self.font = FONT_BUTTON
        self.text_surface = self.font.render(text, True, (255, 255, 255))

    def draw_screen(self, surface: pygame.Surface):
        super().draw_screen(surface)
        
    def update_scene(self, event: pygame.event.Event, trigger_update: None) -> bool:
        """
        Override Clickables.update_scene to add coin sound effect on click.
        
        Args:
            event (pygame.event.Event): The event to process
            trigger_update (None): Trigger function for scene updates
            
        Returns:
            bool: True if click was processed, False otherwise
        """
        if super().update_scene(event, trigger_update):
            self.click_sound.play()
            return True
        return False
