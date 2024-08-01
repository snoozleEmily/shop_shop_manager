import pygame
from typing import Optional, Callable

from ui_controls.clickables import Clickable
from scenes.states import GameScenes
from pygame_loads import load_image
from backgrounds import INITIAL_BACKGROUND

# Initialize button
pygame.font.init()
button = Clickable(254, 280, "Play Game", type_tag='button')

def handle_game_start(mouse_event: pygame.event.Event) -> bool:
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
        if button.rect.collidepoint(mouse_event.pos):
            GameScenes.in_beginning, GameScenes.in_town = False, True
            return True  # Starts the game 
    return False

def render_initial_screen(display_surface: pygame.Surface, 
                          mouse_event: pygame.event.Event, 
                          update_scene: Optional[Callable] = None) -> None:
    
    button.update_state(mouse_event, update_scene)         
    
    # Draw everything on the screen
    display_surface.blit(load_image(INITIAL_BACKGROUND), (0, 0))
    button.draw_screen(display_surface)   