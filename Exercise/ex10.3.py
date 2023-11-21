"""Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor.
Continue the main program by causing a fire alarm in your building."""
class Building:
    def __init__(self, bottomfloor, topfloor, num_elevators):
        self.bottomfloor = bottomfloor

        self.elevators = []

        for _ in range(num_elevators):
            elevator = Elevator(bottomfloor, topfloor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_num, destination_floor):
        elevator = self.elevators[elevator_num]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottomfloor)
        print("Fire alarm triggered. All elevators are moving to the bottom floor.")

class Elevator:
    def __init__(self, bottomfloor, topfloor):
        self.currentfloor = bottomfloor
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor


    def go_to_floor(self,targetfloor):
        if targetfloor > self.topfloor or targetfloor < self.bottomfloor:
            print("No floor.")
            return
        while self.currentfloor != targetfloor:
            if self.currentfloor < targetfloor:
                self.floor_up()
            elif self.currentfloor > targetfloor:
                self.floor_down()

    def floor_up(self):
        if self.currentfloor < self.topfloor:
            self.currentfloor+=1
            print(f'{self.currentfloor}')
    def floor_down(self):
        if self.currentfloor > self.bottomfloor:
            self.currentfloor -= 1
            print(f'{self.currentfloor}')


bfloor = int(input('Enter the bottom floor: '))
tfloor = int(input('Enter the top floor: '))
num_elevators = int(input('Enter the number of elevators: '))

building = Building(bfloor, tfloor, num_elevators)

elevator_num = int(input('Enter the elevator number (0 to {}): '.format(num_elevators - 1)))
destination_floor = int(input('Enter the destination floor: '))

building.run_elevator(elevator_num, destination_floor)

building.fire_alarm()