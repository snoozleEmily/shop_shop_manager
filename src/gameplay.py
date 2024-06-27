import pygame
import scenes
from ui_controls import *
from shop_scene import *

# Main game logic/gamyplay here
box = Clickable(10, 350, text = None, identifier_type='box')
town_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\town_background_one.png")

def main_game(screen, event, update_scene=shop_scene):    
    if scenes.in_shop:
        update_scene(screen, event)
    else:
        screen.blit(town_background_image, (0, 0))
        box.draw_image(screen)
        
        # Handle box click event   
        if box.update_state(event, update_scene):
            scenes.in_shop = True  # Switch to shop scene

    # Update display to show the new frame
    pygame.display.flip()
