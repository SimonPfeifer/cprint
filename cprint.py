from __future__ import print_function
def cprint(*args, **kwargs):
    ''' 
    Prints text in different colours and typography.

    Parameters
    ----------------
    *args : str or scalar or array-like, optional
        Objects passed to print()

    c : str, optional
        A string of letters to set the colour and typography.
        
        ========== ===========
        character  colour
        ========== ===========
        'k'        black
        'r'        red
        'g'        green
        'y'        yellow
        'b'        blue
        'm'        magenta
        'c'        cyan
        'w'        white
        ========== ===========
        character  style
        ========== ===========
        'B'        bold
        'D'        dark
        'I'        italic
        'U'        underline
        'F'        flash
        'R'        reverse colour
        'C'        crossed through

    **kwargs : print() properties, optional
        Any other keyword arguments accepted by print().

    Example
    -----------
    cprint('Hello World!', c='rB')
    cprint('Hello World!', 'Monty Python', c='bUI', end='!')

    '''
    c_args = list(kwargs.pop('c', ''))

    prefix = '\033['
    if 'k' in c_args:
        prefix += '90;'
    elif 'r' in c_args:
        prefix += '91;'
    elif 'g' in c_args:
        prefix += '92;'
    elif 'y' in c_args:
        prefix += '93;'
    elif 'b' in c_args:
        prefix += '94;'
    elif 'm' in c_args:
        prefix += '95;'
    elif 'c' in c_args:
        prefix += '96;'
    elif 'w' in c_args:
        prefix += '97;'

    if 'B' in c_args:
        prefix += '1;'
    if 'D' in c_args:
        prefix += '2;'
    if 'I' in c_args:
        prefix += '3;'
    if 'U' in c_args:
        prefix += '4;'
    if 'F' in c_args:
        prefix += '5;'
    if 'R' in c_args:
        prefix += '7;'
    if 'C' in c_args:
        prefix += '9;'

    print(prefix[:-1]+'m', end='')
    print(*args, **kwargs)
    print('\033[0m', end='')
