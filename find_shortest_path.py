def find_shortest_path(G, source, target):
    # Use Dijkstra's algorithm to find the shortest path
    shortest_path = nx.shortest_path(G, source=source, target=target)
    return shortest_path
