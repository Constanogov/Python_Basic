from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False
    def start(self):
        if self.started == True:
            pass
        elif self.fuel == 0:
            raise exceptions.LowFuelError
        else:
            self.started = True

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        fuel_now = self.fuel
        if fuel_now < required_fuel or fuel_now < self.fuel_consumption:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel = self.fuel - required_fuel