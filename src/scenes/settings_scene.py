import pygame
import pyperclip 


from scenes.scene_manager import GameScenes
from music.sound_controller import SoundController
from utils.buttons import Button
from utils.pygame_loads import load_image
from backgrounds import PAPER_IMG
from utils.declared_buttons import (
    MUSIC_TOGGLE,
    SOUND_UP,
    SOUND_DOWN,
    NEXT_SONG,
    PREVIOUS_SONG,
    SEE_LEADERBOARD,
    ABOUT_INFO,
    SUPPORT,
    EXIT_SCENE,
)


volume_controller = SoundController()

def render_text(display_surface, text, position, font, color=(0, 0, 0)):
    text_surface = font.render(text, True, color)
    display_surface.blit(text_surface, position)

def render_copy_icon(display_surface, position, icon_size=(20, 20)):
    icon = pygame.Surface(icon_size)
    icon.fill((200, 200, 200))  # Simple gray square as an icon
    display_surface.blit(icon, position)
    return pygame.Rect(position, icon_size)

def handle_copy_icon_click(mouse_event, copy_icon_rect, text_to_copy):
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and copy_icon_rect.collidepoint(mouse_event.pos):
        pyperclip.copy(text_to_copy)
        print(f"Copied to clipboard: {text_to_copy}")


def render_settings(display_surface, mouse_event, trigger_update=None) -> None:
    display_surface.blit(load_image(PAPER_IMG), (0, 0))

    MUSIC_TOGGLE.draw_screen(display_surface)
    NEXT_SONG.draw_screen(display_surface)
    PREVIOUS_SONG.draw_screen(display_surface)
    SOUND_UP.draw_screen(display_surface)
    SOUND_DOWN.draw_screen(display_surface)
    SEE_LEADERBOARD.draw_screen(display_surface)
    ABOUT_INFO.draw_screen(display_surface)
    SUPPORT.draw_screen(display_surface)
    EXIT_SCENE.draw_screen(display_surface)

    if MUSIC_TOGGLE.update_scene(mouse_event, trigger_update):
        Button.checkbox_toggle = not Button.checkbox_toggle
        volume_controller.toggle_mute()

    if NEXT_SONG.update_scene(mouse_event, trigger_update):
        volume_controller.next_song()

    if PREVIOUS_SONG.update_scene(mouse_event, trigger_update):
        volume_controller.last_song()  # Not implemented

    if SOUND_UP.update_scene(mouse_event, trigger_update):
        volume_controller.increase_volume()

    if SOUND_DOWN.update_scene(mouse_event, trigger_update):
        volume_controller.decrease_volume()

    if SEE_LEADERBOARD.update_scene(mouse_event, trigger_update): # Do i need to implement this?
        # Need to implement the saving of scores/games
        raise NotImplementedError("SEE_LEADERBOARD button Not implemented yet")

    if ABOUT_INFO.update_scene(mouse_event, trigger_update):
         # Read and display the README file
        try:
            with open('README.md', 'r') as file:
                readme_content = file.read()
                print(readme_content)
        except FileNotFoundError:
            print("README.md file not found.")
        except Exception as e:
            print(f"An error occurred while reading the README.md file: {e}")
        finally: 
            # Add info to the screen as well
            print("About info button clicked - this is a placeholder")

    if SUPPORT.update_scene(mouse_event, trigger_update):
        email = "will_add@example.com"
        font = pygame.font.Font(None, 36)
        email_position = (100, 200)
        icon_position = (100 + font.size(email)[0] + 10, 200)

        render_text(display_surface, email, email_position, font)
        copy_icon_rect = render_copy_icon(display_surface, icon_position)
        handle_copy_icon_click(mouse_event, copy_icon_rect, email)

    # Goes back to town if exit button is clicked
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_settings = True, False
