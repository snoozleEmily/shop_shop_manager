import pygame

from utils.pygame_loads import load_image

# Load jumping sheep
jumping_sheep = load_image(
    r"D:\Projects\Python-studies\shop_shop_manager\images\characters\sheep\sheep_jump.png"
)


# Load sprite frames
def get_sheep_frames(spritesheet_path: str, frame_width: int, frame_height: int):
    sprite_sheet = load_image(spritesheet_path)
    sheet_width, sheet_height = sprite_sheet.get_size()
    sprites = []

    # Extract individual frames from the sprite sheet
    for y in range(0, sheet_height, frame_height):
        for x in range(0, sheet_width, frame_width):
            frame = sprite_sheet.subsurface(
                pygame.Rect(x, y, frame_width, frame_height)
            )
            sprites.append(frame)

    return sprites


sheep_sprites = get_sheep_frames(
    r"D:\Projects\Python-studies\shop_shop_manager\images\characters\sheep\sheep_spritesheet.png",
    200,
    200,
)


# Remove the excluded frame from the animation list
sheep_sprites = [frame for i, frame in enumerate(sheep_sprites)]
