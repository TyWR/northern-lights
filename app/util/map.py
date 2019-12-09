import geopandas as gpd
import matplotlib.pyplot as plt

def plot_world():
    fig, ax = plt.subplots(1, 1, figsize=(15,7))
    fig.patch.set_facecolor((41/255, 46/255, 57/255))

    world = gpd.read_file(
        gpd.datasets.get_path('naturalearth_lowres')
    )
    world.plot(color='#3b4252', edgecolor='#4c566a', ax=ax)
    ax.margins(x=0, y=0)
    ax.axis('off')
    fig.tight_layout()
    fig.savefig('world.png', bbox_inches='tight',
                facecolor=fig.get_facecolor(),
                pad_inches=0, dpi=350)
    plt.show()

plot_world()
