def merge_lists_to_dict(list_one, list_two):
   zipped_seq = zip(list_one, list_two)
   return dict(zipped_seq)
res_one = merge_lists_to_dict(list_one=['a', 'b', 'c'], list_two=[10, True, []])
print(res_one)

res_two = merge_lists_to_dict(list_one=['abc'], list_two=[{}, True, 100])
print(res_two)

res_three = merge_lists_to_dict([10, True, 100], list_two=['abc'])
print(res_three)

def update_car_info(**car):
   car['is_available'] = True
   return car 
res = update_car_info(bran='BMW', price=100000)
print(res)