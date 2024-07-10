import pygame
from PIL import Image

def handle_gif_frames(gif_path):
    """
    Loads frames from a GIF file and converts them to Pygame images.

    Returns a list of Pygame images representing each frame of the GIF.
    """
    pil_image = Image.open(gif_path)
    frames = []
    try:
        while True:
            frame = pil_image.copy()
            frame = frame.convert('RGBA')
            frame_data = frame.tobytes()
            frame_image = pygame.image.fromstring(frame_data, frame.size, frame.mode)
            frames.append(frame_image)
            pil_image.seek(pil_image.tell() + 1)
    except EOFError:
        pass
    return frames