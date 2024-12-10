nums = (3, 5, 10)
squares = (num * num for num in nums)
print(squares)

sqrs = (num * num for num in range(6))
print(sqrs)
print(type(sqrs))
for num in sqrs:
    print(num)

nums = [3, 5, 10]
gen = (num * num for num in nums)
squar = list(gen)
print(squar)
print(type(squar))

from sys import getsizeof
sqrs_gen = (num * num for num in range (10000))
print(getsizeof(sqrs_gen))
print(type(sqrs_gen))

for elem in sqrs_gen:
    print(elem)
    if elem == 100: 
        break

sqrs_list = [num * num for num in range(10000)]
print(getsizeof(sqrs_list))
print(type(sqrs_list))