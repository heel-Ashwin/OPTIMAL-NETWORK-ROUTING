def visualize_topology(G):
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_size=10, font_weight='bold')
    plt.title("Network Topology")
    plt.show()
