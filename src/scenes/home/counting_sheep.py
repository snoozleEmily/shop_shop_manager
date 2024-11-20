import pygame
from typing import Optional, Callable

from scenes.scene_manager import GameScenes
from .sheep_sprite import sheep_sprites, jumping_sheep
from utils.pygame_loads import load_image
from utils.declared_buttons import RETURN
from backgrounds import SHEEP_FIELD

# Global variables for sheep animation and position
current_frame = 0  # Current frame index for the sheep animation
frame_counter = 0  # Counter to control the speed of the animation
animation_speed = 5  # Number of frames to wait before moving to the next animation frame
sheep_axis_x = 800  # Starting X position (right edge of the screen)
sheep_axis_y = 200  # Fixed Y position
sheep_velocity = -5  # Speed at which the sheep moves left


def render_sheep(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
):
    global current_frame, frame_counter, sheep_axis_x

    # Draw the sheep game background
    display_surface.blit(load_image(SHEEP_FIELD), (0, 0))

    # Animate sheep
    frame_counter += 1
    if frame_counter >= animation_speed:
        current_frame = (current_frame + 1) % len(sheep_sprites)
        frame_counter = 0

    # Update sheep position
    sheep_axis_x += sheep_velocity
    if sheep_axis_x < -sheep_sprites[0].get_width():  # If sheep moves off-screen
        sheep_axis_x = 800  # Reset to right side of the screen

    # Draw the sheep
    sheep_position = (sheep_axis_x, sheep_axis_y)
    display_surface.blit(sheep_sprites[current_frame], sheep_position)

    # Render the exit button
    RETURN.draw_screen(display_surface)
    if RETURN.update_scene(mouse_event, trigger_update):
        GameScenes.in_sheep_mg = False  # End the sheep game
