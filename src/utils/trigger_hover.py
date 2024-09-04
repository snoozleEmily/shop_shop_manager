from scenes.scene_manager import GameScenes
from utils.declared_buttons import (
    EXIT_SCENE,
    ABOUT_INFO,
    MUSIC_TOGGLE,
    SOUND_UP,
    SOUND_DOWN,
    NEXT_SONG,
    PREVIOUS_SONG,
    SEE_LEADERBOARD,
    SUPPORT,
    NEXT_BUTTON,
    SLEEP,
    ROLL_DICE,
    DICE_CUP,
)

# Which buttons trigger the rerendering of the scene if hovered
shop: GameScenes = GameScenes(
    buttons_in_scene={
        "shop": [
            EXIT_SCENE,
            NEXT_BUTTON,
        ]
    }
)
inventory: GameScenes = GameScenes(
    buttons_in_scene={
        "inventory": [
            EXIT_SCENE,
        ]
    }
)
home: GameScenes = GameScenes(
    buttons_in_scene={
        "home": [
            SLEEP,
            EXIT_SCENE,
        ]
    }
)
tavern: GameScenes = GameScenes(
    buttons_in_scene={
        "tavern": [
            EXIT_SCENE,
            ROLL_DICE,
            DICE_CUP,
        ]
    }
)
settings: GameScenes = GameScenes(
    buttons_in_scene={
        "settings": [
            EXIT_SCENE,
            MUSIC_TOGGLE,
            SOUND_UP,
            SOUND_DOWN,
            NEXT_SONG,
            PREVIOUS_SONG,
            SEE_LEADERBOARD,
            SUPPORT,
            ABOUT_INFO,
        ]
    }
)
