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


bfloor = int(input('Enter the bottom floor :'))
tfloor = int(input('Enter the top floor: '))
target = int(input('Floor you want to go to: '))
elevator = Elevator(bfloor,tfloor)
elevator.go_to_floor(target)
elevator.go_to_floor(bfloor)