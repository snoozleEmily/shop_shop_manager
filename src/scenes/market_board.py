import pygame

from utils.pygame_loads import (
    Global,
    all_items,
    FONT_CURSIVE,
)

CELL_WIDTH = 135
CELL_HEIGHT = 27
PADDING = 18
ROW_MARGIN = 10
COLUMN_MARGIN = 45

# Color constants
COLOR_WHITE = (255, 255, 255)
COLOR_TITLE_TEXT = (20, 13, 8)
COLOR_CELL_TEXT = (25, 25, 25)
COLOR_BORDER = (69, 69, 69)

# Precompute layout constants
COLUMN_POSITIONS = [
    j * (CELL_WIDTH + COLUMN_MARGIN) + PADDING for j in range(len(all_items[0]))
]
table_width = (Global.SCREEN_WIDTH + CELL_WIDTH) - PADDING
table_height = (Global.SCREEN_HEIGHT // 2) - (PADDING * 6)

# Calculate rows per page
rows_per_page = (table_height - CELL_HEIGHT - ROW_MARGIN) // (CELL_HEIGHT + ROW_MARGIN)

# Pagination variables
total_pages = len(all_items) // rows_per_page + (
    1 if len(all_items) % rows_per_page > 0 else 0
)

# Skip the first row (column titles) when paginating
items_without_titles = all_items[1:]

# Precompute pages
def precompute_pages():
    Global.paginated_data = [
        items_without_titles[i:i + rows_per_page] for i in range(0, len(items_without_titles), rows_per_page)
    ]

precompute_pages()

viewport_surface = pygame.Surface((table_width, table_height))

def render_table(display_surface: pygame.Surface) -> None:
    viewport_surface.fill(COLOR_WHITE)

    # Fetch data for the current page
    pages = Global.paginated_data[Global.current_page]

    # Pre-compute row offsets for the current page
    row_offsets = [
        (i + 1) * (CELL_HEIGHT + ROW_MARGIN) + PADDING for i in range(len(pages))
    ]

    def draw_text(surface, text, color, position):
        text_surface = FONT_CURSIVE.render(text, True, color)
        surface.blit(text_surface, position)

    # Draw column titles
    title_y = PADDING / 3
    for col_pos, title in zip(COLUMN_POSITIONS, all_items[0]):
        draw_text(viewport_surface, title, COLOR_TITLE_TEXT, (col_pos, title_y))

    # Draw table rows
    for row_offset, row in zip(row_offsets, pages):
        for col_pos, cell in zip(COLUMN_POSITIONS, row):
            draw_text(viewport_surface, cell, COLOR_CELL_TEXT, (col_pos, row_offset))

    # Draw outer border
    pygame.draw.rect(viewport_surface, COLOR_BORDER, (0, 0, table_width, table_height), 1)

    # Draw horizontal lines for each row including the title row
    for y in [(i * (CELL_HEIGHT + ROW_MARGIN)) + PADDING for i in range(1, len(pages) + 1)]:
        pygame.draw.line(viewport_surface, COLOR_BORDER, (0, y), (table_width, y))

    # Draw vertical lines for each column
    for x in [j * (CELL_WIDTH + COLUMN_MARGIN) + PADDING for j in range(1, len(all_items[0]) + 1)]:
        pygame.draw.line(viewport_surface, COLOR_BORDER, (x, 0), (x, table_height))

    display_surface.blit(viewport_surface, (PADDING, PADDING))