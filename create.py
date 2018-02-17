"""
Regenerate all those useful files that contain the color cycle.
"""

import matplotlib as mpl
import pylab as plt

# A list of (filename, template) pairs.
templates = [

    ('rg_friendly.mplstyle',
"""axes.prop_cycle    : cycler('color', {string_list})
"""),

    ('rg_friendly.py',
     """
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['axes.prop_cycle'] = cycler(color={hashstring_list})
"""),

]

cvals, names = zip(*[x.split() for x in open('colors.txt')])

data = {'string_list': '[' + ','.join(["'%s'" % c for c in cvals]) + ']',
        'hashstring_list': '[' + ','.join(["'#%s'" % c for c in cvals]) + ']'}

# Make files...
for filename, template in templates:
    open(filename, 'w').write(template.format(**data))


# Also make an image showing the colors with their names.
fig = plt.figure(figsize=(5, 4))
ax = plt.axes([0,0,1,1])

x = plt.arange(0., 6.28, .01)
y = plt.sin(x)
for i in range(len(names)):
    ax.plot(x, y-i*2, lw=2, color='C{}'.format(i))
    ax.text(1, 1-i*2, 'C{}: {}'.format(i, names[i]))

ax.axis('off')
fig.savefig('rg_friendly.png')

