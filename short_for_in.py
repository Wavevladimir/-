all_nums = [-3, 1, 0, 10, -20, 5]
absolutly_nums = []
for num in all_nums:
    absolutly_nums.append(abs(num))
#absolutly_nums = [abs(num) for num in all_nums] либо так сокращенный цикл for in
#absolutly_nums = [num for num in all_nums if num > 0] сокращенный с фильтрацией
print(absolutly_nums)
print(all_nums)

my_set = {1, 10, 15}
new_set = set()
for val in my_set:
    new_set.add(val * val)
#new_set = {val * val for val in my_set} сокращенный цикл
print(new_set)
print(my_set)

my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}
scores = {}

for key, value in my_scores.items():
    scores[key] = value * 10
print(scores)
print(my_scores)