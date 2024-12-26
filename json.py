import json

json_str = '{"id":235, "brand": "Nike", "qty":84, "status": {"isForSale":true}}'
json_array = '[1, 2, 3]'
sneakers = json.loads(json_str)

print(type(sneakers))

my_list = json.loads(json_array)
json.dump(sneakers, indent=1)
print(my_list)

