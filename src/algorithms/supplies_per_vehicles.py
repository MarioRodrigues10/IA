import supply as sp
import vehicle as vh
from collections import defaultdict

def split_supplies_per_vehicle(vehicles, supplies):
    """
    Distributes supplies among vehicles based on each vehicle's weight and volume capacity.

    For each supply, the function checks if the vehicle can carry the supply's weight and volume.
    If it can, the supply is assigned to that vehicle.

    Args:
        vehicles (list): List of available vehicles.
        supplies (list): List of supplies to be distributed.

    Returns:
        list: A list of supplies assigned to each vehicle.
    """
    supply_type_data = defaultdict(lambda: None)
    supplies_per_vehicle = [[] for _ in range(len(vehicles))]
    
    for supply in supplies:
        if supply.type not in supply_type_data:
            supply_type_data[supply.type] = sp.get_weight_volume_per_supply(supply.type)
        
        supply_weight, supply_volume = supply_type_data[supply.type]
        total_supply_weight = supply_weight * supply.quantity
        total_supply_volume = supply_volume * supply.quantity
        
        for i, vehicle in enumerate(vehicles):
            if (vehicle.current_weight + total_supply_weight <= vehicle.type.weight_capacity and
                vehicle.current_volume + total_supply_volume <= vehicle.type.volume_capacity):
                
                vehicle.current_weight += total_supply_weight
                vehicle.current_volume += total_supply_volume
                supplies_per_vehicle[i].append(supply)
                break 

    return supplies_per_vehicle
