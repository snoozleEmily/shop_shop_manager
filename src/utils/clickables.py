import pygame
import time
from typing import Callable, Tuple

from .pygame_loads import FONT_BUTTON, load_image, load_sound

IMAGES_PATH = "D:/Projects/Python-studies/shop_shop_manager/images/clickables/"
SOUND_EFFECTS_PATH = "D:/Projects/Python-studies/shop_shop_manager/music/sound_effects/"


class Clickable:
    def __init__(self, x, y, text, type_tag):
        """
        Initializes a clickable object with its position, type, and specific attributes

        Args:
        x and y (int): X and y coordinates positions on the screen
        text (str): Text displayed on the clickable object (e.g. 'button' type)
        identifier_type (str): Type of clickable object (e.g. 'button', 'exit_scene', 'settings')
        """
        self.x = x
        self.y = y
        self.text = text
        self.identifier_type = type_tag

        self.current_frame_index = 0
        self.last_frame_time = time.time()
        self.click_delay = {
            "button": 0.5,
            "exit_scene": 1,
            "box": 0.8,
            "settings": 1.5,
        }.get(type_tag, 0.5)

        self.enabled, self.toggled, self.toggle_count = True, False, 0
        self.has_hover = False

        if type_tag in ["button", "exit_scene"]:
            self.has_hover = True

        if type_tag == "button":
            self.default_image = load_image(IMAGES_PATH + "button_image.png")
            self.hover_image = load_image(IMAGES_PATH + "button_image_hover.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "button_click.mp3")
            self.font = FONT_BUTTON
            self.text_surface = self.font.render(text, True, (255, 255, 255))

        elif type_tag == "exit_scene":
            self.default_image = load_image(
                IMAGES_PATH + "exit_scene_default_image.png"
            )
            self.hover_image = load_image(IMAGES_PATH + "exit_scene_hover_image.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "exit_scene_click.mp3")

        elif type_tag == "box":
            self.default_image = load_image(IMAGES_PATH + "box.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "box_click.mp3")

        elif type_tag == "settings":
            self.default_image = load_image(IMAGES_PATH + "settings_default.png")
            self.click_sound = load_sound(SOUND_EFFECTS_PATH + "settings_click.mp3")

        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))

        # Allow immediate first click
        self.last_click_time = time.time() - self.click_delay

    def is_hovered(self) -> bool:
        """
        Checks if the mouse is hovering over the clickable object.

        Returns:
            bool: True if the mouse is hovering over the clickable object, False otherwise.
        """
        mouse_position: Tuple[int, int] = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position)

    def draw_screen(self, surface: pygame.Surface) -> None:
        """
        Draws the current image of the clickable object on the screen.
        """
        surface.blit(self.current_image, self.rect.topleft)

        if self.identifier_type == "button":
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            surface.blit(self.text_surface, text_rect)

    def update_scene(
        self, event: pygame.event.Event, trigger_update: Callable[[], None]
    ) -> bool:
        """
        Updates the state of the clickable object based on the given event and trigger_update function.
        """
        hovered = self.is_hovered()

        # Only update the image if hover state changes and hover_image exists
        if hovered != self.has_hover and hasattr(self, "hover_image"):
            self.current_image = self.hover_image if hovered else self.default_image
            self.has_hover = hovered

        # Adds a delay to the sound effect
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            current_time = time.time()

            # Check for mouse click
            if self.enabled and self.rect.collidepoint(pygame.mouse.get_pos()):
                # Ensure delay between clicks
                if current_time - self.last_click_time >= self.click_delay:
                    self.click_sound.play()
                    self.last_click_time = current_time

                    # Signal that the button was clicked
                    return True
        return False
