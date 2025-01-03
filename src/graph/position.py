class Position:
    """
    A class to represent a position with x and y coordinates.

    Attributes:
        x (int or float): The x-coordinate of the position.
        y (int or float): The y-coordinate of the position.

    Methods:
        __str__(): 
            Returns a string representation of the position in the format (x, y).
        
        __hash__(): 
            Returns a hash value for the position, allowing it to be used as a dictionary key.
        
        __eq__(other): 
            Compares the current position to another position for equality.
        
        __lt__(other): 
            Compares the current position to another position to determine if it is "less than" the other, based on the (x, y) values.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Position):
            return (self.x, self.y) < (other.x, other.y)
        return False
