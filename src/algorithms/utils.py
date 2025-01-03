from graph.node import Node

def manhattan_distance(p1, p2):
    """
    Calculates the Manhattan distance between two points (p1 and p2).
    
    The Manhattan distance is the sum of the absolute differences of the 
    x and y coordinates between the two points. It is commonly used in grid-based
    pathfinding algorithms.

    Args:
        p1 (Node or Position): The first point, either a Node object or a position object.
        p2 (Node or Position): The second point, either a Node object or a position object.

    Returns:
        int: The Manhattan distance between the two points.
    """
    if isinstance(p1, Node):
        p1 = p1.position
    if isinstance(p2, Node):
        p2 = p2.position

    return abs(p1.x - p2.x) + abs(p1.y - p2.y)