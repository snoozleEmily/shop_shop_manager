from .buttons import Button
from utils.interactables import Interactables


# Regular Buttons
EXIT_SCENE = Button(740, 4, text=None, type_tag="exit")
NEXT_BUTTON = Button(327, 320, text=None, type_tag="default")


# Settings Buttons
MUSIC_TOGGLE = Button(402, 20, text=None, type_tag="checkbox_on")
SOUND_UP = Button(402, 80, text=None, type_tag="default")
SOUND_DOWN = Button(337, 80, text=None, type_tag="default")
NEXT_SONG = Button(402, 140, text=None, type_tag="default")
PREVIOUS_SONG = Button(337, 140, text=None, type_tag="default")
SEE_LEADERBOARD = Button(254, 199, text="See Leaderboard", type_tag="caption_btn")
ABOUT_INFO = Button(254, 265, "About The Game", type_tag="caption_btn")
SUPPORT = Button(254, 330, "Support", type_tag="caption_btn")


# Scene-changer Buttons
START_GAME_BUTTON = Button(254, 280, "Start Game", type_tag="caption_btn")
SHOP_BUTTON = Button(10, 350, text=None, type_tag="default")
IVENTORY_BUTTON = Button(63, 350, text=None, type_tag="default")
TAVERN_BUTTON = Button(170, 350, text=None, type_tag="default")
HOME_BUTTON = Button(116, 350, text=None, type_tag="default")
SETTINGS_BUTTON = Button(768, 4, text=None, type_tag="settings")


# Minigame Buttons
ROLL_DICE = Button(254, 5, "Roll Dice", type_tag="caption_btn")
RETURN = Button(254, 295, "Return", type_tag="caption_btn")
DICE_CUP = Button(180, 75, text=None, type_tag="dice_cup")
SLEEP = Button(254, 55, text="Sleep", type_tag="caption_btn")
WAKE_UP  = Button(254, 115, text="Wake Up", type_tag="caption_btn")


# Interactable visuals
COINS_DISPLAY = Interactables(732, 350, "0", type_tag="coins")
