import networkx as nx

def greedy_route_optimizer(G: nx.Graph, start_node: int):
    """
    Compute a delivery route using a greedy nearest-neighbor heuristic.
    - Start at warehouse (start_node)
    - Always move to the nearest unvisited location
    """
    visited = [start_node]
    total_distance = 0
    current = start_node

    while len(visited) < len(G.nodes):
        nearest = None
        shortest_distance = float('inf')

        for neighbor in G.nodes:
            if neighbor not in visited:
                try:
                    dist = nx.dijkstra_path_length(G, current, neighbor, weight='weight')
                    if dist < shortest_distance:
                        shortest_distance = dist
                        nearest = neighbor
                except nx.NetworkXNoPath:
                    continue

        if nearest is None:
            break  # No reachable nodes left

        visited.append(nearest)
        total_distance += shortest_distance
        current = nearest

    print(f"✅ Greedy route complete: {visited}")
    print(f"🛣️  Total Distance: {total_distance:.2f} km")

    return visited, total_distance
