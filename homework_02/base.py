from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):

    def __init__(self, weight, started, fuel, fuel_consumption):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def get_fuel(fuel):
        if fuel == 0:
            return False
        else:
            return True

    def start(self, started):
        if started == 'started':
#            pass
            print('started test')
        else:
            if not self.get_fuel(self.fuel):
                raise exceptions.LowFuelError
            else:
                started = 'started'
                print(started)

    def move(self, distance, fuel, fuel_consumption):
        if fuel * 100 / fuel_consumption >= distance:
            self.fuel = fuel - distance * fuel_consumption / 100
            print(self.fuel)
        else:
            raise exceptions.NotEnoughFuel


auto = Vehicle(1, '', 2, 5)
#car.fuel = 0
#print(vars(car))
auto.start('started')