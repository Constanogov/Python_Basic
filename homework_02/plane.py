from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo: int = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
#        self.cargo = cargo

    def load_cargo(self, load_cargo):
        if self.max_cargo >= self.cargo + load_cargo:
            self.cargo = self.cargo + load_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        all_cargo = self.cargo
        self.cargo = 0
        return all_cargo
