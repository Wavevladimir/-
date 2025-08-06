my_list = [True, 10, 'abc', {}]
for elem in my_list:
    print(elem)
    
my_object = {
    'x': 10,
    'y': 20,
    'z': 30
}

for key in my_object:
    print(key, my_object[key])
    
for el in [1, 'abc', True]:
    print(type(el))
    print(el)
    
my_obj = {
    'q': 10,
    'w': 20
}
for item in my_obj.items():
    key, value = item
    print(key, value)