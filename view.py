import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from colormap import get_continuous_cmap, names_to_hex

def concentric_plot(cmap_list= ['viridis']):
    x, y = np.mgrid[-5:5:0.05, -5:5:0.05]
    z = (np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2))

    fig, ax = plt.subplots(1,1)
    im = ax.imshow(z, cmap=get_continuous_cmap(names_to_hex(cmap_list)))
    fig.colorbar(im)
    ax.yaxis.set_major_locator(plt.NullLocator()) # remove y axis ticks
    ax.xaxis.set_major_locator(plt.NullLocator()) # remove x axis ticks

def multi_concentric_plot(cmap_list):

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    fig, axes = plt.subplots(2,2, figsize=(10,10))

    # the colormaps we'll be trying out
    if not cmap_list:
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