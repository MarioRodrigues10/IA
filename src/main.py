class State:
    def __init__(self, time, vehicles, start_point, end_points, graph):
        self.time = time
        self.vehicles = vehicles
        self.start_point = start_point
        self.end_points = end_points
        self.graph = graph