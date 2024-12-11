class Car: 
    def move(self):
        print("Car is moving")
    def stop(self):
        print("Car stopped")
    
my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))