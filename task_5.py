# Есть файл text.txt. Вывести слово, имеющее минимальную длину. Обработать исключения.

try:
    with open('text.txt', 'r', encoding = 'utf-8') as f:
        s = f.read().split()
        a = len(min(s, key = len))
        b = [q for q in s if len(q) == a]
        print(b)

except FileNotFoundError:
    print('Невозможно открыть файл')


