#def sum(a, b):
#    c = a + b
#    print(c)
#print(type(sum))

#def my_fn(a, b):
#    a = a + 1
#    c = a + b
#    return c 
#res = my_fn(10, 3)
#print(res)

#def my_function():
#    pass
#print(my_function())

#def my_fn(a, b):
#    a = a + 1
#    c = a + b
#    return c 
#num_one = 10
#num_two = 5 

#res = my_fn(num_one, num_two)
#print(res)
#print(num_one)

#def increase_person_age(person):
#    print(id(person))
#    person['age'] += 1
#    return person

#person_one = {
#    'name': 'Vova',
#    'age': 27
#}
#print(id(person_one))
#increase_person_age(person_one)
#print(person_one)

def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] =+ 1
    return person_copy

person_one = {
    'name': 'Vova',
    'age': 27
}

new_person =increase_person_age(person_one)
print(new_person['age'])
print(person_one ['age'])