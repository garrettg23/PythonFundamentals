# Object Oriented Programming
# Object: An instance of a class, representing real life objects or hypothetical objects
# Assigng attributes (what an object is or has) and Methods (what an object can do)

class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        selfyear = year
        self.color = color
    def drive(self):
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")

car_1 = Car("Chevy","Equinox","2019", "Black")
car_2 = Car("Ford","Fusion","2014","Black")

print(car_1.make)
print(car_1.model)
print(car_2.make)
print(car_2.model)
car_1.drive()
car_2.stop()
