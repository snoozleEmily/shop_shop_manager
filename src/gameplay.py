import pygame

from ui_controls.clickables import Clickable
from scenes.states import GameScenes
from scenes.settings.settings_scene import render_settings
from scenes.shop_scene import render_shop 
from scenes.inventory_scene import render_inventory
from pygame_loads import load_image
from backgrounds import TOWN_BACKGROUND

SHOP_BUTTON = Clickable(10, 350, text = None, type_tag='box')
IVENTORY_BUTTON = Clickable(63, 350, text = None, type_tag='box')
HOME_BUTTON = Clickable(116, 350, text = None, type_tag='box')
SETTINGS_BUTTON = Clickable(767, 5, text = None, type_tag='settings')

def main_game(display_surface, mouse_event, update_scene=None):  
    if GameScenes.in_shop:
        update_scene=render_shop
        update_scene(display_surface, mouse_event)

    elif GameScenes.in_settings:
        update_scene=render_settings
        update_scene(display_surface, mouse_event)
        
    elif GameScenes.in_inventory:
        update_scene=render_inventory 
        update_scene(display_surface, mouse_event)
         
    else:
        display_surface.blit(load_image(TOWN_BACKGROUND), (0, 0))

        SHOP_BUTTON.draw_screen(display_surface)
        IVENTORY_BUTTON.draw_screen(display_surface)
        HOME_BUTTON.draw_screen(display_surface)
        SETTINGS_BUTTON.draw_screen(display_surface)
        
        # Switch to shop scene
        if SHOP_BUTTON.update_state(mouse_event, update_scene):
            GameScenes.in_shop, GameScenes.in_town = True, False  
        
        # Switch to inventory scene
        elif IVENTORY_BUTTON.update_state(mouse_event, update_scene):
            GameScenes.in_inventory, GameScenes.in_town = True, False
          
        # Switch to settings scene
        elif SETTINGS_BUTTON.update_state(mouse_event, update_scene):
            GameScenes.in_settings, GameScenes.in_town = True, False


    pygame.display.flip()