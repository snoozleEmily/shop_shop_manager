import pygame

#main game here

town_background_image = pygame.image.load(r"D:/Projects/Python-studies/shop_shop_manager/images/town_background_one.png")

def gameplay(screen):
    # Main game logic here
    
    screen.blit(town_background_image, (0, 0))