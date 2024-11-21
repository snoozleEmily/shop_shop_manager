import pygame
from typing import Optional, Callable

from scenes.scene_manager import GameScenes
from .sheep_sprite import sheep_sprite, jumping_sheep
from utils.pygame_loads import Screen, load_image
from utils.declared_buttons import RETURN
from backgrounds import SHEEP_FIELD

# Constants
current_frame = 0  # Current frame index for the sheep animation
frame_counter = 0  # Counter to control the speed of the animation
ANIMATION_SPEED = 5 # Number of frames to wait before moving to the next animation frame
SHEEP_AXIS_X = 800  # Starting X position (right edge of the screen)
SHEEP_AXIS_Y = 200  # Fixed Y position
SHEEP_VELOCITY = -5  # Speed at which the sheep moves left


class Sheep:
    """Class to manage sheep animation and movement."""

    def __init__(self, x: int, y: int, velocity: int):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.current_frame = 0
        self.frame_counter = 0
        self.is_jumping = False

    def reset_position(self):
        """Update the sheep's position and reset when it goes off-screen."""
        self.x += self.velocity
        if self.x < -sheep_sprite[0].get_width():
            self.x = Screen.SCREEN_WIDTH * 2

    def animate(self):
        """Animate the sheep by cycling through frames."""
        if not self.is_jumping:  # Only animate when not jumping
            self.frame_counter += 1
            if self.frame_counter >= ANIMATION_SPEED:
                self.current_frame = (self.current_frame + 1) % len(sheep_sprite)
                self.frame_counter = 0

    def draw(self, display_surface: pygame.Surface):
        """Draw the sheep at its current position."""
        if self.is_jumping:
            display_surface.blit(jumping_sheep, (self.x, self.y))
        else:
            display_surface.blit(sheep_sprite[self.current_frame], (self.x, self.y))


# Initialize the sheep
sheep = Sheep(SHEEP_AXIS_X, SHEEP_AXIS_Y, SHEEP_VELOCITY)


def render_sheep(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
):
    """
    Render the sheep game screen, including background, sheep animation, and buttons.
    """
    # Draw the sheep game background
    display_surface.blit(load_image(SHEEP_FIELD), (0, 0))

    # Check for spacebar press to make the sheep jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        sheep.is_jumping = True
    else:
        sheep.is_jumping = False

    # Update and draw sheep
    sheep.reset_position()
    sheep.animate()
    sheep.draw(display_surface)

    # Render the exit button
    RETURN.draw_screen(display_surface)
    if RETURN.update_scene(mouse_event, trigger_update):
        GameScenes.in_sheep_mg = False  # End the sheep game
