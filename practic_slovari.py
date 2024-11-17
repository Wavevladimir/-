my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

#print(my_disk)
#print(id(my_disk))

print(list(my_disk.keys()))

print(my_disk.get('type'))

new_disk = my_disk.copy()

new_disk['type'] = 'ssd'
print(my_disk)
print(new_disk)

my_list =[['first', 0], ['second', True]]

my_dict = dict(my_list)

print(my_dict)