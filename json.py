import json
json_str = '{"id":235, "brand": "Nike", "qty":84, "status": {"isForSale":true}}'
sneakers = json.loads(json_str)

print(type(sneakers))

print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])
print(len(json_str))