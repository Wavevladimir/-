import re
my_string = "My name is Vova"
res = re.search('Vova', my_string)
print(res)
print(type(res))