import pygame

from ui_controls.clickables import Clickable
from scenes.states import GameScenes
from pygame_loads import load_image
from backgrounds import PAPER_BACKGROUND

exit_scene = Clickable(740, 330, text = None, type_tag='exit_scene')

def render_settings_scene(display_surface, mouse_event, update_scene=None):  
    display_surface.blit(load_image(PAPER_BACKGROUND), (0, 0))

    exit_scene.draw_screen(display_surface)

    if exit_scene.update_state(mouse_event, update_scene):
        GameScenes.in_town, GameScenes.in_settings = True, False

    pygame.display.flip()