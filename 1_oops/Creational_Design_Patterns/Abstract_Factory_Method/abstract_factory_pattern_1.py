from abc import ABC, abstractmethod


class VehicleFactory:
    @abstractmethod
    def create_vehicle(self, vehicle_type):
        pass


class ElectricVehicleFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return ElectricCar()
        elif vehicle_type == "bike":
            return ElectricBike()
        else:
            raise ValueError(f"Invalid vehicle type {vehicle_type}")


class GasolineVehicleFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return GasolineCar()
        elif vehicle_type == "bike":
            return GasolineBike()
        else:
            raise ValueError(f"Invalid vehicle type {vehicle_type}")


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def __str__(self):
        return self.vehicle_type


class ElectricCar(Vehicle):
    def __init__(self):
        super().__init__("electric car")


class GasolineCar(Vehicle):
    def __init__(self):
        super().__init__("gasoline car")


class ElectricBike(Vehicle):
    def __init__(self):
        super().__init__("electric bike")


class GasolineBike(Vehicle):
    def __init__(self):
        super().__init__("gasoline bike")


class Main:

    @staticmethod
    def get_vehicle(type_of_vehicle, vehicle_type):
        localizers = {
            "Electric": ElectricVehicleFactory,
            "Gasoline": GasolineVehicleFactory,
        }

        return localizers[type_of_vehicle]().create_vehicle(vehicle_type)


print(Main().get_vehicle('Electric', "car"))
print(Main().get_vehicle('Gasoline', "bike"))
