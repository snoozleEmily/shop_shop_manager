import pygame
import numpy as np
from scenes import *

with open(r'Python-studies\shop_shop_manager\items\all_items.csv', 'r') as file:
    all_items = np.genfromtxt(file, delimiter=',', dtype=str)

FONT = pygame.font.Font(r'Python-studies\shop_shop_manager\assets\SKEETCH_.TTF', 36)
CELL_WIDTH, CELL_HEIGHT = 105, 25
PADDING = 12
ROW_MARGIN = 9

table_width = Globals.screen_width - PADDING
table_height = (Globals.screen_height // 2) - (PADDING * 5)

rows_per_page = (table_height - CELL_HEIGHT - ROW_MARGIN) // (CELL_HEIGHT + ROW_MARGIN)
cols_per_page = table_width // CELL_WIDTH

# Pagination
current_page = 0
total_pages = len(all_items) // rows_per_page + (1 if len(all_items) % rows_per_page > 0 else 0)

viewport_surface = pygame.Surface((table_width, table_height))

def render_table(display_surface):
    start_row = current_page * rows_per_page
    end_row = min(start_row + rows_per_page, len(all_items))

    viewport_surface.fill((255, 255, 255))

    for i, row in enumerate(all_items[start_row:end_row]):
        for j, cell in enumerate(row):
            if i == 0: # Column Titles
                text_surface = FONT.render(cell, True, (0, 0, 0))
                x = j * CELL_WIDTH + PADDING
                y = PADDING / 3
                viewport_surface.blit(text_surface, (x, y))
            else: 
                text_surface = FONT.render(cell, True, (0, 0, 0))
                x = j * CELL_WIDTH + PADDING
                y = i * (CELL_HEIGHT + ROW_MARGIN) + PADDING
                viewport_surface.blit(text_surface, (x, y))

    display_surface.blit(viewport_surface, (PADDING, PADDING))
    pygame.display.flip()

