'''Great module for teaching.

This module has everything you would ever want!

- Data
- Functions
- Bad documentation
'''

if __name__ == '__main__':
    print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]


def hello(name):
    '''This is the best function ever written.

So great, it gets a two-line docstring.

You normally want your function docstring to say:
- Expects:
- Modifies:
- Returns:

'''

    return f'Hello, {name}!'


# Meaning: If this program is run directly from the command line,
# then print out "goodbye."  Otherwise, remain silent.
if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')
