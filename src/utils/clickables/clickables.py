import pygame
import time
from typing import Tuple


class Clickable:
    # Parent class of buttons and dice classes
    def __init__(self, x, y, text, type_tag):
        """
        Initializes a clickable object with its position, type, and specific attributes.

        Args:
        x and y (int): X and y coordinates positions on the screen.
        text (str): Text displayed on the clickable object.
        type_tag (str): Type of clickable object (e.g., 'exit_scene').
        """
        self.x = x
        self.y = y
        self.text = text
        self.type_tag = type_tag

        self.enabled = True
        self.has_hover = False
        self.last_click_time = time.time() - 0.5  # Default click delay

    def draw_screen(self, surface: pygame.Surface) -> None:
        """
        Draws the current image of the clickable object on the screen.
        """
        surface.blit(self.current_image, self.rect.topleft)

    def is_hovered(self) -> bool:
        """
        Checks if the mouse is hovering over the clickable object.

        Returns:
            bool: True if the mouse is hovering over the clickable object, False otherwise.
        """
        mouse_position: Tuple[int, int] = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position)

    def update_scene(self, event: pygame.event.Event, trigger_update: None) -> bool:
        """
        Updates the state of the clickable object based on the given event and trigger_update function.
        """
        hovered = self.is_hovered()

        if self.has_hover and hasattr(self, "hover_image"):
            self.current_image = self.hover_image if hovered else self.default_image

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            current_time = time.time()

            if self.enabled and self.rect.collidepoint(pygame.mouse.get_pos()):
                if current_time - self.last_click_time >= 0.5:  # Default click delay
                    self.click_sound.play()
                    self.last_click_time = current_time
                    return True
        return False
