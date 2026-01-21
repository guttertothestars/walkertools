#Text Utils for string formatting

#__all__ keeps tab_complete clean. 
# Use only functions you want to show up in tab complete
__all__ = ['create_banner', 'print_blank_lines']

def create_banner(text: str, char: str = "#"):
    """
    Wraps text in a decorative border for terminal output.

    Args:
        text: The string to be highlighted.
        char: The character used for the border (default is '#').

    Returns:
        A formatted string representing the banner.
    """
    line_length = len(text) + 2
    border = char * line_length

    return f"{border}\n {text}\n{border}"

def print_blank_lines(num_of_lines):
    print("\n" * num_of_lines, end="")

