import networkx as nx

def show_graph_degree(graph):
    """
    Display degree information for all nodes in the graph
    Args:
        graph: NetworkX graph object
    """
    print("\n" + "="*70)
    print(" "*25 + "GRAPH DEGREE ANALYSIS")
    print("="*70)
    
    # Check if graph is directed
    is_directed = graph.is_directed()
    
    if is_directed:
        print("\nGraph Type: DIRECTED")
        print("\n{:<10} {:<15} {:<15} {:<15}".format("Node", "In-Degree", "Out-Degree", "Total Degree"))
        print("-"*70)
        
        for node in sorted(graph.nodes()):
            in_degree = graph.in_degree(node)
            out_degree = graph.out_degree(node)
            total_degree = in_degree + out_degree
            print("{:<10} {:<15} {:<15} {:<15}".format(node, in_degree, out_degree, total_degree))
        
        print("\nDegree Statistics:")
        print(f"  Average In-Degree: {sum(dict(graph.in_degree()).values()) / len(graph.nodes()):.2f}")
        print(f"  Average Out-Degree: {sum(dict(graph.out_degree()).values()) / len(graph.nodes()):.2f}")
        
        # Find nodes with highest degrees
        max_in = max(graph.in_degree(), key=lambda x: x[1])
        max_out = max(graph.out_degree(), key=lambda x: x[1])
        print(f"  Highest In-Degree: {max_in[0]} ({max_in[1]})")
        print(f"  Highest Out-Degree: {max_out[0]} ({max_out[1]})")
    
    else:
        print("\nGraph Type: UNDIRECTED")
        print("\n{:<10} {:<15}".format("Node", "Degree"))
        print("-"*70)
        
        for node in sorted(graph.nodes()):
            degree = graph.degree(node)
            print("{:<10} {:<15}".format(node, degree))
        
        print("\nDegree Statistics:")
        print(f"  Average Degree: {sum(dict(graph.degree()).values()) / len(graph.nodes()):.2f}")
        print(f"  Total Edges: {graph.number_of_edges()}")
        
        # Find node with highest degree
        max_degree = max(graph.degree(), key=lambda x: x[1])
        print(f"  Highest Degree: {max_degree[0]} ({max_degree[1]})")
    
    print("="*70)

def show_graph_properties(graph):
    """
    Display general properties of the graph
    Args:
        graph: NetworkX graph object
    """
    print("\n" + "="*70)
    print(" "*22 + "GRAPH PROPERTIES ANALYSIS")
    print("="*70)
    
    print(f"\n{'Property':<30} {'Value':<20}")
    print("-"*70)
    
    # Basic properties
    print(f"{'Graph Type':<30} {'Directed' if graph.is_directed() else 'Undirected':<20}")
    print(f"{'Number of Nodes':<30} {graph.number_of_nodes():<20}")
    print(f"{'Number of Edges':<30} {graph.number_of_edges():<20}")
    
    # Connectivity
    if graph.is_directed():
        is_connected = nx.is_weakly_connected(graph)
        print(f"{'Weakly Connected':<30} {'Yes' if is_connected else 'No':<20}")
        is_strongly_connected = nx.is_strongly_connected(graph)
        print(f"{'Strongly Connected':<30} {'Yes' if is_strongly_connected else 'No':<20}")
    else:
        is_connected = nx.is_connected(graph)
        print(f"{'Connected':<30} {'Yes' if is_connected else 'No':<20}")
    
    # Density
    density = nx.density(graph)
    print(f"{'Graph Density':<30} {density:<20.4f}")
    
    # Check for cycles
    try:
        cycles = list(nx.simple_cycles(graph)) if graph.is_directed() else list(nx.cycle_basis(graph))
        has_cycles = len(cycles) > 0
        print(f"{'Has Cycles':<30} {'Yes' if has_cycles else 'No':<20}")
    except:
        print(f"{'Has Cycles':<30} {'Unable to determine':<20}")
    
    print("="*70)

def show_node_neighbors(graph, node):
    """
    Display neighbors of a specific node
    Args:
        graph: NetworkX graph object
        node: node to analyze
    """
    if node not in graph.nodes():
        print(f"Node '{node}' not found in graph!")
        return
    
    print("\n" + "="*70)
    print(f" "*20 + f"NEIGHBORS OF NODE '{node}'")
    print("="*70)
    
    neighbors = list(graph.neighbors(node))
    
    if not neighbors:
        print(f"\nNode '{node}' has no neighbors.")
    else:
        print(f"\nNode '{node}' has {len(neighbors)} neighbor(s):")
        
        for neighbor in neighbors:
            # Get edge weight if it exists
            if graph.has_edge(node, neighbor):
                weight = graph[node][neighbor].get('weight', 'N/A')
                print(f"  → {neighbor} (weight: {weight})")
    
    print("="*70)

def show_all_analytics(graph):
    """
    Display all analytics: degree, properties, and detailed information
    Args:
        graph: NetworkX graph object
    """
    show_graph_degree(graph)
    print("\n")
    show_graph_properties(graph)