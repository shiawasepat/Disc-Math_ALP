import heapq

def dijkstra_with_table(graph, start, end):
    """
    Dijkstra's algorithm implementation with step-by-step table
    Args:
        graph: NetworkX graph object
        start: starting node
        end: ending node
    Returns:
        tuple: (path, total_distance) or (None, None) if no path exists
    """
    nodes = list(graph.nodes())
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0
    previous = {}
    visited = set()
    
    pq = [(0, start)]
    
    # Print table header
    print(f"\nDijkstra's Algorithm Table (Start: {start}, End: {end})")
    print("=" * 80)
    header = f"{'Step':<6}{'Current':<10}{'Visited':<15}"
    for node in sorted(nodes):
        header += f"{node:<8}"
    print(header)
    print("-" * 80)
    
    step = 0
    
    # Initial state
    step += 1
    visited_str = "{" + start + "}"
    distances_str = ""
    for node in sorted(nodes):
        if distances[node] == float('inf'):
            distances_str += f"{'∞':<8}"
        else:
            distances_str += f"{distances[node]:<8}"
    
    print(f"{step:<6}{start:<10}{visited_str:<15}{distances_str}")
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        if current_node == end:
            break
        
        # Check neighbors and update distances
        updated = False
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                weight = graph[current_node][neighbor].get('weight', 1)
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
                    updated = True
        
        # Print updated state if any changes occurred
        if updated:
            step += 1
            visited_str = "{" + ", ".join(sorted(visited)) + "}"
            distances_str = ""
            for node in sorted(nodes):
                if distances[node] == float('inf'):
                    distances_str += f"{'∞':<8}"
                else:
                    distances_str += f"{distances[node]:<8}"
            
            print(f"{step:<6}{current_node:<10}{visited_str:<15}{distances_str}")
    
    print("=" * 80)
    
    # Reconstruct path
    if end not in previous and start != end:
        print(f"No path from {start} to {end}")
        return None, None
        
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous.get(current)
    path.reverse()
    
    print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
    print(f"Total distance: {distances[end]}")
    return path, distances[end]

def dijkstra(graph, start, end):
    """
    Standard Dijkstra's algorithm (without table)
    """
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    previous = {}
    visited = set()

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            break

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                weight = graph[current_node][neighbor].get('weight', 1)
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

    if end not in previous and start != end:
        print(f"No path exists between {start} and {end}")
        return None, None

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous.get(current)
    path.reverse()

    print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
    print(f"Total distance: {distances[end]}")
    return path, distances[end]