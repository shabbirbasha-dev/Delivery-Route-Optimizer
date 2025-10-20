import networkx as nx

def dijkstra_shortest_path(G: nx.Graph, source: int, target: int):
    """Find the shortest path and distance using Dijkstra’s algorithm."""
    try:
        path = nx.dijkstra_path(G, source, target, weight='weight')
        distance = nx.dijkstra_path_length(G, source, target, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        print("❌ No path found between nodes.")
        return [], float('inf')
