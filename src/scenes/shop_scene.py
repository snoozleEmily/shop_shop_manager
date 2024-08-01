import pygame
from typing import Optional, Callable

from ui_controls.clickables import Clickable
from scenes.states import GameScenes
from pygame_loads import load_image
from backgrounds import SHOP_BACKGROUND

EXIT_SCENE = Clickable(740, 330, text = None, type_tag='exit_scene')

def render_shop(display_surface: pygame.Surface, 
                      mouse_event: pygame.event.Event, 
                      update_scene: Optional[Callable] = None) -> None:
    
    display_surface.blit(load_image(SHOP_BACKGROUND), (0, 0)) 
    EXIT_SCENE.draw_screen(display_surface)

    if EXIT_SCENE.update_state(mouse_event, update_scene):
        GameScenes.in_town, GameScenes.in_shop = True, False
                
    pygame.display.flip()
