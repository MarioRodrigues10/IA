import json
from end_point import EndPoint
from geography.geography import load_map_data_to_graph
from graph.position import Position
from start_point import StartPoint
from supply import Supply, SupplyType
from vehicle import Vehicle, VehicleStatus, VehicleType
from weather import Weather, WeatherCondition

class State:
    """
    Represents the current state of the simulation, including time, vehicles, start point, end points, 
    geographical graph, and weather conditions.
    """
    def __init__(self, time, vehicles, start_point, end_points, graph, weather):
        self.time = time
        self.vehicles = vehicles
        self.start_point = start_point
        self.end_points = end_points
        self.graph = graph
        self.weather = weather

def load_dataset(dataset_path):
    """
    Loads and processes the dataset to initialize the state of the simulation.
    
    :param dataset_path: Path to the JSON dataset file
    :return: An instance of the State class representing the simulation state
    """
    with open(dataset_path, 'r') as file:
        dataset = json.load(file)

    geography = dataset['geography']
    graph = load_map_data_to_graph(geography)
    weather = Weather()

    for node in graph.nodes.values():    
        weather.set_condition(Position(node.position.x, node.position.y), WeatherCondition.SUNNY)

    start_position = Position(*dataset['start_point']['position'])
    supplies = [Supply(s['quantity'], SupplyType[s['type']]) for s in dataset['start_point']['supplies']]
    start_point = StartPoint(start_position, supplies)

    end_points = [EndPoint(Position(*ep['position']), ep['needs_supplies'], ep['priority']) for ep in dataset['end_points']]

    vehicles = []
    for vehicle in dataset['vehicles']:
        vehicle_position = Position(*vehicle['position'])
        vehicle_type = VehicleType(
            vehicle['type']['name'],
            vehicle['type']['transportation'],
            vehicle['type']['fuel_capacity'],
            vehicle['type']['weight_capacity'],
            vehicle['type']['volume_capacity'],
            vehicle['type']['average_velocity']
        )
        vehicle = Vehicle(
            vehicle['id'], vehicle_position, vehicle_type, vehicle['current_fuel'],
            vehicle['current_weight'], vehicle['current_volume'], VehicleStatus[vehicle['status']]
        )
        vehicles.append(vehicle)

    return State(0, vehicles, start_point, end_points, graph, weather)

