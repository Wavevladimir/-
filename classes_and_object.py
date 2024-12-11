class Car: 
    def move(self):
        print("Car is moving")
    def stop(self):
        print("Car stopped")
    
my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))

my_second_car = Car()
Car.move(my_car)

print(my_car == my_second_car)
my_car.move()
my_car.stop()

class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
    def upvote(self):
        self.votes_qty += 1 
first_comment = Comment("First comment")
print(first_comment.text)
print(first_comment.upvote)
print(first_comment.__dict__)
print(dir(first_comment))
print(type(first_comment))