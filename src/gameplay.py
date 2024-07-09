import pygame
import scenes
from settings import *
from ui_controls import *
from shop_scene import *

# Main game logic/gamyplay here
box = Clickable(10, 350, text = None, type_tag='box')
settings_button = Clickable(770, 7, text = None, type_tag='settings')
town_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\town_background_one.png")

def main_game(display_surface, mouse_event, update_scene=None):  
    if scenes.in_shop:
        update_scene=render_shop_scene
        update_scene(display_surface, mouse_event)

    elif scenes.in_settings:
        update_scene=render_settings_scene
        update_scene(display_surface, mouse_event) 
         
    else:
        display_surface.blit(town_background_image, (0, 0))

        box.draw_image(display_surface)
        settings_button.draw_image(display_surface)
        
        if box.update_state(mouse_event, update_scene):
            scenes.in_shop, scenes.in_town = True, False  # Switch to shop scene
          
        elif settings_button.update_state(mouse_event, update_scene):
            scenes.in_settings, scenes.in_town = True, False  # Switch to settings scene

    # Update display to show the new frame
    pygame.display.flip()