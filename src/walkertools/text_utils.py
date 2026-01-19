#Text Utils for string formatting

#__all__ keeps tab_complete clean. 
# Use only functions you want to show up in tab complete
__all__ = ['create_banner', 'print_blank_lines']

def create_banner(text: str, char: str = "#", padding: int = 2) -> str:
    """
    Wraps text in a decorative border for terminal output.

    Args:
        text: The string to be highlighted.
        char: The character used for the border (default is '#').
        padding: The number of spaces between the text and the border.

    Returns:
        A formatted string representing the banner.
    """
    line_length = len(text) + (padding * 2) + 2
    border = char * line_length

    spaces = " " * padding
    return f"{border}\n{char}{spaces}{text}{spaces}{char}\n{border}"


def print_blank_lines(num_of_lines):
    print("\n" * num_of_lines, end="")

