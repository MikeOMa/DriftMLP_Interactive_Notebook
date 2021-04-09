"""
Backend for interactive.ipynb to keep the notebook relatively tidy.
"""

import ipywidgets as widgets
import cartopy.crs as ccrs
import driftmlp
import matplotlib.pyplot as plt

def get_network(_str_append):
    network = driftmlp.network_from_file('transition_'+_str_append+'.GraphML', visual=False)
    return network
EXP_STR =(
"""
Blue lines are going from the blue point to the red point above.
Red lines are going from the red point to the blue point above.
""")
class interactive_app:
    def __init__(self):
        self.network = None
        self.network_type = None
        self.__name__ = 'interactive_app'

    def __call__(self, lon_from, lat_from, lon_to, lat_to, network_type):
        ### This is relatively expensive so only do it when needed
        if network_type != self.network_type or self.network is None:
            self.network = get_network(network_type)
            self.network_type = network_type

        from_loc = (lon_from, lat_from)
        to_loc = (lon_to, lat_to)
        fig = plt.figure()
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.coastlines()
        ax.plot((from_loc[0]), (from_loc[1]), 'bo', transform=ccrs.Geodetic())
        ax.plot((to_loc[0]), (to_loc[1]), 'ro', transform=ccrs.Geodetic())
        ax.plot(to_loc[0], to_loc[1], transform=ccrs.Geodetic())
        ax.set_extent([-180, 180, -90, 90])
        plt.show()
        path = driftmlp.shortest_path.SingleSP(self.network, from_loc, to_loc)
        if path.sp.travel_time != -1:
            m = path.plot_folium()
            print(EXP_STR)
            display(m)
            display(path)

        else:
            print("No Path Found")

        return
