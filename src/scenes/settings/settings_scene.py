from scenes.scene_manager import GameScenes
from .sound_controller import SoundController
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
        raise NotImplementedError("MUSIC_TOGGLE button Not implemented yet")

    if NEXT_SONG.update_scene(mouse_event, trigger_update):
        volume_controller.next_song()  # Not implemented

    if PREVIOUS_SONG.update_scene(mouse_event, trigger_update):
        volume_controller.previous_song()  # Not implemented

    if SOUND_UP.update_scene(mouse_event, trigger_update):
        volume_controller.increase_volume()

    if SOUND_DOWN.update_scene(mouse_event, trigger_update):
        volume_controller.decrease_volume()

    if SEE_LEADERBOARD.update_scene(mouse_event, trigger_update):
        # Need to implement the saving of scores/games
        raise NotImplementedError("SEE_LEADERBOARD button Not implemented yet")

    if ABOUT_INFO.update_scene(mouse_event, trigger_update):
        # What type of info should I add?
        raise NotImplementedError("ABOUT_INFO button Not implemented yet")

    if SUPPORT.update_scene(mouse_event, trigger_update):
        # Should I only add my email?
        raise NotImplementedError("SUPPORT button Not implemented yet")

    # Goes back to town if exit button is clicked
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_settings = True, False
