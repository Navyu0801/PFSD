class Vehicle:
    def init(self,s):
        self.speed = 200
class LandVehicle:
    def init(self):
        self.wheelcount = 10
class Car(LandVehicle):
    pass
ob = Car()
print(ob.dict)