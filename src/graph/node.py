from graph.position import Position

class Node:
    """
    A class representing a node in a graph.

    Each node is associated with a position, has a list of neighbours (connected nodes),
    and tracks accessible terrains. It also provides functionality to check whether a node
    can be accessed under certain terrain and weather conditions.

    Attributes:
        id (int): The unique identifier for the node.
        position (Position): The position of the node in the graph.
        neighbours (list): A list of tuples representing neighbouring nodes and their open status.
        accessible_terrains (list): A list of terrain types that the node can access (0, 1, 2).
    """
    def __init__(self, position, id):
        """
        Initializes a new node with a specified position and ID.

        Args:
            position (Position): The position of the node.
            id (int): The unique identifier for the node.
        """
        self.id = id
        self.position = position
        self.neighbours = []  # List of tuples (Node, open: bool)
        self.accessible_terrains = [0,1,2] # List of Terrain

    def can_access_terrain(self, terrain, weather):
        """
        Checks if the node can be accessed given the terrain and weather conditions.

        Args:
            terrain (int): The type of terrain to check (e.g., 0, 1, 2).
            weather (Weather): A weather object used to determine if the node is blocked.

        Returns:
            bool: True if the node is accessible under the given terrain and weather conditions, 
                  otherwise False.
        """
        return terrain in self.accessible_terrains and not weather.blocked_position(Position(self.position.x, self.position.y))