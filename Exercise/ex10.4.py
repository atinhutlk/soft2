import random

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

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name}\n{'Reg Num':<8} {'Max Speed':<10} {'Cur Speed':<10} {'Traveled Dist':<15}")
        print("-" * 55)
        for car in self.cars:
            print(car)
        print()

    def race_finished(self):
        return any(car.traveldist >= self.distance for car in self.cars)


cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
grand_derby_race = Race("Grand Demolition Derby", 8000, cars)

print("Initial Race Status:")
grand_derby_race.print_status()

hours_passed = 0
while not grand_derby_race.race_finished():
    grand_derby_race.hour_passes()
    hours_passed += 1

    if hours_passed % 10 == 0:
        print(f"Race Status after {hours_passed} hours:")
        grand_derby_race.print_status()

print("Race Finished!")
