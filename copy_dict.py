my_cars = ['BMW', 'Audi']
copied_cars = my_cars

copied_cars.append('Mercedes')
print(copied_cars) 
print(my_cars)

print(id(my_cars) == id(copied_cars))