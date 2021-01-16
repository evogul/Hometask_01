income = float(input('Введите выручку: '))
charge = float(input('Введите издержки: '))
if income>charge:
    rent = income-charge
    print(f"Прибыль. Ренатбельность выручки {round(rent/income*100,2)}%")
    count_empl = int(input('Введите количество сотрудников: '))
    rent_empl = rent / count_empl
    print(f'Прибыль в расчете на одного сотрудyика: {round(rent_empl)}')
elif income<charge:
    print("Убыток")
else:
    print("отработали в ноль")





