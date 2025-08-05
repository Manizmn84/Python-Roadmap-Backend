# IMPORTS
from vehicle import Vehicle

class GroundVehicle(Vehicle):
    def __init__(self, number_of_wheels: int, steering_wheel: str, **kwargs):
        self.nubmer_of_wheels = number_of_wheels
        self.steering_whell = steering_wheel
        super().__init__(**kwargs)
