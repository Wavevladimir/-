greeting = 'Hello from python'
greeting_letters = list(greeting)
print(greeting_letters)

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(my_dict_keys)

ratings = [12.5, 16, 17.8, 19]
print(min(ratings))
print(max(ratings))
print(sum(ratings))

print(sum(ratings)/len(ratings))

my_ratings = [1.5, 14.6, 23]
other_ratings = [2, 5, 11]
all_retings = my_ratings + other_ratings
print(all_retings)

rat = [2.5, 12, 14, 17]
first_two_rat = rat[:2]
print(first_two_rat)

middle_rat = rat[1:-1]
print(middle_rat)

last_two_rat = rat[-2:]
print(last_two_rat)