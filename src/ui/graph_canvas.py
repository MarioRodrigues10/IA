import tkinter as tk

class GraphCanvas(tk.Canvas):
    """
    A custom tkinter Canvas that supports zooming and dragging.

    Attributes:
        scale_factor (float): The current zoom level of the canvas.
        drag_data (dict): A dictionary to store the starting coordinates for dragging.

    Methods:
        zoom(event):
            Zooms the canvas in or out using the mouse wheel.
        
        zoom_linux(event):
            Handles zooming for Linux using the mouse button 4 and 5 events.
        
        start_drag(event):
            Initiates dragging by storing the initial mouse position.
        
        drag(event):
            Drags the canvas by calculating the distance moved since the last event.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.scale_factor = 1.0  # Initial scale factor
        self.bind_all("<MouseWheel>", self.zoom)  # Bind mouse wheel event (cross-platform)
        self.bind_all("<Button-4>", self.zoom_linux)  # For Linux scrolling
        self.bind_all("<Button-5>", self.zoom_linux)

        # Variables for dragging
        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.drag)
        self.drag_data = {"x": 0, "y": 0}

    def zoom(self, event):
        if event.delta:  # For Windows and macOS
            scale = 1.1 if event.delta > 0 else 0.9
            self.scale_factor *= scale
            self.scale("all", event.x, event.y, scale, scale)
            self.configure(scrollregion=self.bbox("all"))  # Adjust scroll region

    def zoom_linux(self, event):
        scale = 1.1 if event.num == 4 else 0.9  # For Linux
        self.scale_factor *= scale
        self.scale("all", event.x, event.y, scale, scale)
        self.configure(scrollregion=self.bbox("all"))  # Adjust scroll region

    def start_drag(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def drag(self, event):
        # Calculate the distance moved
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        # Move all items on the canvas
        self.move("all", dx, dy)
        # Update drag data
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
