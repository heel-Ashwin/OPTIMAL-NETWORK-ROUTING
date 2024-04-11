def create_topology(num_nodes, topology_type):
    if topology_type == "star":
        # Create a star network topology
        G = nx.star_graph(num_nodes - 1)  # Example with num_nodes - 1 nodes
    elif topology_type == "mesh":
        # Create a mesh network topology
        G = nx.grid_2d_graph(num_nodes, num_nodes)  # Example with num_nodes x num_nodes grid
    elif topology_type == "bus":
        # Create a bus network topology
        G = nx.path_graph(num_nodes)  # Example with num_nodes nodes
    elif topology_type == "ring":
        # Create a ring network topology
        G = nx.cycle_graph(num_nodes)  # Example with num_nodes nodes
    else:
        # Default to a simple star network topology
        print("Invalid topology type. Defaulting to star network topology.")
        G = nx.star_graph(num_nodes - 1)  # Example with num_nodes - 1 nodes
    
    return G
