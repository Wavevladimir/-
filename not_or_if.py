not 10
not 0 
not 'abc'
not ''
not True
not None

my_list = [1, 2]
other_list = ['a', 'b']
print(my_list or other_list)
print(len(my_list) > 0 or other_list)

my_dict = {}
print(bool(my_list and my_dict))

my_list and print("List is not empty")