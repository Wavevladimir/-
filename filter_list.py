def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)
    return list(filter(check_element_type, list_to_filter))

res = filter_list([1, 10, 'abc', 5.5], int)
print(res)

print(isinstance(True, bool))
print(isinstance(True, int))
print(isinstance(True, object))