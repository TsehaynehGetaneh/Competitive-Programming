class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.slots[0] >=1:
                self.slots[0] -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.slots[1] >=1:
                self.slots[1] -= 1
                return True
            else:
                return False
        if carType == 3:
            if self.slots[2] >=1:
                self.slots[2] -= 1
                return True
            else:
                return False
            

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)