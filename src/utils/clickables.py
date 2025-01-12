import pygame
import time
from typing import Tuple, Optional, Callable


class Clickables:
    # Superclass of Buttons
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
        self.last_click_time = time.perf_counter() - 0.5  # Default click delay

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

    def register_click(self, event: pygame.event.Event, last_click_time: time.perf_counter):
        """
        Check if button was clicked with delay between clicks
        
        Args:
            event (pygame.event.Event): The pygame event to check for a click.

        Returns:
            bool: True if the button was clicked, False otherwise.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            current_time = time.perf_counter()

            if self.enabled and self.rect.collidepoint(pygame.mouse.get_pos()):
                if current_time - self.last_click_time >= 0.5:  # Default click delay
                    self.click_sound.play()
                    self.last_click_time = current_time
                    return True
        return False

    def update_scene(self, event: pygame.event.Event, trigger_update: Optional[Callable]) -> bool:
        """
        Update the state of the clickable object based on the given event and trigger_update function.

        Args:
            event (pygame.event.Event): The pygame event to process.
            trigger_update (Optional[Callable]): Placeholder as default, receives the scenes display fcuntions.

        Returns:
            bool: True if the clickable object was interacted with, False otherwise.
        """
        # Animate hover effect
        hovered = self.is_hovered()
        if self.has_hover and hasattr(self, "hover_image"):
            self.current_image = self.hover_image if hovered else self.default_image

        return self.register_click(event, self.last_click_time)
