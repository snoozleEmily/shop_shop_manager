import pygame
from typing import Optional, Callable

from scenes.scene_manager import GameScenes
from .sheep_sprite import sheep_sprites, jumping_sheep
from utils.pygame_loads import load_image
from utils.declared_buttons import RETURN
from backgrounds import SHEEP_FIELD


class CountingSheep:
    # Do I really need this class?????
    grow_dark = False


current_frame = 0
frame_counter = 0
animation_speed = 5


def render_sheep(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
):
    global current_frame, frame_counter
    # Draw the sheep game background
    display_surface.blit(load_image(SHEEP_FIELD), (0, 0))
    
    # Animate sheep
    frame_counter += 1
    if frame_counter >= animation_speed:
        current_frame = (current_frame + 1) % len(sheep_sprites)
        frame_counter = 0
    sheep_position = (300, 200)
    display_surface.blit(sheep_sprites[current_frame], sheep_position)
    
    # Render the exit button
    RETURN.draw_screen(display_surface)
    if RETURN.update_scene(mouse_event, trigger_update):
        GameScenes.in_sheep_mg = False  # End the sheep game


# TODO: Add the jumping_sheep for when I click spacebar
# TODO: Make the sheep image a bit smaller
# TODO: Make the sheep move from the right to the left
# TODO: Add the fance as an obstacle and when
# I don't click spacebar, the sheep disappears (puff - like in a dream) 
# For each successful jump, I gain a point