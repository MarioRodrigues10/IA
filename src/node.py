class Node:
    def __init__(self, position, neighbours):
        self.position = position
        self.neighbours = neighbours # [(node: Node, open: bool)]