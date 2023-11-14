class Car:
    def __init__(self, regisnum, maxspeed):
        self.regisnum = regisnum
        self.maxspeed = int(maxspeed)
        self.curspeed = 0
        self.traveldist = 0

    def accelerate(self, acceleration : int):
        self.curspeed = min(max(self.curspeed + acceleration, 0), self.maxspeed)

    def drive(self, time):
        self.traveldist += self.curspeed * time

new_car = Car("ERO-977","150")
print(f'Registration number : {new_car.regisnum}')
print(f'Maximum speed: {new_car.maxspeed}')
print(f'Current speed: {new_car.curspeed}')
print(f'Travelled distance: {new_car.traveldist}')

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f'{new_car.curspeed}')
new_car.accelerate(-200)
print(f'{new_car.curspeed}')
new_car.accelerate(60)
print(f'{new_car.curspeed}')
new_car.drive(1.5)
print(f'{new_car.traveldist}')