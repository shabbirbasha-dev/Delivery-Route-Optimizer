"""
Kepler.gl Visualization (GeoJSON)
---------------------------------
Fully working line + point map visualization.
"""

import pandas as pd
from keplergl import KeplerGl
import json


def visualize_route(df_locations: pd.DataFrame, route: list, output_html="optimized_route_map.html"):
    """
    Create a Kepler.gl map visualization using GeoJSON for paths and points.
    """

    points = []
    for _, row in df_locations.iterrows():
        points.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [row["longitude"], row["latitude"]],
            },
            "properties": {
                "name": row["name"],
                "id": int(row["location_id"])
            },
        })

    path_coords = []
    for loc_id in route:
        row = df_locations[df_locations["location_id"] == loc_id].iloc[0]
        path_coords.append([row["longitude"], row["latitude"]])

    route_line = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": path_coords
        },
        "properties": {"name": "Optimized Route"}
    }

    # ✅ Combine into GeoJSON
    geojson_data = {
        "type": "FeatureCollection",
        "features": points + [route_line]
    }

    # ✅ Create Kepler map
    map_ = KeplerGl(height=600)
    map_.add_data(data=geojson_data, name="Route Visualization")

    # ✅ Save HTML file
    map_.save_to_html(file_name=output_html)
    print(f" Interactive route map saved to: {output_html}")
