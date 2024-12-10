my_scores = [10, 7, 14]

#my_scores = {
#   '0': 10,
#    '1': 7,
#    '2':14
#}

scores = {index: elem * 2 for index, elem in enumerate(my_scores)}

print(scores)

my_motorbike = {
    'brand': 'bmw',
    'country': 'germany',
    'owner': 'vova'
}

bike = {k: v.upper() for k , v in my_motorbike.items()}
print(bike)

my_moto = ['Ducati', 'Italy', 'Vi']

motobike = [el for el in my_moto if len(el) > 3]
print(motobike)