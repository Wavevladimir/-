import random 
print(random.random())
print(random.randint(1, 10))
print(random.choice('abcd'))
print(random.choice([1, 10, 4]))
print(random.choices([1, 2, 3, 10, 15], k=3))
my_list = [1, 2, 3, 10, 15]
print(random.shuffle(my_list))
print(my_list)

print(''.join(random.choices('abcdf0123456789', k=8)))