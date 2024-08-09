my_dict = {'Роман': 1997, 'Глеб' : 1996, 'Раиса': 1960}
print(my_dict)
print(my_dict['Роман'])
my_dict.update({'Валя': 1976,
                'Тот': 1954})
delete = my_dict.pop('Тот')
print(delete)
print(my_dict)

my_set = {1, 2, 3, 'Тот', 'Тот', 5.5}
print(my_set)
my_set.update([6.3, 24])
print(my_set)
my_set.discard(5.5)
print(my_set)