my_list = []
my_dict = {'a': 500, 'b': 5874, 'c': 560,'d': 400, 'e': 5874, 'f': 20}
for k, v in my_dict.items():
    if v >= 560:
        my_list.extend(k)
print(my_list)
my_dict.pop('b')
my_dict.pop('c')
my_dict.pop('e')
print(my_dict)
	





