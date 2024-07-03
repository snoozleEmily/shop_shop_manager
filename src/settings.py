import pygame
from ui_controls import *

paper_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\paper_background.png")

def render_settings_screen(screen):
    screen.blit(paper_background_image, (0, 0))

    # Update display to show the new frame
    pygame.display.flip()