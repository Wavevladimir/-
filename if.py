my_number = 25
if my_number > 0:
    print(my_number, "is positive nummber")

person_info = {
    'age': 20
}
if not person_info.get('name'):
    print("Имя отстутствует")

if 10 > 2:
    print(True)

num_one = 10
num_two = 5

if (num_one > 0 and num_two > 0 and 
    isinstance(num_one, int) and 
    isinstance(num_two, int)):
    print("both numbers are ints and positive")