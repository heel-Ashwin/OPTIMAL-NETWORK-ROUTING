def configure_monitoring_tool(network_topology, selected_equipment):
    # Generate configuration file for monitoring tool (e.g., Nagios, Zabbix)
    config = "# Configuration for network monitoring tool\n\n"
    config += "# Devices:\n"
    for node in network_topology.nodes:
        config += f"define host{{\n\tuse\tgeneric-switch\n\thost_name\t{node}\n\talias\t{node}\n\taddress\t{node}.example.com\n}}\n\n"

    config += "# Services:\n"
    for node in network_topology.nodes:
        for equipment in selected_equipment:
            config += f"define service{{\n\tservice_description\t{equipment}\n\thost_name\t{node}\n\tuse\tgeneric-service\n}}\n\n"

    return config
