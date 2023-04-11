from abc import ABC


class Vehicle(ABC):

    def __init__(self, weight, started, fuel, fuel_consumption, ):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def get_fuel(self, fuel):
        if fuel== 0:
            return False
        else:
            return True

    def start(self, started):
        if started == 'started':
            print(started)
        else:
            if self.get_fuel(self.fuel) == False:
                print('exceptions.LowFuelError') # TO DO переделать в исключение
            else:
                self.started = 'started'
                print(started)


auto_1 = Vehicle(25, 'nostarted', 1, 10)
auto_1.start(auto_1.started)
print(vars(auto_1))
#print(vars(auto_1))
#print(auto_1.started)




