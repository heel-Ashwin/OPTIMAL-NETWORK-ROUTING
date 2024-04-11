if "feasible" in feasibility_result:
    # Input the number of nodes
    num_nodes = int(input("Enter the number of nodes: "))
    
    # Input the type of topology
    topology_type = input("Enter the type of network topology (star/mesh/bus/ring): ")

    # Create the network topology
    network_topology = create_topology(num_nodes, topology_type)

    # Visualize the network topology
    visualize_topology(network_topology)

    # Select equipment based on specifications
    selected_equipment = select_equipment()

    # Print selected equipment
    print("\nSelected Equipment:")
    for equipment in selected_equipment:
        print("- " + equipment)

    # Configure security measures
    firewall_config, encryption_config, acl_config = configure_security_measures(network_topology)
    print("\nFirewall Configuration:")
    print(firewall_config)
    print("\nEncryption Configuration:")
    print(encryption_config)
    print("\nACL Configuration:")
    print(acl_config)

    # Generate configuration for monitoring tool
    monitoring_config = configure_monitoring_tool(network_topology, selected_equipment)
    print("\nMonitoring Tool Configuration:\n")
    print(monitoring_config)

    # Find the shortest path between nodes
    source = input("\nEnter source node: ")
    target = input("Enter target node: ")
    shortest_path = find_shortest_path(network_topology, source, target)
    print("\nShortest Path:", shortest_path)

