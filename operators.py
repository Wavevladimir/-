a = 10 
b = a 

c = a + b 

print(a is b)
print(c is a)

d = [1, 2]
f = [1, 2]
print(d == f)
print(a.__eq__(b))
#print(a.__eq__v)

print(id(d) == id(f))
print(hex(id(d)))

my_num = 10
print(+my_num)

my_bool = False
print(+my_bool)

mu_numb = 10
print(not my_num)

my_car = {
    'brand': 'Toyota',
    'price': 10_000
}

print('brand' in my_car)
print('year' in my_car)
print('year' not in my_car)