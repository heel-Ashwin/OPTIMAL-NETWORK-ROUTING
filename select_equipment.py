def select_equipment():
    # Input equipment specifications
    throughput = float(input("Enter desired throughput (Mbps): "))
    port_density = int(input("Enter desired port density: "))
    scalability = input("Does the equipment need to be scalable? (yes/no): ")

    selected_equipment = []

    # Example criteria for equipment selection
    if throughput >= 1000:
        selected_equipment.append("High-speed switches")
    else:
        selected_equipment.append("Standard switches")

    if port_density >= 24:
        selected_equipment.append("Switches with high port density")
    else:
        selected_equipment.append("Switches with standard port density")

    if scalability == "yes":
        selected_equipment.append("Scalable routers")
    else:
        selected_equipment.append("Non-scalable routers")
    if throughput / port_density >= 50:
        selected_equipment.append("High throughput density equipment")
    else:
        selected_equipment.append("Standard throughput density equipment")
    return selected_equipment
