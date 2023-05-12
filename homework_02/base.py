from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    started: bool = False
    distance: int = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == True:
            pass
        elif self.fuel == 0:
            raise exceptions.LowFuelError
        else:
            self.started = True

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        fuel_need = self.distance * self.fuel_consumption
        if self.fuel == 0 or \
                self.fuel_consumption > self.fuel or \
                self.distance > max_distance or \
                fuel_need > self.fuel:
            raise exceptions.NotEnoughFuel
        elif fuel_need == self.fuel:
            self.fuel = self.fuel - self.distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel



#auto = Vehicle(1, 0, 5)
# auto.fuel = 10
# print(vars(auto))
#auto.started = True
#auto.start(auto.started)
#print(auto.started)
# auto.started = '1'
# print(auto.started)
#print(Vehicle.started)
#print(Vehicle.start)