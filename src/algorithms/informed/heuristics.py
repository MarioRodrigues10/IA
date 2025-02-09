from algorithms.utils import manhattan_distance
from supply import SupplyType, get_weight_volume_per_supply
from vehicle import VehicleStatus

# Heuristic based on Manhattan distance
def manhattan_heuristic(p1, p2, state, end_point):
    """
    Estimates the cost between two points using Manhattan distance.

    Args:
        p1 (Point): The starting point.
        p2 (Point): The destination point.
        state (object): The current state of the simulation.
        end_point (object): The end node representing the delivery destination.

    Returns:
        float: The Manhattan distance between the two points.
    """
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Heuristic to estimate the minimum time to traverse between points
def time_estimation_heuristic(p1, p2, state, end_point):
    """
    Estimates the minimum time required to travel between two points.

    Args:
        p1 (Point): The starting point.
        p2 (Point): The destination point.
        state (object): The current state of the simulation, including available vehicles.
        end_point (object): The end node representing the delivery destination.

    Returns:
        float: The estimated time based on vehicle speed or infinity if no vehicles are available.
    """
    min_time = float('inf')
    for vehicle in state.vehicles:
        if vehicle.vehicle_status == VehicleStatus.IDLE:
            distance = manhattan_distance(p1, p2)
            time = distance / vehicle.type.average_velocity
            min_time = min(min_time, time)
    return min_time if min_time != float('inf') else float('inf')

# Heuristic to account for blocked routes
def blocked_route_heuristic(p1, p2, state, end_point):
    """
    Adds a penalty to the heuristic for routes that are blocked.

    Args:
        p1 (Point): The starting point.
        p2 (Point): The destination point.
        state (object): The current state of the simulation.
        end_point (object): The end node representing the delivery destination.

    Returns:
        float: The heuristic value including penalties for blocked routes.
    """
    penalty = 0
    current_node = state.graph.nodes.get(p1)
    if current_node:
        for _, is_open in current_node.neighbours:
            if not is_open:
                penalty += 10  # Arbitrary penalty value for blocked routes
    return manhattan_distance(p1, p2) + penalty

# Heuristic to prioritize addressing supply deficits dynamically
def dynamic_supply_priority_heuristic(p1, p2, state, end_point):
    """
    Adjusts the heuristic dynamically based on the supply deficits at the destination.

    Args:
        p1 (Point): The starting point.
        p2 (Point): The destination point.
        state (object): The current state of the simulation.
        end_point (object): The end node representing the delivery destination.

    Returns:
        float: The heuristic value adjusted for supply deficits.
    """
    supplies_needed = end_point.get_supplies_needed()
    critical_penalty = 0
    for supply_type, quantity in supplies_needed.items():
        for supply in state.start_point.supplies:
            if supply.type.name == supply_type and supply.quantity < quantity:
                critical_penalty += (quantity - supply.quantity) * 5  # Arbitrary penalty multiplier
    return manhattan_distance(p1, p2) + critical_penalty

# Heuristic to estimate the probability of delivery success
def delivery_success_probability_heuristic(p1, p2, state, end_point):
    """
    Penalizes the heuristic based on the probability of successful delivery.

    Args:
        p1 (Point): The starting point.
        p2 (Point): The destination point.
        state (object): The current state of the simulation, including vehicles and supplies.
        end_point (object): The end node representing the delivery destination.

    Returns:
        float: A penalty inversely proportional to the estimated delivery success probability.
    """
    supplies_needed = end_point.get_supplies_needed()
    total_weight_needed = sum(
        quantity * get_weight_volume_per_supply(SupplyType[supply_type])[0]
        for supply_type, quantity in supplies_needed.items()
    )
    total_volume_needed = sum(
        quantity * get_weight_volume_per_supply(SupplyType[supply_type])[1]
        for supply_type, quantity in supplies_needed.items()
    )

    total_distance = manhattan_distance(p1, p2)
    success_probability = 0

    for vehicle in state.vehicles:
        if vehicle.vehicle_status == VehicleStatus.IDLE and vehicle.current_fuel >= total_distance:
            weight_available = vehicle.type.weight_capacity - vehicle.current_weight
            volume_available = vehicle.type.volume_capacity - vehicle.current_volume

            weight_factor = min(1, weight_available / total_weight_needed)
            volume_factor = min(1, volume_available / total_volume_needed)
            success_probability = max(success_probability, weight_factor * volume_factor)

    return (1 - success_probability) * 100  # Penalty inversely proportional to success probability

# Final combined heuristic combining various factors
def final_combined_heuristic(p1, p2, state, end_point):
    """
    Combines multiple heuristics to estimate the cost between two points.

    Args:
        p1 (Point): The starting point.
        p2 (Point): The destination point.
        state (object): The current state of the simulation.
        end_point (object): The end node representing the delivery destination.

    Returns:
        float: The combined heuristic value considering distance, time, blockages, supply deficits, and delivery success probability.
    """

    manhattan_cost = manhattan_heuristic(p1, p2, state, end_point)
    time_cost = time_estimation_heuristic(p1, p2, state, end_point)
    block_cost = blocked_route_heuristic(p1, p2, state, end_point)
    supply_cost = dynamic_supply_priority_heuristic(p1, p2, state, end_point)
    success_cost = delivery_success_probability_heuristic(p1, p2, state, end_point)

    return manhattan_cost + time_cost + block_cost + supply_cost + success_cost
