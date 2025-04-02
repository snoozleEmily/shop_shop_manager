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

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Check for a new section (e.g., ## Section Title)
        if line.startswith("## "):
            current_section = line[3:].strip()  # Get the section name (after "## ")

            # Initialize section with empty content
            readme_dict[current_section] = "" 
            
            # Reset subsection tracker
            current_sub_dict = None  

        # Check for a new subsection (e.g., ### Subsection Title)
        elif line.startswith("### ") and current_section:
            if current_sub_dict is None:
                current_sub_dict = {}  

                # Add subsections to the current section
                readme_dict[current_section] = current_sub_dict
                
            # Initialize subsection content
            current_sub_dict[line[4:].strip()] = ""  

        # Add content to the current section or subsection
        elif current_section:
            _append_content(readme_dict, current_section, current_sub_dict, line)

    return readme_dict


def _append_content(readme_dict, current_section, current_sub_dict, line):
    # Determine where to append the line
    if current_sub_dict:
        target_dict = current_sub_dict
        subsection = list(current_sub_dict.keys())[-1]  # Last key
    else:
        target_dict = readme_dict
        subsection = current_section

    # Add newline only if content already exists
    separator = "\n" if target_dict[subsection] else ""
    target_dict[subsection] += f"{separator}{line}"