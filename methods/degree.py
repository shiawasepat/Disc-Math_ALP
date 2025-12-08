import networkx as nx

def show_graph_degree(graph):
    """
    Display degree information for all nodes in the graph
    Args:
        graph: NetworkX graph object
    """
    print("\n" + "="*60)
    print(" "*20 + "GRAPH DEGREE ANALYSIS")
    print("="*60)
    
    # Check if graph is directed
    is_directed = graph.is_directed()
    
    if is_directed:
        print("\nGraph Type: DIRECTED")
        print("\n{:<10} {:<15} {:<15} {:<15}".format("Node", "In-Degree", "Out-Degree", "Total Degree"))
        print("-"*60)
        
        for node in sorted(graph.nodes()):
            in_degree = graph.in_degree(node)
            out_degree = graph.out_degree(node)
            total_degree = in_degree + out_degree
            print("{:<10} {:<15} {:<15} {:<15}".format(node, in_degree, out_degree, total_degree))
        
        print("\nDegree Statistics:")
        # Find nodes with highest degrees
        max_in = max(graph.in_degree(), key=lambda x: x[1])
        max_out = max(graph.out_degree(), key=lambda x: x[1])
        print(f"  Highest In-Degree: {max_in[0]} ({max_in[1]})")
        print(f"  Highest Out-Degree: {max_out[0]} ({max_out[1]})")
    
    else:
        print("\nGraph Type: UNDIRECTED")
        print("\n{:<10} {:<15}".format("Node", "Degree"))
        print("-"*60)
        
        for node in sorted(graph.nodes()):
            degree = graph.degree(node)
            print("{:<10} {:<15}".format(node, degree))
        
        # Find node with highest degree
        max_degree = max(graph.degree(), key=lambda x: x[1])
        print(f"\nHighest Degree: {max_degree[0]} ({max_degree[1]})")
    
    print("="*60)

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