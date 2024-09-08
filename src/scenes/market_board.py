import pygame

from utils.pygame_loads import (
    Screen,
    all_items,
    FONT_CURSIVE,
)

CELL_WIDTH = 135
CELL_HEIGHT = 27
PADDING = 18
ROW_MARGIN = 10
COLUMN_MARGIN = 45

table_width = (Screen.SCREEN_WIDTH + CELL_WIDTH) - PADDING
table_height = (Screen.SCREEN_HEIGHT // 2) - (PADDING * 6)

# Calculate rows and columns per page
rows_per_page = (table_height - CELL_HEIGHT - ROW_MARGIN) // (CELL_HEIGHT + ROW_MARGIN)
cols_per_page = table_width // (CELL_WIDTH + COLUMN_MARGIN)

# Pagination variables
total_pages = len(all_items) // rows_per_page + (
    1 if len(all_items) % rows_per_page > 0 else 0
)

# Skip the first row (column titles) when paginating
items_without_titles = all_items[1:]

# Precompute pages
for page in range(total_pages):
    start_row = page * rows_per_page
    end_row = min(start_row + rows_per_page, len(items_without_titles))
    items_per_page = items_without_titles[start_row:end_row]
    Screen.paginated_data.append(items_per_page)

viewport_surface = pygame.Surface((table_width, table_height))


def render_table(display_surface: pygame.Surface) -> None:
    viewport_surface.fill((255, 255, 255))

    # Fetch data for the current page
    pages = Screen.paginated_data[Screen.current_page]

    # Draw the column titles
    titles = all_items[0]
    for j, title in enumerate(titles):
        text_surface = FONT_CURSIVE.render(title, True, (0, 0, 0))
        x = j * (CELL_WIDTH + COLUMN_MARGIN) + PADDING
        y = PADDING / 3
        viewport_surface.blit(text_surface, (x, y))

    # Iterate over the paginated items and draw the table (excluding titles)
    for i, row in enumerate(pages):
        for j, cell in enumerate(row):
            text_surface = FONT_CURSIVE.render(cell, True, (0, 0, 0))
            x = j * (CELL_WIDTH + COLUMN_MARGIN) + PADDING
            y = (i + 1) * (CELL_HEIGHT + ROW_MARGIN) + PADDING
            viewport_surface.blit(text_surface, (x, y))

    display_surface.blit(viewport_surface, (PADDING, PADDING))
