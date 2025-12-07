from collections import defaultdict

def dfs(graph, start, end, path=None, visited=None, verbose=False, visited_order=None, step_counter=None):
    """
    Depth-First Search implementation
    Args:
        graph: NetworkX graph object
        start: starting node
        end: ending node
        verbose: if True, print detailed information about visited nodes
    """
    if path is None:
        path = []
    if visited is None:
        visited = set()
    if visited_order is None:
        visited_order = []
    if step_counter is None:
        step_counter = {'count': 0}
        if verbose:
            print(f"\n--- DFS Traversal Details ---")
            print(f"Starting node: {start}")
            print(f"Target node: {end}")
            print(f"\nVisiting nodes in order:")
    
    path.append(start)
    visited.add(start)
    visited_order.append(start)
    step_counter['count'] += 1
    
    if verbose:
        print(f"Step {step_counter['count']}: Visit {start}")
    
    if start == end:
        if verbose:
            print(f"\n✓ Target node {end} found!")
            print(f"Total nodes visited: {len(visited_order)}")
            print(f"Nodes visited in order: {' -> '.join(visited_order)}")
        print(f"DFS path from {start} to {end}: {' -> '.join(path)}")
        print(f"Number of steps: {len(path) - 1}")
        return path, len(path) - 1, visited_order
    
    neighbors_list = list(graph.neighbors(start))
    if verbose:
        unvisited = [n for n in neighbors_list if n not in visited]
        if unvisited:
            print(f"  Exploring from {start}, unvisited neighbors: {unvisited}")
        else:
            print(f"  Backtracking from {start} (no unvisited neighbors)")
    
    for neighbor in neighbors_list:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, path.copy(), visited, verbose, visited_order, step_counter)
            if result[0] is not None:
                return result
    
    if verbose and step_counter['count'] == len(visited_order):
        print(f"\n✗ No path found")
        print(f"Total nodes visited: {len(visited_order)}")
        print(f"Nodes visited: {', '.join(visited_order)}")
    
    return None, None, visited_order