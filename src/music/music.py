import pygame
import os

# The button sounds are in the declared in the Clickables class

pygame.mixer.init()

PLAYLIST_DIR = "D:\\Projects\\Python-studies\\shop_shop_manager\\music\\loop_songs"


class SongsPath:
    def __init__(self):
        self.mp3_files = mp3_files = [
            os.path.join(PLAYLIST_DIR, file)
            for file in os.listdir(PLAYLIST_DIR)
            if file.endswith(".mp3")
        ]
        self.previous_song = None
        self.is_first_song = False  # First song only plays once

    @staticmethod
    def start_music(path):
        if path.mp3_files:
            pygame.mixer.music.load(path.mp3_files[0])
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()

    @staticmethod
    def check_current_music(path):
        if path.mp3_files and not pygame.mixer.music.get_busy():
            # Save the current song as the previous song
            if path.previous_song is not None:
                path.previous_song = path.mp3_files[0]

            next_song = path.mp3_files.pop(0)
            if not path.is_first_song:
                path.is_first_song = True  # Mark the first song as played
            else:
                # Move the current song to the end of the playlist
                path.mp3_files.append(next_song)

            pygame.mixer.music.load(path.mp3_files[0])
            pygame.mixer.music.play()


# I want to play the first song only once
