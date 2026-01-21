#Input/output utils, including some validation
#import dependencies
import os 


#__all__ keeps tab_complete clean. 
# Use only functions you want to show up in tab complete


__all__ = ['ask_for', 'clear_screen']

# request and validate a single input
def ask_for(data_type, prompt, low, high):
    while True:
        try:
            x = data_type(input(prompt))
            if x < low or x > high:
                print(f'Must print a value between {low} and {high}')
            else:
                return x
        except ValueError:
            print('Invalid value, try again')


def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    """
    # 'nt' is the internal name for Windows. 
    # Otherwise, we assume it's a POSIX system (Linux/Mac).
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')