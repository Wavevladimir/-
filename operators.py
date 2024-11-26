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