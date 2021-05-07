import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def concentric_plot():
    x, y = np.mgrid[-5:5:0.05, -5:5:0.05]
    z = (np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2))

    fig, ax = plt.subplots(1,1)
    im = ax.imshow(z)
    fig.colorbar(im)
    ax.yaxis.set_major_locator(plt.NullLocator()) # remove y axis ticks
    ax.xaxis.set_major_locator(plt.NullLocator()) # remove x axis ticks


def multi_concentric_plot():

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    fig, axes = plt.subplots(2,2, figsize=(10,10))

    # the colormaps we'll be trying out
    cmap_list = ['RdPu', 'spring', 'PRGn', 'gnuplot']

    for ax, name in zip(axes.flatten(), cmap_list):
        im = ax.imshow(z, aspect='auto',  cmap=plt.get_cmap(name))
        ax.yaxis.set_major_locator(plt.NullLocator())   # remove y axis ticks
        ax.xaxis.set_major_locator(plt.NullLocator())   # remove x axis ticks
        ax.set_aspect('equal', adjustable='box')        # make subplots square
        ax.set_title(f'Cmap: {name}', fontsize=18)      # add a title to each
        divider = make_axes_locatable(ax)               # make colorbar same size as each subplot
        cax = divider.append_axes("right", size="5%", pad=0.1)
        plt.colorbar(im, cax=cax)

def name_to_rgba(name, alpha=1.0):
    '''
    Converts str color name to rgb color + alpha
    value: string of characters representing a color.
    Returns: tuple (length 4) of RGBA values'''
    return colors.to_rgba(name, alpha=alpha)

def name_to_hex(name):
    '''
    Converts str color name to rgb color + alpha
    value: string of characters representing a color.
    Returns: string representing the hex color'''

    return colors.cnames[name]

def hex_to_rgb(value):
    '''
    Converts hex to rgb colours
    value: string of 6 characters representing a hex color.
    Returns: list (length 3) of RGB values'''
    value = value.strip("#") # removes hash symbol if present
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_dec(value):
    '''
    Converts rgb to decimal colours (i.e. divides each value by 256)
    value: list (length 3) of RGB values
    Returns: list (length 3) of decimal values'''
    return [v/256 for v in value]

def get_continuous_cmap(hex_list, float_list=None):
    ''' creates and returns a color map that can be used in heat map figures.
        If float_list is not provided, colour map graduates linearly between each color in hex_list.
        If float_list is provided, each color in hex_list is mapped to the respective location in float_list. 
        
        Parameters
        ----------
        hex_list: list of hex code strings
        float_list: list of floats between 0 and 1, same length as hex_list. Must start with 0 and end with 1.
        
        Returns
        ----------
        colour map'''
    rgb_list = [rgb_to_dec(hex_to_rgb(i)) for i in hex_list]
    if float_list:
        pass
    else:
        float_list = list(np.linspace(0,1,len(rgb_list)))
        
    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        col_list = [[float_list[i], rgb_list[i][num], rgb_list[i][num]] for i in range(len(float_list))]
        cdict[col] = col_list
    cmp = colors.LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
    return cmp