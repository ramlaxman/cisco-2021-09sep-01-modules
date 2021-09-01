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


class Person:
    '''A class that describes a person by name.'''

    def __init__(self, first, last):
        '''Creates a new Person object.
        
        - Expects: Two strings, first and last
        - Modifies: The instance
        - Returns: The instance
        '''
        self.first = first
        self.last = last
        
    def greet(self):
        '''Returns a string with a friendly greeting to the person.'''
        return f'Hello, {self.first} {self.last}'
    
p = Person('Reuven', 'Lerner')    
print(p.greet())


# Meaning: If this program is run directly from the command line,
# then print out "goodbye."  Otherwise, remain silent.
if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')
