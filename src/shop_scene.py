import pygame
from ui_controls import *

def shop_scene(screen):
    shop_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\shop_background.png")
    screen.blit(shop_background_image, (0, 0))

    # Update display to show the new frame
    pygame.display.flip()