#1 Написать программу для получения списка словарей из списков.

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# 1 способ
b = []
for i, j in zip(color_name, color_code):
    b.append({'color_name': i, 'color_code': j})
print(b)

# 2 способ
a =[{'color_name' : color_name[x], 'color_code' : color_code[x]} for x in range(len(color_name))]
print(a)



