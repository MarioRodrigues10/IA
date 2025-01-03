from enum import Enum

class WeatherCondition(Enum):
    """
    Enum representing different weather conditions.
    """
    SUNNY = 0
    RAINY = 1
    SNOWY = 2
    STORM = 3

class Weather:
    """
    Class for managing weather conditions in the simulation.
    """
    def __init__(self):
        self.conditions = {}

    def set_condition(self, position, condition):
        self.conditions[position] = condition

    def get_condition(self, position):
        return self.conditions.get(position)
    
    def blocked_position(self, position):
        return self.conditions[position] == WeatherCondition.STORM