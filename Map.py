#import Library
import folium
import pandas as pd
from folium.plugins import MarkerCluster
#load Data
data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']


# Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')

# create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start= 5, tiles = "CartoDB dark_matter")


# Create Cluster
marker_cluster = MarkerCluster().add_to(map)

# Plotting Markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)


# Save the map
map.save("map1.html")


