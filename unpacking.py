my_fruits = ['apple', 'banana', 'lime']
my_aplle, my_banana, my_lime = my_fruits
print(my_aplle)
print(my_banana)
print(my_lime)

my_car = ['Audi', 'BMW', 'Renoult']
my_Audi, *remaining_car = my_car
print(my_Audi)
print(remaining_car)
print(type(remaining_car))

user_profile = {
        'name': 'Vova',
        'comments_qty': 23,
}

def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    
    return f"{name} has {comments_qty} comments"

print(user_info(**user_profile))