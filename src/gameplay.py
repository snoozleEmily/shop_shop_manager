import pygame
from ui_controls import *

#main game here

town_background_image = pygame.image.load(r"D:/Projects/Python-studies/shop_shop_manager/images/town_background_one.png")

def main_game(screen, event):
    # Main game logic here
    screen.blit(town_background_image, (0, 0))

    box = Box(10, 350, None)
    box.box_draw(screen)

    # Update display to show the new frame
    pygame.display.flip()