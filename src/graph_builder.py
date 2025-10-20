import pandas as pd
import networkx as nx
from math import radians, sin, cos, sqrt, atan2


def load_locations(file_path: str) -> pd.DataFrame:
    """Load delivery locations (lat/lon) from CSV."""
    df = pd.read_csv(file_path)
    print(f"✅ Loaded {len(df)} locations.")
    return df


def haversine(lat1, lon1, lat2, lon2):
    """Compute distance (km) between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def build_graph(df: pd.DataFrame) -> nx.Graph:
    """Build weighted graph where nodes = locations, edges = distances."""
    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_node(row["location_id"], name=row["name"], pos=(row["latitude"], row["longitude"]))

    for i, row1 in df.iterrows():
        for j, row2 in df.iterrows():
            if i < j:
                dist = haversine(row1["latitude"], row1["longitude"], row2["latitude"], row2["longitude"])
                G.add_edge(row1["location_id"], row2["location_id"], weight=dist)

    print(f"✅ Graph built with {len(G.nodes)} nodes and {len(G.edges)} edges.")
    return G
