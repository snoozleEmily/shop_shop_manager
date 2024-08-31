from utils.clickables import Clickable

# Regular Buttons
EXIT_SCENE = Clickable(740, 4, text=None, type_tag="exit_scene")
NEXT_BUTTON = Clickable(327, 309, text=None, type_tag="box")


# Settings Buttons
MUSIC_TOGGLE = Clickable(402, 20, text=None, type_tag="box")
SOUND_UP = Clickable(337, 80, text=None, type_tag="box")
SOUND_DOWN = Clickable(402, 80, text=None, type_tag="box")
NEXT_SONG = Clickable(337, 140, text=None, type_tag="box")
PREVIOUS_SONG = Clickable(402, 140, text=None, type_tag="box")
SEE_LEADERBOARD = Clickable(254, 199, text="See Leaderboard", type_tag="button")
ABOUT_INFO = Clickable(254, 265, "About The Game", type_tag="button")
SUPPORT = Clickable(254, 330, "Support", type_tag="button")


# Scene-changer Buttons
START_GAME_BUTTON = Clickable(254, 280, "Play Game", type_tag="button")
SHOP_BUTTON = Clickable(10, 350, text=None, type_tag="box")
IVENTORY_BUTTON = Clickable(63, 350, text=None, type_tag="box")
HOME_BUTTON = Clickable(116, 350, text=None, type_tag="box")
SETTINGS_BUTTON = Clickable(4, 5, text=None, type_tag="settings")
