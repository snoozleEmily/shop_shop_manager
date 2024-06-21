import pygame
import os

# Initializing Pygame mixer
pygame.mixer.init()

# Defining the directory containing the playlist
playlist_dir = 'D:\Projects\Python-studies\shop_shop_manager\music\loop_songs'
mp3_files = [os.path.join(playlist_dir, file) for file in os.listdir(playlist_dir) if file.endswith('.mp3')]

def start_music(mp3_files):
    if mp3_files:
        pygame.mixer.music.load(mp3_files[0])
        pygame.mixer.music.set_volume(0.1)  # Set volume to 10%
        pygame.mixer.music.play()
        print(f"Playing {mp3_files[0]}")

def check_current_music(mp3_files):
    if mp3_files and not pygame.mixer.music.get_busy():
        next_song = mp3_files.pop(0) # Removes the first song
        mp3_files.append(next_song)  # Appends the song to the end of the playlist
        pygame.mixer.music.load(mp3_files[0]) # Loads the new first song
        pygame.mixer.music.play() # Plays the new song
        print(f"Playing {mp3_files[0]}")
