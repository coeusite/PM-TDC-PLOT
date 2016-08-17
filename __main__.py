# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
    PM-TDC-PLOT.__main__
    ~~~~~~~~~~~~~~

    :copyright: (c) 2015 by CoeusITE.
    :license: LGPL, see LICENSE for more details.
'''

from tkinter import filedialog, messagebox
from libs import _inputs, _outputs, _automated

def main():
    """main function

    This is the main function of this project.

    """
    # automated processings
    _automated.run()
    # manually
    flag = messagebox.askquestion('Manually','Select a csv to plot?')
    if flag == 'no': return
    # select a csv file
    file_name = filedialog.askopenfilename()
    data = _inputs.csv_to_dataframe(file_name)
    # plot it~
    _outputs.plot(data)
    return

if __name__ == '__main__':
    main()
