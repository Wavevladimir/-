my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}
print(my_set.intersection(other_set))
print(other_set.intersection(my_set))

#print(my_set.union(other_set)) обьединение наборов

#print(my_set.issubset(other_set)) подмножество
#print(my_set.discard('d')) удаление элемента d

print(my_set == other_set)
print(my_set.difference(other_set))

copied_set = my_set.copy()
my_set.add('t')
copied_set.add('l')
print(my_set)
print(copied_set)

#print(my_set & copied_set) пересечение наборов 

a = {'v', 'n', 'k', 'w'}
b = {'v', 'n', 'k', 'q'}

#print((a | b) - (a & b)) | юнион обьединение & пересечение 
# либо эта форула для нахождения разницы либо symmetric_diference 