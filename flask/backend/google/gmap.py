import googlemaps
import os
from datetime import datetime

GMAPS_API_KEY = os.getenv("GMAPS_API_KEY")
print(GMAPS_API_KEY)

gmaps = googlemaps.Client(key=GMAPS_API_KEY)

geocode_result = gmaps.geocode('cassis')
