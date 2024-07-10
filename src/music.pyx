# cython: language_level=3

cimport cython
import pygame
import os

pygame.mixer.init()

PLAYLIST_DIR  = 'D:\\Projects\\Python-studies\\shop_shop_manager\\music\\loop_songs'
MP3_FILES = [os.path.join(PLAYLIST_DIR, file) for file in os.listdir(PLAYLIST_DIR) if file.endswith('.mp3')]

@cython.boundscheck(False)
@cython.wraparound(False)
def start_music(list MP3_FILES):
    if MP3_FILES:
        pygame.mixer.music.load(MP3_FILES[0])
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

@cython.boundscheck(False)
@cython.wraparound(False)
def check_current_music(list MP3_FILES):
    if MP3_FILES and not pygame.mixer.music.get_busy():
        next_song = MP3_FILES.pop(0)
        MP3_FILES.append(next_song)
        pygame.mixer.music.load(MP3_FILES[0])
        pygame.mixer.music.play()
