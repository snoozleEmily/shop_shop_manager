def wrap_text(text, font, max_width):
    """
    Wrap text to fit within a given width.
    """
    # Check if text is a dictionary, and extract the string if so
    if isinstance(text, dict):
        text = text.get("speech", "")
        
    words = text.split(" ")
    lines = []
    current_line = []

    for word in words:
        # Check the width of the line if we add this word
        test_line = " ".join(current_line + [word])
        line_width, _ = font.size(test_line)
        if line_width <= max_width:
            current_line.append(word)
        else:
            # If the line is too wide, append the current line to lines and start a new one
            lines.append(" ".join(current_line))
            lines.append("")  # Add an empty line for line spacing
            current_line = [word]

    # Add the last line
    lines.append(" ".join(current_line))
    return lines
