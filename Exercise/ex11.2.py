class Car:
    def __init__(self, regisnum, maxspeed):
        self.regisnum = regisnum
        self.maxspeed = maxspeed
        self.curspeed = 0
        self.traveldist = 0

    def accelerate(self, acceleration):
        self.curspeed = min(max(self.curspeed + acceleration, 0), self.maxspeed)

    def drive(self, time):
        self.traveldist += self.curspeed * time

    def __str__(self):
        return f"{self.regisnum:<8} {self.maxspeed:<10} km/h {self.curspeed:<10} km/h {self.traveldist:.2f} km"


class ElectricCar(Car):
    def __init__(self, regisnum, maxspeed, battery_capacity):
        super().__init__(regisnum, maxspeed)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"{super().__str__()} {self.battery_capacity:.2f} kWh"


class GasolineCar(Car):
    def __init__(self, regisnum, maxspeed, tank_volume):
        super().__init__(regisnum, maxspeed)
        self.tank_volume = tank_volume

    def __str__(self):
        return f"{super().__str__()} {self.tank_volume:.2f} l"



electric_car = ElectricCar(regisnum="ERO-977", maxspeed=180, battery_capacity=52.5)
gasoline_car = GasolineCar(regisnum="DOC-223", maxspeed=165, tank_volume=32.3)


electric_car.accelerate(20)
gasoline_car.accelerate(15)


for _ in range(3):
    electric_car.drive(1)
    gasoline_car.drive(1)


print("Electric Car Status:")
print(electric_car)

print("\nGasoline Car Status:")
print(gasoline_car)
