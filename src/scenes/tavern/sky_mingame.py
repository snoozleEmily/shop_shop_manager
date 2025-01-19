from scenes.tavern.cloud import Cloud
from scenes.scene_manager import GameScenes
from utils.declared_buttons import EXIT_SCENE


cloud_A = Cloud()
cloud_B = Cloud()
cloud_C = Cloud()
clouds = [cloud_A, cloud_B, cloud_C] # Add more clouds here

def render_sky(display_surface, mouse_event, trigger_update=None):
    # Fill the background with sky blue color
    sky_blue = (135, 206, 235)  # RGB values for sky blue
    display_surface.fill(sky_blue)
    
    # Update and draw bubble
    # bubble.draw_container(display_surface) #  See container for debugging
    for cloud in clouds:
        cloud.update_cloud()
        cloud.draw_cloud(display_surface)
        
        # Check for click to make the sheep jump
        if cloud.kill_cloud(mouse_event):
            print('Cloud clicked')
            
    # Goes back to town if exit button is clicked
        EXIT_SCENE.draw_screen(display_surface)  # Not visible in minigame
        if EXIT_SCENE.update_scene(mouse_event, trigger_update):
            GameScenes.in_tavern, GameScenes.in_sky = True, False    