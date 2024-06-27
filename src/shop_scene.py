import pygame
import scenes
from ui_controls import *

exit_scene = Clickable(740, 330, text = None, identifier_type='exit_scene')
shop_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\shop_background.png")

def shop_scene(screen, event, update_scene=None):

    screen.blit(shop_background_image, (0, 0))
    
    exit_scene.draw_image(screen)

    # Handle exit_scene click event
    if exit_scene.update_state(event, update_scene):
        scenes.in_town = True  
        scenes.in_shop = False
        
    # Update display to show the new frame
    pygame.display.flip()