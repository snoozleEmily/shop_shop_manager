import pygame
from clickables import *
from scenes.market_board import render_table
from scenes.states import GameScenes

exit_scene = Clickable(740, 330, text = None, type_tag='exit_scene')
shop_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\shop_background.png")

def render_shop_scene(display_surface, mouse_event, update_scene=None):
    display_surface.blit(shop_background_image, (0, 0))

    render_table(display_surface)
    
    exit_scene.draw_image(display_surface)

    if exit_scene.update_state(mouse_event, update_scene):
        GameScenes.in_town, GameScenes.in_shop = True, False
                
    pygame.display.flip()