class Car():

 # How to create a class
    model = "Mercedes"
    color = "Grey"
    enginePower = 110
    cylinder = 4

# Constructor
    def __init__(self, model, color, enginePower, cylinder):
            print("init function")
            self.cylinder = cylinder
            self.model = model
            self.enginePower = enginePower
            self.color = color
car1 = Car("Hyundai", "Grey", 110, 4)

print(car1.model)

car2 = Car("Mercedes", "Red", 112, 6)

print(car2.model)