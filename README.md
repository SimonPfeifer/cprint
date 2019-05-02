# cprint
Small python package for printing text in different colours and typography.

### Prerequisites

You need to have a Python2.7+ or Python3+ installation with the following libraries:

### Usage

The `cprint()` function simply adds one keyword argument, `c`, to the python `print()` function. This extra keyword argument can change the output of `print()` to one colour and any number of given styles. Colours are given in lower case and styles in upper case. Any other keyword arguments are passed on to `print()`.

| Character  |  Colour         |
| ---------- | --------------- |
| 'k'        | black           |
| 'r'        | red             |
| 'g'        | green           |
| 'y'        | yellow          |
| 'b'        | blue            |
| 'm'        | magenta         |
| 'c'        | cyan            |
| 'w'        | white           |

| Character  | Style           |
| ---------- | --------------- |
| 'B'        | bold            |
| 'D'        | dark            |
| 'I'        | italic          |
| 'U'        | underline       |
| 'F'        | flash           |
| 'R'        | reverse colour  |
| 'C'        | crossed through |

Example:
```python
cprint('Hello World!', c='rB')
cprint('Hello World!', 'Monty Python', c='bUI', end='!')
```
