#!/usr/bin/env python3
'''
This file is the main script of PM-TDC-PLOT.
'''

from tkinter.filedialog import askopenfilename

def main():
    """ main function

    This is the main function of this project.

    Args:
        NULL

    Returns:
        NULL

    Raises:
        NULL
    """
    filename = askopenfilename()
    print(filename)
    return

if __name__ == '__main__':
    main()
