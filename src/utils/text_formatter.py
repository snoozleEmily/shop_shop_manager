def wrap_text(text, font, max_width):
    """Wrap text to fit within a given width."""
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
            current_line = [word]

    # Add the last line
    lines.append(" ".join(current_line))
    return lines
