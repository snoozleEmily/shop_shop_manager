import pygame
from clickables import *
from scenes.settings_scene import *
from scenes.shop_scene import * 
from scenes.states import GameScenes

box = Clickable(10, 350, text = None, type_tag='box')
settings_button = Clickable(770, 7, text = None, type_tag='settings')
town_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\town_background_one.png")

def main_game(display_surface, mouse_event, update_scene=None):  
    if GameScenes.in_shop:
        update_scene=render_shop_scene
        update_scene(display_surface, mouse_event)

    elif GameScenes.in_settings:
        update_scene=render_settings_scene
        update_scene(display_surface, mouse_event) 
         
    else:
        display_surface.blit(town_background_image, (0, 0))

        box.draw_image(display_surface)
        settings_button.draw_image(display_surface)
        
        # Switch to shop scene
        if box.update_state(mouse_event, update_scene):
            GameScenes.in_shop, GameScenes.in_town = True, False  
          
        # Switch to settings scene
        elif settings_button.update_state(mouse_event, update_scene):
            GameScenes.in_settings, GameScenes.in_town = True, False  

    # Update display to show the new frame
    pygame.display.flip()