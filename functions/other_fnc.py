# Обработка исключения неправильного ввода данных
def ex_input(value):
    while True:
        try:
            if value == None:
                value = int(input(": "))
            else:
                value = int(value)
        except ValueError:
            print("Введены неправильные данные. Введи число без сторонних символов", end="")
            value = ex_input(None)
        else:
            break
    return value

# Рассчитать количество трат за период времени. Payment for period
def PFP(value: int, day_base: int, day_upper: int) -> int:
    PFP = value * (day_base + 2 * day_upper)
    return PFP

# Рассчитать затраты в день из трат за период. Payment for day
def PFD(PFP: int, day_base: int, day_upper: int) -> int:
    PFD = PFP / (day_base + 2 * day_upper)
    return PFD

# Показать ключи, значения словаря затрат, посчитать сумму всех затрат
def dict_cont_summ(dict: dict, day_base: int, day_upper: int) -> int:
    summary = 0
    for key, values in dict.items():
        if key != "питание/проезд в день":
            print(f"\n{key}: {values} руб", end="")
            summary += values
        else:
            print(f"\n{key}: {values} руб/день", end="")
            Pay_FP = PFP(dict[key], day_base, day_upper)
            print("\nтраты на питание/проезд за период:", Pay_FP, "руб", end="")
    summary += Pay_FP
    return summary

# Заполнение значений словаря затрат
def dict_cont_write(dict:dict) -> dict:
    for key, values in dict.items():
        if key == "проживание":
            toggle = input(f"\nДобавить плановое накопление на проживание за следющий период? \
                        \nЗначение по умолчанию = {values} (половина от суммы месячной платы) \
                        \nВведи другое значение или нажми Enter: ") 
            if toggle != '':
                dict[key] = ex_input(toggle)
            else:
                continue
        elif key == "кредит/рассрочка":
            toggle = input(f"\nДобавить плановое накопление на кредит или рассрочку за следющий период? \
                        \nЗначение по умолчанию = {values} (половина от суммы месячной платы) \
                        \nВведи другое значение или нажми Enter: ") 
            if toggle != '':
                dict[key] = ex_input(toggle)
            else:
                continue
        else:    
            toggle = input(f"\nДобавить плановый расход на {key} за следющий период? \
                        \nЗначение по умолчанию = {values} \
                        \nВведи другое значение или нажми Enter: ") 
            if toggle != '':
                dict[key] = ex_input(toggle)
            else:
                continue
    return dict

def end_key():
    input("\nНажми Enter чтобы закончить")
    return None

def separator():
    print("\n------------------------------------------\n")
    return None

def separator_line():
    print("\n___________________________________________\n")
    return None