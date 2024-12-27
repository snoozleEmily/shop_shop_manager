import pygame
from typing import Optional, Callable

from .run_sheep import RunSheep
from .cloud import Cloud
from scenes.scene_manager import GameScenes 
from utils.pygame_loads import load_image
from utils.declared_buttons import RETURN
from backgrounds import SHEEP_FIELD


# Constants
current_frame: int = 0  # Current frame index for the sheep animation
frame_counter: int = 0  # Counter to control the speed of the animation
SHEEP_AXIS_X: int = 800  # Starting X position (right edge of the screen)
SHEEP_INIT_AXIS_Y: int = 200  # Fixed Y position
SHEEP_VELOCITY: int = -5  # Speed at which the sheep moves left

cloud = Cloud() # Initialize the bubble
sheep = RunSheep(SHEEP_AXIS_X, SHEEP_INIT_AXIS_Y, SHEEP_VELOCITY) # Initialize the sheep

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

    # Check for click to make the sheep jump
    if cloud.kill_cloud(mouse_event):
        sheep.is_jumping = True
        sheep.jump_timer = pygame.time.get_ticks()  # Set the jump timer to the current time

    # Check if the jump duration has passed
    if sheep.is_jumping and pygame.time.get_ticks() - sheep.jump_timer >= 1000:
        sheep.is_jumping = False

    # Update and draw sheep
    sheep.reset_sheep_position()
    sheep.animate_sheep()
    sheep.draw_sheep(display_surface)

    # Update and draw bubble
    # bubble.draw_container(display_surface) #  See container for debugging
    cloud.update_cloud()
    cloud.draw_cloud(display_surface)

    # Render the return button
    #RETURN.draw_screen(display_surface)
    if RETURN.update_scene(mouse_event, trigger_update):
        GameScenes.in_sheep_mg = False  # End the sheep game