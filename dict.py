my_nums = [10, 50, 0, 5, 5, 100]

res = my_nums.count(5)

print(res)

my_nums.append(25)


my_nums.insert(2, -5)

my_nums.extend('abc')
print(my_nums)

other_nums = my_nums.copy()
print(id(my_nums))
print(id(other_nums))

my_nums.append(3)
other_nums.clear()
print(my_nums, other_nums)

print(len(my_nums))