import re
import json
from enum import Enum


README_PATH = r"D:\Projects\Python-studies\shop_shop_manager\README.md"
ABOUT_PATH = r"D:\Projects\Python-studies\shop_shop_manager\src\utils\about_game.py"

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

def parse_readme(file_path):
    """
    Reads a markdown file and organizes its content into a dictionary.
    Sections (##) become dictionary keys, and subsections (###) are nested dictionaries.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        return _process_lines(lines)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return {}  # Ensure a return value even in case of an error


def _process_lines(lines):
    """
    Helper function to process lines from the file and construct the dictionary.
    """
    readme_dict = {}
    current_section = None
    current_sub_dict = None

    formatted_line = ("\n" + line) if readme_dict[current_section] else line

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # If the line starts with '## ', it's a new section header
        if line.startswith("## "):
            current_section = line[3:].strip()
            readme_dict[current_section] = ""  # Initialize section
            current_sub_dict = None  # Reset subsection tracker

        # If the line starts with '### ' and there's an active section, it's a subsection
        elif line.startswith("### ") and current_section:
            if current_sub_dict is None:
                current_sub_dict = {}
                readme_dict[current_section] = current_sub_dict  # Store subsections
            current_sub_dict[line[4:].strip()] = ""  # Initialize subsection
            
        # If the line belongs to a current section, add its content
        elif current_section:
            _append_content(readme_dict, current_section, current_sub_dict, line)

    return readme_dict


def _append_content(readme_dict, current_section, current_sub_dict, line):
    """
    Helper function to append content to the appropriate section or subsection.
    """
    if current_sub_dict:
        last_sub_key = list(current_sub_dict.keys())[-1]
        current_sub_dict[last_sub_key] += f"\n{line}" if current_sub_dict[last_sub_key] else line
    else:
        readme_dict[current_section] += f"\n{line}" if readme_dict[current_section] else line


if __name__ == "__main__":
    # Read and print README.md
    parsed_readme = parse_readme(README_PATH)
    print("README.md Content:\n", json.dumps(parsed_readme, indent=4, ensure_ascii=False))

    # Example Usage
    print("\nUsing Enums to Access Data:")
    if ReadmeSections.CONTRIBUTING.value in parsed_readme:
        contributing_section = parsed_readme[ReadmeSections.CONTRIBUTING.value]

        if isinstance(contributing_section, dict
            ) and ContributingSubsections.ADD_BUTTON.value in contributing_section:
            print(
                "\nAdd Button Subsection:\n",
                contributing_section[ContributingSubsections.ADD_BUTTON.value],
            )

    # Read and print ABOUT.md
    parsed_about = parse_readme(ABOUT_PATH)
    print("\nAbout Section Data:\n", json.dumps(parsed_about, indent=4, ensure_ascii=False))