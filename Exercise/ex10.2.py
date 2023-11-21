"""Extend the previous program by creating a Building class.
The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
 When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building.
 Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
 In the main program, write the statements for creating a new building and running the elevators of the building."""


class Building:
    def __init__(self, bottomfloor, topfloor, num_elevators):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.elevators = []
        for _ in range(num_elevators):
            elevator = Elevator(bottomfloor, topfloor)
            self.elevators.append(elevator)

    def run_elevator(self, num_elevators, destinationfloor):
        if 0 <= elevator_num < len(self.elevators):
            elevator = self.elevators[elevator_num]
            elevator.go_to_floor(destination_floor)
        else:
            print("None found")

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