import pygame
import random
import math
from utils.pygame_loads import load_image

# Constants
CLOUDS_PATH = r'Python-studies\\shop_shop_manager\\images\\characters\\sheep\\clouds'
CLOUD_NAMES = ['sheepish', 'sinister', 'sleepy', 'sus']

# Load images globally to avoid repeated loading
CLOUD_IMAGES = [load_image(f"{CLOUDS_PATH}\\{cloud}.png") for cloud in CLOUD_NAMES]

class Cloud:
    """Class to manage the cloud behavior."""

    minigame_active = False
    CONTAINER_WIDTH = 620
    CONTAINER_HEIGHT = 170

    def __init__(self, container_x=97, container_y=11, min_distance=120):
        self.container_x = container_x
        self.container_y = container_y
        self.min_distance = min_distance

        # Random position within the container
        self.x = random.randint(self.container_x, self.container_x + self.CONTAINER_WIDTH)
        self.y = random.randint(self.container_y, self.container_y + self.CONTAINER_HEIGHT)
        self.last_x = self.x
        self.last_y = self.y
        self.current_cloud = random.choice(CLOUD_IMAGES)
        self.timer = random.randint(30, 60)  # Cloud stays for 30-60 frames
        self.visible = False

    def _calculate_distance(self, x1, y1, x2, y2):
        """Calculate Euclidean distance."""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def _generate_random_position(self):
        """Generate a random position within the container."""
        return (
            random.randint(self.container_x, self.container_x + self.CONTAINER_WIDTH),
            random.randint(self.container_y, self.container_y + self.CONTAINER_HEIGHT),
        )

    def _is_valid_position(self, new_x, new_y):
        """Check if the new position is valid based on minimum distance."""
        return self._calculate_distance(self.last_x, self.last_y, new_x, new_y) >= self.min_distance

    def update_cloud(self):
        """Update the cloud's position and timer."""
        if self.timer > 0:
            self.timer -= 1
        else:
            while True:
                new_x, new_y = self._generate_random_position()
                if self._is_valid_position(new_x, new_y):
                    self._update_position(new_x, new_y)
                    break

    def _update_position(self, new_x, new_y):
        """Update cloud position and reset timer."""
        self.last_x, self.last_y = self.x, self.y
        self.x, self.y = new_x, new_y
        self.current_cloud = random.choice(CLOUD_IMAGES)
        self.timer = random.randint(60, 120)
        self.visible = True

    def draw_cloud(self, display_surface: pygame.Surface):
        """Draw the cloud if it is visible."""
        if self.visible and self.current_cloud:
            display_surface.blit(self.current_cloud, (self.x, self.y))

    def kill_cloud(self, mouse_event: pygame.event.Event) -> bool:
        """Check if the cloud is clicked and make it disappear."""
        if (
            mouse_event.type == pygame.MOUSEBUTTONDOWN
            and mouse_event.button == 1
            and self.visible
            and self.current_cloud
        ):
            if (
                self.x <= mouse_event.pos[0] <= self.x + self.current_cloud.get_width()
                and self.y <= mouse_event.pos[1] <= self.y + self.current_cloud.get_height()
            ):
                self.visible = False
                return True
        return False

    @staticmethod
    def sync_clouds(clouds, min_distance=120):
        """Update multiple clouds with a delay and ensure minimum distance."""
        for i in range(1, len(clouds)):
            clouds[i].timer -= int(0.3 * 60)

        cloud_positions = set()

        for cloud in clouds:
            while True:
                cloud.update_cloud()
                current_position = (cloud.x, cloud.y)
                if all(
                    Cloud._calculate_distance(x, y, cloud.x, cloud.y) >= min_distance
                    for x, y in cloud_positions
                ):
                    cloud_positions.add(current_position)
                    break