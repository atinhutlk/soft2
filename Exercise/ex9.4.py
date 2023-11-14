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


cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

race_finished = False
hour = 1

print("Race Status:")
print(f"{'Reg Num':<8} {'Max Speed':<10} {'Cur Speed':<10} {'Traveled Dist':<15}")
print("-" * 55)

while not race_finished:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.traveldist >= 10000:
            race_finished = True

    for car in cars:
        print(car)

    hour += 1

print("\nRace Finished!")