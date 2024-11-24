import pygame

from utils.pygame_loads import load_image


FRAME_WIDTH: int = 200
FRAME_HEIGHT: int = 200


# Load sprite frames
def get_sheep_frames(spritesheet_path: str, frame_width: int, frame_height: int) -> list[str]:
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


sheep_sprite = get_sheep_frames(
    r"D:\Projects\Python-studies\shop_shop_manager\images\characters\sheep\sheep_spritesheet.png",
    FRAME_WIDTH,
    FRAME_HEIGHT,
)

jumping_sheep = load_image(
    r"D:\Projects\Python-studies\shop_shop_manager\images\characters\sheep\sheep_jump.png"
)


sheep_sprite = [frame for i, frame in enumerate(sheep_sprite)]
jumping_sheep = pygame.transform.scale(jumping_sheep, (FRAME_WIDTH, FRAME_HEIGHT))
