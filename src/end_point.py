class EndPoint:
    """
    Represents an endpoint in the simulation with a position, supplies needed, and priority.
    """

    def __init__(self, position, supplies_needed, priority):
        """
        Initializes the endpoint with its position, required supplies, and priority level.
        
        :param position: Position object representing the endpoint's location
        :param supplies_needed: Dictionary of supplies needed (key: supply type, value: quantity)
        :param priority: Priority level of the endpoint
        """
        self.position = position
        self.supplies_needed = supplies_needed
        self.priority = priority

    def get_supplies_needed(self):
        """
        Returns the supplies that are still needed at the endpoint (quantity > 0).
        
        :return: Dictionary of required supplies
        """
        return {supply_type: quantity for supply_type, quantity in self.supplies_needed.items() if quantity > 0}
    
    def satisfy_supplies(self, supplies):
        """
        Satisfies the supply needs of the endpoint based on the provided supplies.
        
        :param supplies: List of supply objects (each having a type and quantity)
        """
        for supply in supplies:
            if supply.type.name in self.supplies_needed:
                self.supplies_needed[supply.type.name] = max(0, self.supplies_needed[supply.type.name] - supply.quantity)

