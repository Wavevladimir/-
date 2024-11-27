set_one = {10, 'abc', 50, True}
set_two = {10, 'abc', 50, True}

print(set_one == set_two)
print(set_one.__eq__(set_two))

print(set_one is set_two)
print('abc' in set_one)
print('abc' in set_two)
print(10000 in set_one)