from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight,  fuel, fuel_consumption, engine):
        super().__init__(weight,  fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self):
        return Engine()

#auto = Car(1, '', 1, 1, 1)
#auto.engine = auto.set_engine()
#car.fuel = 0
#print(vars(car))
#print(vars(auto))
