def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Проверка работы функции с разными параметрами
#print_params(b=25)
#print_params(c = [1,2,3])

values_list = [False, 4.43, 'Третий параметр']
values_dict = {'a': False, 'b': 'текст', 'c': 300}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [43, 'Текст_2']
print_params(*values_list_2, 42)

