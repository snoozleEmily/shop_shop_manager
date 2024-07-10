# cython: language_level=3

cimport cython
import pygame
import os

pygame.mixer.init()

playlist_dir = 'D:\\Projects\\Python-studies\\shop_shop_manager\\music\\loop_songs'
mp3_files = [os.path.join(playlist_dir, file) for file in os.listdir(playlist_dir) if file.endswith('.mp3')]

@cython.boundscheck(False)
@cython.wraparound(False)
def start_music(list mp3_files):
    if mp3_files:
        pygame.mixer.music.load(mp3_files[0])
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

@cython.boundscheck(False)
@cython.wraparound(False)
def check_current_music(list mp3_files):
    if mp3_files and not pygame.mixer.music.get_busy():
        next_song = mp3_files.pop(0)
        mp3_files.append(next_song)
        pygame.mixer.music.load(mp3_files[0])
        pygame.mixer.music.play()
