from abc import ABC


class Vehicle(ABC):

    def __init__(self, weight, started, fuel, fuel_consumption, ):
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
            print(started)
        else:
            if self.get_fuel(self.fuel) == False:
                print('exceptions.LowFuelError')  # TO DO переделать в исключение
            else:
                self.started = 'started'
                print(started)

    def move(self, distance, fuel, fuel_consumption):
        if fuel * 100 / fuel_consumption >= distance:
            self.fuel = fuel - distance * fuel_consumption / 100
            print(self.fuel)
        else:
            print('exceptions.NotEnoughFuel')  # TO DO переделать в исключение


auto_1 = Vehicle(25, 'nostarted', 20, 10)
auto_1.start(auto_1.started)
auto_1.move(100, auto_1.fuel, auto_1.fuel_consumption)
# print(vars(auto_1))
# print(vars(auto_1))
# print(auto_1.started)
