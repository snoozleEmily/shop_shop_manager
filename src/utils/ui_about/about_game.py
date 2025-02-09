import json
from enum import Enum


from files_exist import check_readme
from readme_parser import parse_readme


README_PATH = r"D:\Projects\Python-studies\shop_shop_manager\README"
ABOUT_PATH = r"D:\Projects\Python-studies\shop_shop_manager\assets\data\about"

# New section/subsection names need to be added here
class ReadmeSections(Enum):
    INTRO = "Shop Shop Manager Game"
    ABOUT = "What is it about?"
    GAMEPLAY = "Gameplay"
    CONTRIBUTING = "Contributing"
    LICENSE = "License"

# New game expensions need to be added here
class ContributingSubsections(Enum):
    RENDERING = "Rendering"
    ADD_SCENE = "Adding a New Scene"
    ADD_BUTTON = "Adding a New Button"
    ADD_ITEM = "Adding a New Item"
    ADD_DIALOGUE = "Adding a New Dialogue"

if __name__ == "__main__":
     # Import the check_readme function

    # Use check_readme to get the parsed README content
    parsed_readme = check_readme(README_PATH)
    if parsed_readme:
        print("README.md Content:\n", json.dumps(parsed_readme, indent=4, ensure_ascii=False))

        # Example Usage
        print("\nUsing Enums to Access Data:")
        if ReadmeSections.CONTRIBUTING.value in parsed_readme:
            contributing_section = parsed_readme[ReadmeSections.CONTRIBUTING.value]

            if isinstance(contributing_section, dict) and ContributingSubsections.ADD_BUTTON.value in contributing_section:
                print(
                    "\nAdd Button Subsection:\n",
                    contributing_section[ContributingSubsections.ADD_BUTTON.value],
                )
    else:
        print("No pre-processed README file found.")

    # Use check_readme to get the parsed ABOUT content
    parsed_about = check_readme(ABOUT_PATH)
    if parsed_about:
        print("\nAbout Section Data:\n", json.dumps(parsed_about, indent=4, ensure_ascii=False))
    else:
        print("No pre-processed ABOUT file found.")