import pygame
from ui_controls.clickables import Clickable
from scenes.states import GameScenes
from scenes.settings_scene import render_settings_scene
from scenes.shop_scene import render_shop_scene 

town_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\town_background_one.png")

shop_button = Clickable(10, 350, text = None, type_tag='box')
iventory_button = Clickable(63, 350, text = None, type_tag='box')
home_button = Clickable(116, 350, text = None, type_tag='box')
settings_button = Clickable(767, 5, text = None, type_tag='settings')

def main_game(display_surface, mouse_event, update_scene=None):  
    if GameScenes.in_shop:
        update_scene=render_shop_scene
        update_scene(display_surface, mouse_event)

    elif GameScenes.in_settings:
        update_scene=render_settings_scene
        update_scene(display_surface, mouse_event) 
         
    else:
        display_surface.blit(town_background_image, (0, 0))

        shop_button.draw_image(display_surface)
        iventory_button.draw_image(display_surface)
        home_button.draw_image(display_surface)
        settings_button.draw_image(display_surface)
        
        # Switch to shop scene
        if shop_button.update_state(mouse_event, update_scene):
            GameScenes.in_shop, GameScenes.in_town = True, False  
          
        # Switch to settings scene
        elif settings_button.update_state(mouse_event, update_scene):
            GameScenes.in_settings, GameScenes.in_town = True, False


    pygame.display.flip()