from .clickables.buttons import Button

# Regular Buttons
EXIT_SCENE = Button(740, 4, text=None, type_tag="exit")
NEXT_BUTTON = Button(327, 309, text=None, type_tag="default")


# Settings Buttons
MUSIC_TOGGLE = Button(402, 20, text=None, type_tag="default")
SOUND_UP = Button(337, 80, text=None, type_tag="default")
SOUND_DOWN = Button(402, 80, text=None, type_tag="default")
NEXT_SONG = Button(337, 140, text=None, type_tag="default")
PREVIOUS_SONG = Button(402, 140, text=None, type_tag="default")
SEE_LEADERBOARD = Button(254, 199, text="See Leaderboard", type_tag="caption_btn")
ABOUT_INFO = Button(254, 265, "About The Game", type_tag="caption_btn")
SUPPORT = Button(254, 330, "Support", type_tag="caption_btn")


# Scene-changer Buttons
START_GAME_BUTTON = Button(254, 280, "Start Game", type_tag="caption_btn")
SHOP_BUTTON = Button(10, 350, text=None, type_tag="default")
IVENTORY_BUTTON = Button(63, 350, text=None, type_tag="default")
TAVERN_BUTTON = Button(170, 350, text=None, type_tag="default")
HOME_BUTTON = Button(116, 350, text=None, type_tag="default")
SETTINGS_BUTTON = Button(10, 6, text=None, type_tag="settings")


# Mini-game Buttons
ROLL_DICE = Button(254, 5, "Roll Dice", type_tag="caption_btn")
DICE_CUP = Button(254, 30, text=None, type_tag="dice_cup")
