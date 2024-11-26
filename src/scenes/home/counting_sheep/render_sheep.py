import pygame
from typing import Optional, Callable

from .run_sheep import RunSheep
from .bubble import Bubble
from scenes.scene_manager import GameScenes 
from utils.pygame_loads import load_image
from utils.declared_buttons import RETURN
from backgrounds import SHEEP_FIELD


# Constants
current_frame: int = 0  # Current frame index for the sheep animation
frame_counter: int = 0  # Counter to control the speed of the animation
SHEEP_AXIS_X: int = 800  # Starting X position (right edge of the screen)
SHEEP_AXIS_Y: int = 200  # Fixed Y position
SHEEP_VELOCITY: int = -5  # Speed at which the sheep moves left

bubble = Bubble() # Initialize the bubble
sheep = RunSheep(SHEEP_AXIS_X, SHEEP_AXIS_Y, SHEEP_VELOCITY) # Initialize the sheep

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
    sheep.reset_sheep_position()
    sheep.animate_sheep()
    sheep.draw_sheep(display_surface)

    # Update and draw bubble
    # bubble.draw_container(display_surface)
    bubble.update_bubble()
    bubble.draw_bubble(display_surface)

    # Render the exit button
    RETURN.draw_screen(display_surface)
    if RETURN.update_scene(mouse_event, trigger_update):
        GameScenes.in_sheep_mg = False  # End the sheep game