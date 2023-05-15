from homework_02 import engine
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, *args, **kwargs):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = Engine(volume=3.5, pistons=8)

    def set_engine(self, engine):
        self.engine = engine
