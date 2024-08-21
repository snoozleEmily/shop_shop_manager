import pygame


class VolumeController:
    def __init__(self):
        self.volume = 0.1  # Default volume

    def increase_volume(self):
        if self.volume < 1.0:
            self.volume += 0.1
            pygame.mixer.music.set_volume(self.volume)

    def decrease_volume(self):
        if self.volume > 0.0:
            self.volume -= 0.1
            pygame.mixer.music.set_volume(self.volume)
