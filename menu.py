def menu(*args):   # this is pronounced "splat-args" in the Python world --
    # it means all positional arguments are assigned to the tuple args

    while True:

        print(f'Choose one of these: {args}')

        options = '/'.join(sorted(args))

        # get the user's input, and remove whitespace from the sides
        s = input(f'Choose one: {options}').strip()

        if s in args:
            return s

        print(f'{s} is not a valid input! Try again!')
