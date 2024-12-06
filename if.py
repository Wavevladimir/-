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

my_num = 21.5
if type(my_num) is int:
    print(my_num, 'is integer')
else:
    print(my_num, 'is not an integer')

my_phone = {
    'price': 200,
}
if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")

print(my_phone.get('brand'))
print(bool(my_phone.get('brand')))

my_numb = -10
if my_numb > 0:
    print(my_numb, 'is positiv number')
elif my_numb < 0:
    print(my_numb, 'is negative number')
else: 
    print(my_numb, 'is zero')

def nums_info(a, b):
    if(type(a) is not int) or (type(b) is not int):
        return"Один из агументов не целое число"
    if a >= b:
        return f"{a} больше или равно {b}"
    return f"{a}меньше{b}"
print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))