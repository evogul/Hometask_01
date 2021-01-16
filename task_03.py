'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
'''

n_number = input('Введите число n: ')
print(f'Сумма чисел "n+nn+nnn" равна {int(n_number)+int(n_number+n_number)+int(n_number+n_number+n_number)}')
