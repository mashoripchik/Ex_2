#Написать программу для вывода уникальных значений из списка словарей

list_1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
a = []
for b in list_1:
    a.extend(list(b.values()))
a = list(set(a))
print(a)







