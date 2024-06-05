my_dict = {'Petr': 1949, 'Alex': 1998, 'Ira': 2005}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ira'])
print('Not existing value:', my_dict.get('Vasya'))
my_dict.update({'Serg': 1988,
                'Igor': 1992})
deleted = my_dict.pop('Alex')
print('Deleted value:', deleted)
print('Modified dictionary', my_dict)
print()

my_set = {45, 'test', False, 11, False, 45, 'year', 'test'}
print('Set:', my_set)
my_set.add(99.9)
my_set.add(True)
my_set.remove(45)
print('Modified set:', my_set)