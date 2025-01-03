from graph.node import Node
from graph.position import Position

class Graph:
    """
    A class representing a graph of nodes and edges.

    This class is used to store and manage a graph, where nodes are represented by positions,
    and edges represent connections between those positions.

    Attributes:
        nodes: A dictionary where keys are positions, and values are Node objects representing the nodes.
    """
    def __init__(self):
        """
        Initializes a new empty graph.
        """
        self.nodes = {}
        
    def add_node(self, position, id = 0):
        """
        Adds a node at the specified position to the graph.

        Args:
            position (Position): The position of the node.
            id (int, optional): The ID of the node. Defaults to 0.
        """
        if position not in self.nodes:
            self.nodes[position] = Node(position, id)

    def add_edge(self, pos1, pos2, open=True):
        """
        Adds an edge between two nodes in the graph.

        Args:
            pos1 (Position): The position of the first node.
            pos2 (Position): The position of the second node.
            open (bool, optional): Whether the edge is open or closed. Defaults to True.
        """
        if pos1 in self.nodes and pos2 in self.nodes:
            self.nodes[pos1].neighbours.append((self.nodes[pos2], open))
            self.nodes[pos2].neighbours.append((self.nodes[pos1], open))