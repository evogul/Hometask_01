
a = int(input('input a: '))
b = int(input('input b: '))

print(f'1-й день: {a}')
day=1
while a<b:
    day = day + 1
    a = round(a * 1.1, 2)
    print(f'{day}-й день: {a}')

print(f'Ответ: на {day}-й день спортсмен достиг результата - не менее {b} км')