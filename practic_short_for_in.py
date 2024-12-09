my_scores = [10, 7, 14]

#my_scores = {
#   '0': 10,
#    '1': 7,
#    '2':14
#}

scores = {index: elem * 2 for index, elem in enumerate(my_scores)}

print(scores)