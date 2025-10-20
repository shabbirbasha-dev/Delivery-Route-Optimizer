"""
Delivery Route Optimizer
Main Runner File
"""

from graph_builder import load_locations, build_graph
from dijkstra import dijkstra_shortest_path
from optimizer import greedy_route_optimizer
from visualize import visualize_route

if __name__ == "__main__":
    # Load dataset
    data_path = "data/locations.csv"
    locations_df = load_locations(data_path)

    # Build graph
    graph = build_graph(locations_df)

    # Test Dijkstra (between Warehouse and one customer)
    source, target = 1, 5
    path, dist = dijkstra_shortest_path(graph, source, target)
    print(f"\n📦 Shortest Path {source} → {target}: {path} ({dist:.2f} km)")

    # Run Greedy Route Optimizer
    print("\n🚚 Running Greedy Route Optimization...\n")
    route, total = greedy_route_optimizer(graph, start_node=1)
    print(f"📍 Final Route: {route}")
    print(f"🧭 Total Distance: {total:.2f} km")

    # Visualize the optimized route
    visualize_route(locations_df, route)