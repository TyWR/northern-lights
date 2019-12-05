import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, Normalize
from matplotlib.colorbar import ColorbarBase

def create_cmap():
    first  = [163/255, 190/255, 140/255,   0]
    green  = [163/255, 190/255, 140/255, 0.8]
    violet = [180/255, 142/255, 173/255, 1]
    to_green = list(np.linspace(first, green, num=51))
    to_violet = list(np.linspace(green, violet, num=50))
    return ListedColormap(to_green + to_violet)

def plot_cmap(cax):
    cmap = create_cmap()
    norm = Normalize(vmin=0, vmax=100)
    cb = ColorbarBase(cax, cmap=cmap, norm=norm,
                      orientation='horizontal',
                      ticks=[0, 50, 100])
    cb.patch.set_facecolor((41/255, 46/255, 57/255))
    cb.ax.set_xticklabels(['0%', '50%', '100%'],
                          fontname='DIN Alternate')
    cb.set_label('Aurora seeing percentage (%)',
                 fontname='DIN Alternate')
    cb.outline.set_color((1, 1, 1, 0))

    cax.tick_params(axis='y', colors=(1, 1, 1, 0))
    cax.tick_params(axis='x', colors='#eceff4', length=0)
    cax.xaxis.label.set_color('#eceff4')

def plot_world(ax):
    world = gpd.read_file(
        gpd.datasets.get_path('naturalearth_lowres')
    )
    world.plot(color='#434c5e', edgecolor='#434c5e', ax=ax)
    ax.margins(x=0, y=0)

def plot_all():
    fig, ax = plt.subplots(1, 1, figsize=(15,1))
    fig.patch.set_facecolor((41/255, 46/255, 57/255))
    plot_cmap(ax)
    fig.tight_layout()
    fig.savefig('world.png', bbox_inches='tight', facecolor=fig.get_facecolor(),
                pad_inches=0, dpi=350)
    plt.show()
