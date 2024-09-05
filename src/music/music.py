import pygame
import os

pygame.mixer.init()

PLAYLIST_DIR = "D:\\Projects\\Python-studies\\shop_shop_manager\\music\\loop_songs"
mp3_files = [
    os.path.join(PLAYLIST_DIR, file)
    for file in os.listdir(PLAYLIST_DIR)
    if file.endswith(".mp3")
]


def start_music(mp3_files):
    if mp3_files:
        pygame.mixer.music.load(mp3_files[0])
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()


def check_current_music(mp3_files):
    if mp3_files and not pygame.mixer.music.get_busy():

        next_song = mp3_files.pop(0)
        mp3_files.append(next_song)
        pygame.mixer.music.load(mp3_files[0])
        pygame.mixer.music.play()
