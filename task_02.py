'''
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк
'''

seconds = int(input("Введите время в секундах: "))

hours = seconds // 3600
hours = hours % 24

minutes = seconds // 60
minutes = minutes % 60

seconds = seconds % 60

print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
