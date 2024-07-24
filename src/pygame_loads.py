import pygame

pygame.mixer.init()

def load_image(image_path):
    return pygame.image.load(image_path)

def load_sound(sound_path):
    return pygame.mixer.Sound(sound_path)