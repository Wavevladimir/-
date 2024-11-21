#my_number = 10
#print(id(my_number))
#other_number = 10
#print(id(other_number))
#print(id(10))

#first_num = 20
#second_num = first_num 
#print(id(first_num))
#print(id(second_num))

#second_num += 5
#print(second_num)
#print(first_num)
#print(id(second_num))
#print(id(first_num))

#my_list = [1, 2, 3]
#print(id(my_list))
#other_list = [1, 2, 3]
#print(id(other_list))
#print(id([1, 2, 3]))

#info = {
#    'name': 'Vova',
#    'student': True
#}
#info_copy = info
#info['reviews_qty'] = 5 
#info_copy['reviews_qty'] = 100
#print(info['reviews_qty'])
#print(info_copy['reviews_qty'])

#my_info = {
#    'name': 'Vova',
#    'student': True
#}

#other_info = {
#    'name': 'Vova',
#    'student': True
#}
#other_info['rating'] = 5.0

#info = {
#    'name': 'Vova',
#    'student': True,
#    'reviews': []
#}
#info_copy = info.copy()
#info_copy['reviews'].append('Great course!')
#print(info)
#print(info_copy)

from copy import deepcopy

info = {
    'name': 'Vova',
    'student': True,
    'reviews': []
}
info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('Great course!')
info['reviews'].append('Super')
print(info)
print(info_deepcopy)