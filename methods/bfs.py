from collections import deque

def bfs(graph, start, end, verbose=False):
    """
    Breadth-First Search implementation
    Args:
        graph: NetworkX graph object
        start: starting node
        end: ending node
        verbose: if True, print detailed information about visited nodes
    Returns:
        tuple: (path, number_of_steps, visited_order) or (None, None, None) if no path exists
    """
    if start not in graph.nodes() or end not in graph.nodes():
        print(f"Start node '{start}' or end node '{end}' not in graph")
        return None, None, None
    
    if start == end:
        print(f"Start and end are the same: {start}")
        return [start], 0, [start]
    
    # Initialize queue and visited set
    queue = deque([(start, [start])])  # (current_node, path_to_current_node)
    visited = {start}
    visited_order = [start]  # Track order of visits
    
    if verbose:
        print(f"\n--- BFS Traversal Details ---")
        print(f"Starting node: {start}")
        print(f"Target node: {end}")
        print(f"\nVisiting nodes in order:")
        print(f"Step 1: Visit {start} (start node)")
    
    step = 1
    while queue:
        current_node, path = queue.popleft()
        
        # Check all neighbors
        neighbors_list = list(graph.neighbors(current_node))
        if verbose:
            print(f"\nExploring from {current_node}, neighbors: {neighbors_list}")
        
        for neighbor in neighbors_list:
            if neighbor not in visited:
                new_path = path + [neighbor]
                visited.add(neighbor)
                visited_order.append(neighbor)
                step += 1
                
                if verbose:
                    print(f"Step {step}: Visit {neighbor} (from {current_node})")
                
                # Found the target
                if neighbor == end:
                    if verbose:
                        print(f"\n✓ Target node {end} found!")
                        print(f"Total nodes visited: {len(visited_order)}")
                        print(f"Nodes visited in order: {' -> '.join(visited_order)}")
                    print(f"BFS path from {start} to {end}: {' -> '.join(new_path)}")
                    print(f"Number of steps: {len(new_path) - 1}")
                    return new_path, len(new_path) - 1, visited_order
                
                # Add to queue for further exploration
                queue.append((neighbor, new_path))
    
    # No path found
    if verbose:
        print(f"\n✗ No path found")
        print(f"Total nodes visited: {len(visited_order)}")
        print(f"Nodes visited: {', '.join(visited_order)}")
    print(f"No path exists between {start} and {end}")
    return None, None, visited_order

def bfs_all_paths(graph, start):
    """
    BFS to find shortest path from start to all reachable nodes
    Args:
        graph: NetworkX graph object
        start: starting node
    Returns:
        dict: {node: (path, distance)}
    """
    if start not in graph.nodes():
        print(f"Start node '{start}' not in graph")
        return {}
    
    # Initialize
    queue = deque([(start, [start], 0)])  # (node, path, distance)
    visited = {start}
    paths = {start: ([start], 0)}
    
    while queue:
        current_node, path, distance = queue.popleft()
        
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_distance = distance + 1
                
                visited.add(neighbor)
                paths[neighbor] = (new_path, new_distance)
                queue.append((neighbor, new_path, new_distance))
    
    return paths