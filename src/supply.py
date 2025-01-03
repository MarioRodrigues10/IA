from enum import Enum

class SupplyType(Enum):
    """
    Enum to represent different types of supplies.
    Each supply type has a unique identifier.
    """
    Water = 0,
    Food = 1,
    Medicine = 2

def get_weight_volume_per_supply(supply_type):
    """
    Returns the weight and volume for a given supply type.

    :param supply_type: Type of supply (e.g., Water, Food, Medicine)
    :return: A tuple representing (weight, volume) for the given supply type
    """
    if supply_type == SupplyType.Water:
        return (1, 1)
    elif supply_type == SupplyType.Food:
        return (1.2, 1.2)
    elif supply_type == SupplyType.Medicine:
        return (0.5, 0.5)

class Supply:
    """
    Represents a supply item with a specific quantity and type.
    """
    def __init__(self, quantity, type):
        self.quantity = quantity
        self.type = type