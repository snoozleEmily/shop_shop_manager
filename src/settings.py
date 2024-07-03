import pygame
from ui_controls import *

paper_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\paper_background.png")

def render_settings_screen(display_surface):  
    display_surface.blit(paper_background_image, (0, 0))

    pygame.display.flip()