from array import array

my_int_array = array('i', [4, 10, 5, 5, 7])
# print(my_int_array)
# print(type(my_int_array))

# my_int_array.append(15)

# print(my_int_array)
# print(my_int_array.count((5)))
# my_int_array.pop()
# print(my_int_array)
# print(len(my_int_array))
# for elem in my_int_array:
#     print(elem)
# print(my_int_array[1])

with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)
imported_array.reverse()
print(imported_array)