import pygame

pygame.mixer.init()


def load_image(image_path: str) -> pygame.Surface:
    return pygame.image.load(image_path)


def load_sound(sound_path: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(sound_path)
