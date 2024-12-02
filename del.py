my_dict = {'a': True, 'b': 10}
del my_dict['a']
my_dict.__delitem__('b')
print(my_dict)

my_list = [1, 2]
del my_list[0]
my_list.__delitem__(0)
print(my_list)