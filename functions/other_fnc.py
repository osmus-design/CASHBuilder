# Обработка исключения неправильного ввода данных
def ex_input():
    while True:
        try:
            value = int(input(": "))
        except ValueError:
            print("Вы ввели неправильные данные. Введите число без сторонних символов", end="")
        else:
            break
    return value

# Показать ключи и значения словаря
def dict_cont_view(dict):
    summary = 0
    for key, values in dict.items():
        print(f"\n{key}: {values} руб", end="")
        summary += values
    print("\n" \
    "------------------------" \
    "\nВсего:", summary, "руб")
    
    return ""

# Заполнение значений словаря
def dict_cont_write(dict):
    for key, values in dict.items():
        if key == "проживание" or key == "кредит/рассрочку":
            toggle = input(f"\nДобавить плановый расход на {key} за следющий период? \
                        \nЗначение по умолчанию = {values} (половина от суммы месячной платы) \
                        \nВведите Y или N: ") 
            if toggle.lower() == "y":
                print("Введите сумму Ваших плановых расходов", end="")
                dict[key] = ex_input()
            else:
                continue
        else:    
            toggle = input(f"\nДобавить плановый расход на {key} за следющий период? \
                        \nЗначение по умолчанию = {values} \
                        \nВведите Y или N: ") 
            if toggle.lower() == "y":
                print("Введите сумму Ваших плановых расходов", end="")
                dict[key] = ex_input()
            else:
                continue
    print(dict_cont_view(dict))
    return dict