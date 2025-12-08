import networkx as nx
import os
import matplotlib.pyplot as plt
from methods.dijkstra import dijkstra, dijkstra_with_table
from methods.bfs import bfs
from methods.dfs import dfs
from methods.degree import show_graph_degree, show_all_analytics

def wait_for_user():
    input("\nPress 'Enter' to continue...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Graf:
    def __init__(self, directed=False):
        if directed:
            self.graph = nx.DiGraph()
            self.is_directed = True
        else:
            self.graph = nx.Graph()
            self.is_directed = False

    # Add node to the graph
    def add_node(self, node):
        self.graph.add_node(node)

    # Add edge with optional weight
    def add_edge(self, node1, node2, weight=None):
        if weight is not None:
            self.graph.add_edge(node1, node2, weight=weight)
        else:
            self.graph.add_edge(node1, node2)
    
    def add_directed_edge(self, from_node, to_node, weight=None):
        """Add a directed edge (only works if graph is directed)"""
        if not self.is_directed:
            print("Warning: This is an undirected graph. Use add_edge() instead.")
            return
        
        if weight is not None:
            self.graph.add_edge(from_node, to_node, weight=weight)
        else:
            self.graph.add_edge(from_node, to_node)

    def shortest_path(self, start, end):
        try:
            path = nx.shortest_path(self.graph, start, end, weight='weight')
            length = nx.shortest_path_length(self.graph, start, end, weight='weight')
            print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
            print(f"Total distance: {length}")
            return path, length
        except nx.NetworkXNoPath:
            print(f"No path exists between {start} and {end}")
            return None, None

    def dijkstra(self, start, end):
        """Use external Dijkstra implementation"""
        return dijkstra(self.graph, start, end)
    
    def dijkstra_with_table(self, start, end):
        """Use external Dijkstra implementation with table"""
        return dijkstra_with_table(self.graph, start, end)

    def bfs(self, start, end, verbose=False):
        """Use external BFS implementation"""
        return bfs(self.graph, start, end, verbose)

    def dfs(self, start, end, verbose=False):
        """Use external DFS implementation"""
        return dfs(self.graph, start, end, verbose=verbose)

    def display(self, path=None, show_weights=True):
        """Basic display method for compatibility"""
        self.visualize(path, show_weights)

    def visualize(self, path=None, show_weights=True):
        pos = nx.spring_layout(self.graph)
        
        # Default colors
        node_colors = ['lightblue'] * len(self.graph.nodes())
        edge_colors = ['black'] * len(self.graph.edges())
        
        # Highlight path if provided
        if path:
            # Highlight path nodes in red
            for node in path:
                node_index = list(self.graph.nodes()).index(node)
                node_colors[node_index] = 'red'
            
            # Highlight path edges in red
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            for edge in path_edges:
                if edge in self.graph.edges():
                    edge_index = list(self.graph.edges()).index(edge)
                    edge_colors[edge_index] = 'red'
                elif (edge[1], edge[0]) in self.graph.edges():
                    edge_index = list(self.graph.edges()).index((edge[1], edge[0]))
                    edge_colors[edge_index] = 'red'
        
        # Draw the graph with arrows for directed graphs
        if self.is_directed:
            nx.draw(self.graph, pos, with_labels=True, node_color=node_colors,
                    edge_color=edge_colors, node_size=500, font_size=14, 
                    font_weight='bold', width=2, arrows=True, arrowsize=20,
                    arrowstyle='->')
        else:
            nx.draw(self.graph, pos, with_labels=True, node_color=node_colors,
                    edge_color=edge_colors, node_size=500, font_size=14, 
                    font_weight='bold', width=2)
        
        # Draw edge labels with weights only if show_weights is True
        if show_weights:
            edge_labels = nx.get_edge_attributes(self.graph, 'weight')
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        
        # Add title to show graph type
        graph_type = "Directed" if self.is_directed else "Undirected"
        plt.title(f"{graph_type} Graph", fontsize=16, fontweight='bold')
        
        plt.show()
    
def handle_pathfinding_choice(g, algorithm_method, algorithm_name):
    """Helper function to handle pathfinding choices"""
    start = input("Enter start node: ").upper()
    end = input("Enter end node: ").upper()
    
    if start in g.graph.nodes() and end in g.graph.nodes():
        # Ask user for output preference
        print("\nOutput options:")
        print("1. Show detailed text output only")
        print("2. Show visualization only")
        print("3. Show both text output and visualization")
        
        output_choice = input("Choose output type (1-3): ")
        
        verbose = output_choice in ['1', '3']
        show_viz = output_choice in ['2', '3']
        
        # Call algorithm with verbose flag if supported
        if algorithm_name in ["BFS", "DFS"]:
            clear_screen()
            result = algorithm_method(start, end, verbose=verbose)
        else:
            result = algorithm_method(start, end)
        
        if result[0]:  # path exists
            if show_viz:
                g.display(result[0])
        elif not verbose:
            print("No path found or algorithm returned no result.")
    else:
        print("Invalid nodes! Please enter nodes from: A, B, C, D, E")

def show_additional_methods_menu(g):
    """Show sub-menu for additional methods"""
    while True:
        clear_screen()
        print("--- Additional Methods ---")
        print("1. BFS (Breadth-First Search)")
        print("2. DFS (Depth-First Search)")
        print("3. Dijkstra with Table")
        print("4. Back to Main Menu")
        
        sub_choice = input("Enter your choice (1-5): ")
        
        match sub_choice:
            case '1':
                clear_screen()
                handle_pathfinding_choice(g, g.bfs, "BFS")
                wait_for_user()

            case '2':
                clear_screen()
                handle_pathfinding_choice(g, g.dfs, "DFS")
                wait_for_user()

            case '3':
                clear_screen()
                handle_pathfinding_choice(g, g.dijkstra_with_table, "Dijkstra with table")
                wait_for_user()

            case '4':
                clear_screen()
                break
            
def create_undirected_graph():
    """Create sample undirected graph"""
    g = Graf(directed=False)
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')
    g.add_node('G')

    # Add edges with weights
    g.add_edge('A', 'B', weight=2)
    g.add_edge('A', 'C', weight=5)
    g.add_edge('B', 'D', weight=4)
    g.add_edge('B', 'E', weight=6)
    g.add_edge('C', 'F', weight=3)
    g.add_edge('D', 'G', weight=2)
    g.add_edge('E', 'F', weight=4)
    g.add_edge('F', 'G', weight=1)
    
    return g

def create_directed_graph():
    """Create sample directed graph"""
    g = Graf(directed=True)
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')

    g.add_directed_edge('A', 'B')
    g.add_directed_edge('A', 'C')
    g.add_directed_edge('B', 'D')
    g.add_directed_edge('C', 'E')
    g.add_directed_edge('C', 'F')
    g.add_directed_edge('D', 'E')
    g.add_directed_edge('E', 'F')  # Creates a cycle
    
    return g

if __name__ == "__main__":
    clear_screen()
    print("=== WELCOME TO THE GRAPH ANALYSIS TOOL ===")
    # Let user choose graph type
    
    print("\n=== GRAPH SELECTION ===")
    print("1. Undirected Graph")
    print("2. Directed Graph")
    
    graph_choice = input("Choose graph type (1-2): ")
    
    match graph_choice:
        case '1':
            g = create_undirected_graph()
            print("Undirected graph created with nodes A, B, C, D, E")
        case '2':
            g = create_directed_graph()
            print("Directed graph created with nodes A, B, C, D, E")
        case _:
            print("Invalid choice. Creating undirected graph by default.")
            g = create_undirected_graph()
    
    while True:
        # Main menu
        graph_type = "Directed" if g.is_directed else "Undirected"
        print(f"=== {graph_type.upper()} GRAPH ANALYSIS MENU ===")
        print("1. Display Graph (basic)")
        print("2. Display Weighted Graph")
        print("3. Find Shortest Path (Dijkstra)")
        print("4. Additional Methods (BFS, DFS, etc.)")
        print("5. Show Graph Analytics")
        print("6. Switch Graph Type")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        match choice:
            case '1':
                print("Displaying basic graph...")
                g.display(show_weights=False)
            
            case '2':
                print("Displaying weighted graph...")
                g.display(show_weights=True)
            
            case '3':
                handle_pathfinding_choice(g, g.dijkstra, "Dijkstra")
            
            case '4':
                clear_screen()
                show_additional_methods_menu(g)

            case '5':
                clear_screen()
                show_all_analytics(g.graph)
                wait_for_user()
            
            case '6':
                print("=== GRAPH SELECTION ===")
                print("1. Undirected Graph")
                print("2. Directed Graph")
                
                new_choice = input("Choose graph type (1-2): ")
                
                match new_choice:
                    case '1':
                        g = create_undirected_graph()
                        print("Switched to undirected graph")
                    case '2':
                        g = create_directed_graph()
                        print("Switched to directed graph")
                    case _:
                        print("Invalid choice. Keeping current graph.")
            
            case '7':
                print("Goodbye!")
                break
            
            case _:
                print("Invalid choice! Please try again.")