import pygame
from ui_controls import *
from shop_scene import *

# Main game logic/gamyplay here
pygame.mixer.init()
box = Clickable(10, 350, item_or_text = None, is_text=False)
town_background_image = pygame.image.load(r"D:/Projects/Python-studies/shop_shop_manager/images/town_background_one.png")

# Define game scenes
in_shop = False

def main_game(screen, event, update_scene=shop_scene):
    global in_shop  # Ensure we can modify the global state
    
    if in_shop:
        update_scene(screen)
    else:
        screen.blit(town_background_image, (0, 0))
        box.draw_image(screen)
        
        # Handle box click event   
        if box.update_state(event, update_scene):
            in_shop = True  # Switch to shop scene

    # Update display to show the new frame
    pygame.display.flip()
