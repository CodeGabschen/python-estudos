class ParkingSystem(object):
    def __init__(self, big: int, medium: int, small: int):

        self.vagas = {
            1: big,
            2: medium,
            3: small
        }
    def addCar(self, carType: int) -> bool:
        if self.vagas[carType] > 0:
            self.vagas[carType] -= 1
            return True
        return False