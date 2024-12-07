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

table_width = (Global.SCREEN_WIDTH + CELL_WIDTH) - PADDING
table_height = (Global.SCREEN_HEIGHT // 2) - (PADDING * 6)

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
    Global.paginated_data.append(items_per_page)

viewport_surface = pygame.Surface((table_width, table_height))


def render_table(display_surface: pygame.Surface) -> None:
    viewport_surface.fill((255, 255, 255))

    # Fetch data for the current page
    pages = Global.paginated_data[Global.current_page]

    # Pre-compute constants for layout
    column_positions = [
        # Don't use here enumarate, it causes a bug
        j * (CELL_WIDTH + COLUMN_MARGIN) + PADDING for j in range(len(all_items[0]))
    ]
    row_offsets = [
        # Don't use here enumarate, it causes a bug
        (i + 1) * (CELL_HEIGHT + ROW_MARGIN) + PADDING for i in range(len(pages))
    ]

    # Draw column titles
    title_y = PADDING / 3
    for col_pos, title in zip(column_positions, all_items[0]):
        text_surface = FONT_CURSIVE.render(title, True, (0, 0, 0))
        viewport_surface.blit(text_surface, (col_pos, title_y))

    # Draw table rows
    for row_offset, row in zip(row_offsets, pages):
        for col_pos, cell in zip(column_positions, row):
            text_surface = FONT_CURSIVE.render(cell, True, (0, 0, 0))
            viewport_surface.blit(text_surface, (col_pos, row_offset))


    display_surface.blit(viewport_surface, (PADDING, PADDING))
