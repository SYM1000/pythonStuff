import pandas as pd
import gmplot
from IPython.display import display


raw_data = pd.read_csv("/Users/santiagoyeomans/desktop/Addresses_in_the_City_of_Los_Angeles.csv")

"""
display(raw_data.head(n = 5))
display(raw_data.info())
"""

data = raw_data.head(n=15000)

latitudes = data["LAT"]
longitudes = data["LON"]

gmap = gmplot.GoogleMapPlotter(34.0522, -118.2437, 10)

gmap.heatmap(latitudes, longitudes)

gmap.draw("my_heatmap.html")
