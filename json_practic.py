import json

my_dict = {
    'a': 10,
    'b': {
        'c': [1, 2, 3]
    },
    'd': (1, 2, 3)
}
converted_dict = json.dumps(my_dict)
print(converted_dict)