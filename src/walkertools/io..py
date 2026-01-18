#Input/output utils, including some validation

#__all__ keeps tab_complete clean. 
# Use only functions you want to show up in tab complete
__all__ = ['ask_for']


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