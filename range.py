my_range = range(7)
print(type(my_range))
print(my_range)
print(list(my_range))

other_range = range(10, 20, 3)
print(list(other_range))

print(other_range[0])
print(other_range[2])
print(other_range[3])

for n in other_range:
    print(n)
