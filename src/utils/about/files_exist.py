import os
import json
from readme_parser import parse_readme  # Import the parse_readme function

JSON_FILE_PATH = r"D:\Projects\Python-studies\shop_shop_manager\README_parsed.json"
MD_FILE_PATH = r"D:\Projects\Python-studies\shop_shop_manager\README_parsed.md"
MESSAGE = "This is a pre-stored value. If you want the updated README, delete the file at ABOUT_PATH."

def check_readme(file_path, folder_path=None):
    """
    Checks if a pre-processed JSON or .md file exists. If so, returns the parsed content.
    If not, processes the README file and stores the result in a JSON or .md file.
    Raises an error if there are other files in the folder.
    """
    if folder_path is None:
        folder_path = os.path.dirname(JSON_FILE_PATH)

    # Check for other files in the folder
    for file_name in os.listdir(folder_path):
        if not (file_name.endswith('.json') or file_name.endswith('.md')):
            INFO = f"It should only contain JSON or MD archives."
            raise ValueError(f"Unexpected file found in the folder: {file_name}. {INFO}")

    # Check if a JSON or .md file exists
    if os.path.exists(JSON_FILE_PATH):
        print(MESSAGE)
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    if os.path.exists(MD_FILE_PATH):
        print(MESSAGE)
        with open(MD_FILE_PATH, 'r', encoding='utf-8') as md_file:
            return json.load(md_file)

    # No pre-stored file found, parse README and save it
    parsed_readme = parse_readme(file_path)
    # Save parsed content to a JSON or .md file
    save_parsed_data(parsed_readme)

    return parsed_readme


def save_parsed_data(parsed_data):
    """
    Saves parsed data to a JSON file and .md file for future use.
    """
    # Save as JSON
    with open(JSON_FILE_PATH, 'w', encoding='utf-8') as json_file:
        json.dump(parsed_data, json_file, indent=4, ensure_ascii=False)

    # Optionally, save as .md file (assuming it's just a JSON format for simplicity)
    with open(MD_FILE_PATH, 'w', encoding='utf-8') as md_file:
        json.dump(parsed_data, md_file, indent=4, ensure_ascii=False)