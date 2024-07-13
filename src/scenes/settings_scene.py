import pygame
from clickables import *
from scenes.states import GameScenes

exit_scene = Clickable(740, 330, text = None, type_tag='exit_scene')
paper_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\paper_background.png")

def render_settings_scene(display_surface, mouse_event, update_scene=None):  
    display_surface.blit(paper_background_image, (0, 0))

    exit_scene.draw_image(display_surface)

    if exit_scene.update_state(mouse_event, update_scene):
        GameScenes.in_town, GameScenes.in_settings = True, False

    pygame.display.flip()