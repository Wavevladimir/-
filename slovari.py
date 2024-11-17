my_mothorbike = {
    'brand': 'Ducati',
    'engine_vol': 1.2,
    'price_info': {
        'price': 20000,
        'is_availble': True
    }
}

other_mothobike = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati'
}

print(my_mothorbike == other_mothobike)

print(my_mothorbike['brand'])

my_mothorbike['price'] = 7000
print(my_mothorbike)

my_mothorbike['is_new'] = True

del my_mothorbike['engine_vol']

key_name = 'brand'

other_mothobike[key_name] = 'BMW'
print(other_mothobike)