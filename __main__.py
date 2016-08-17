# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
    PM-TDC-PLOT.__main__
    ~~~~~~~~~~~~~~

    :copyright: (c) 2015 by CoeusITE.
    :license: LGPL, see LICENSE for more details.
'''

from tkinter.filedialog import askopenfilename
import _inputs, _outputs

def main():
    """main function

    This is the main function of this project.

    """
    file_name = askopenfilename()
    data = _inputs.csv_to_dataframe(file_name)
    _outputs.plot(data)
    return

if __name__ == '__main__':
    main()
