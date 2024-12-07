my_list = [True, 10, 'abc', {}]
for elem in my_list:
    print(type(elem))
    print(elem) 

video_info = ('1920x1080', True, 27)
for elements in video_info:
    print(type(elements))
    print(elements)

my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}
for item in my_object.items():
    print(item)
    key, value = item
    print(key, value)

video_ids = {2134, 4567, 2367, 6734}
for id in video_ids:
    print(id)

my_name = 'Vova'
for char in my_name:
    print(char)

for num in range(5):
    print(num)

for odd_num in range(3, 10, 2):
    print(odd_num)