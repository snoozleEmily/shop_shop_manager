import os
import json

from .readme_parser import parse_readme 


JSON_FILE_PATH = r"D:\Projects\Python-studies\shop_shop_manager\README_parsed.json"
MD_FILE_PATH = r"D:\Projects\Python-studies\shop_shop_manager\README_parsed.md"
ABOUT_FOLDER_PATH = r"D:\Projects\Python-studies\shop_shop_manager\src\utils\about"
MESSAGE = "This is a pre-stored value. If you want the updated README, delete the file at ABOUT_PATH."

def check_readme(file_path, folder_path=None):
    """
    Checks if a pre-processed JSON or .md file exists in the correct folder.
    If not, processes the README file and stores the result in a JSON or .md file.
    Raises an error if unexpected files are found in the folder.
    """
    if folder_path is None:
        folder_path = ABOUT_FOLDER_PATH  # Ensure we're checking the right folder

    print(f"Checking folder path: {folder_path}")
    
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}. Skipping file validation.")
        return None  # Avoid error if folder is missing

    all_files = os.listdir(folder_path)
    print(f"Files found in the folder: {all_files}")

    if not all_files:
        print("No files found in the folder. Skipping file validation.")
        return None

    # Check for unexpected files in the folder
    for file_name in all_files:
        if file_name.startswith('.') or os.path.isdir(os.path.join(folder_path, file_name)):
            continue  # Ignore hidden files and directories
        if not (file_name.endswith('.json') or file_name.endswith('.md')):
            raise ValueError(f"Unexpected file found in the folder: {file_name}. It should only contain JSON or MD archives.")

    # Check for existing parsed files
    if os.path.exists(JSON_FILE_PATH):
        print(MESSAGE)
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    if os.path.exists(MD_FILE_PATH):
        print(MESSAGE)
        with open(MD_FILE_PATH, 'r', encoding='utf-8') as md_file:
            return json.load(md_file)

    # If no pre-stored file found, parse README and save it
    parsed_readme = parse_readme(file_path)
    save_parsed_data(parsed_readme)

    return parsed_readme


def save_parsed_data(parsed_data):
    """
    Saves parsed data to a JSON file and .md file for future use.
    """
    with open(JSON_FILE_PATH, 'w', encoding='utf-8') as json_file:
        json.dump(parsed_data, json_file, indent=4, ensure_ascii=False)

    with open(MD_FILE_PATH, 'w', encoding='utf-8') as md_file:
        json.dump(parsed_data, md_file, indent=4, ensure_ascii=False)
