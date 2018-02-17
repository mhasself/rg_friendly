# Alternative default color cycle for matplotlib

## Quick start

### To set the colors in a single script:

Copy the lines from rg_friendly.py into the top of your script.

### To set the colors for all scripts running in a single directory:

Copy the lines from rg_friendly.mplstyle to the end of the file
matplotlibrc in your script directory.  (Settings in the
./matplotlibrc will override the system and per-user matplotlibrc
files.)

### To make the colors available as a "style"

Figure out where your matplotlib style files should go.  On my system,
it's ~/.config/matplotlib/stylelib/.  Copy the file
rg_friendly.mplstyle into that folder.  Then in your scripts you can
do:

    import pylab as plt
    plt.style.use('rg_friendly')

For more details on setting up styles, see
https://matplotlib.org/users/customizing.html

### To make the colors the default for all plots

Figure out where your matplotlibrc file is.  On my system, it's
~/.config/matplotlib/matplotlibrc.  Append the contents of
rg_friendly.mplstyle to that matplotlibrc file.  (Note that the
matplotlibrc file might not exist yet.)

For more details on matplotlibrc, see
https://matplotlib.org/users/customizing.html

## Discussion

Here are some new colors for matplotlib.  When matplotlib version 2
came out, the new default color cycle was very nice looking but caused
trouble for some colorblind users, such as myself and this fellow:

https://github.com/matplotlib/matplotlib/issues/9460

Without any extensive consultation or scientific approach, I have
tweaked the default matplotlib palette slightly so that it is not so
degenerate to my eyes.

![Alt text](rg_friendly.png?raw=true "Title")

The colors were created according to the following rules:
* I started from the default matplotlib 2 color cycle.
* I changed the color codes until the colors were clearly disambiguated.
* When I changed the colors I tried to move them towards shades that
  had a very clear identity; i.e. there should be only one shade that
  most people would call "red", and another that most could agree is
  "pink".  I was probably less successful on this since it's not
  typically the strength of a color-blind person.
* I ran it by some colleagues for input!  Many thanks to their
  encouragement and rapid adoption of my suggestions.

