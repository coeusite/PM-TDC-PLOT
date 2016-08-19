# PM-TDC-PLOT for *TSI 3321*

This project is designed for parsing data from *TSI 3321*, and it is a mini project that uses **Python 3** to create a time-diameter-count plot of particular matters.

In the plot, X-axis refers to time, Y-axis indicates diameter and the color at point (x, y) is the count of particular matters with diameter y at time x.

Raw txt files in the "data/raw/" folder would be automatically parsed during initialization 
and correspoding figures would be automatically generated.
Parsed data would be stored in the "data/parsed/" folder, 
and figures would be stored in the "figures" folder.

## I would try to
- follow [Google Python Style](https://google.github.io/styleguide/pyguide.html)
- make it interactive (with Flask)

## License

PM-TDC-PLOT is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License (LGPL) as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

PM-TDC-PLOT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PM-TDC-PLOT.  If not, see <http://www.gnu.org/licenses/>.
