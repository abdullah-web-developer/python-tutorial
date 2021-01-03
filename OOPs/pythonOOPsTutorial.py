################### Getting Started With OOP's In Python #####################

# Making Class
class Vehicle:
    # Class Constructor
    def __init__(self, model, year, maxSpeed, howManyGears):
        self.model = model
        self.year = year
        self.maxSpeed = maxSpeed
        self.howManyGears = howManyGears

    # Class Method
    def tellInfoOfVehicle(self):
        print(self.model, "Vehicle is of Year", self.year,
              "with Maximum Speed of", self.maxSpeed)

    # Encapsulation Started With Getters and Setters
    def setHowManyGears(self, howManyGears):
        self.howManyGears = howManyGears

    def getHowManyGears(self):
        print(self.model, "has", self.howManyGears, "gears")
    # Encapsulation Ended

# Inheritance (Child Class MotorBike Extending Vehicle Class)


class MotorBike(Vehicle):
    def maxAcceleration(self):
        print("Maximum Acceleration of", self.model, "is", self.maxSpeed)


# Making Object And Other
Honda1 = Vehicle("Honda Civic", "2020", "240", "5")
Honda1.tellInfoOfVehicle()
Honda1.setHowManyGears("5")
Honda1.getHowManyGears()
Kawasaki1 = MotorBike("Kawasaki Ninja", "2021", "300", "4")
Kawasaki1.tellInfoOfVehicle()
Kawasaki1.setHowManyGears("4")
Kawasaki1.getHowManyGears()
Kawasaki1.maxAcceleration()

#################### Python OOP's Tutorial Ended ###################
