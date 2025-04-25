# Вычисление количества дней недели в периоде начальной и конечной даты обозначенной пользователем.
from datetime import datetime, timedelta, date

# Форматирование даты для функции between
def write_date(start_date: str, end_date: str) -> date:
    # Ввод даты
    if start_date == None:
        start_date = input("\nВведи начальную дату в формате дд.мм.гггг: ")
    
    if end_date == None: 
        end_date = input("Введи конечную дату в формате дд.мм.гггг: ")
    # Преобразуем значения, проработаем исключения
    try:
        start_date = datetime.strptime(start_date,"%d.%m.%Y").date()
    # Если значения не получены (None)
    except ValueError:
        print("Неправильный формат даты. За начальную дату будет принята сегодняшняя дата")   
        start_date = date.today()
        output_start = start_date.strftime("%d.%m.%Y")
    else:
        output_start = start_date.strftime("%d.%m.%Y")
    try:
        end_date = datetime.strptime(end_date, "%d.%m.%Y").date()
    except ValueError:
        print("Неправильный формат даты. Конечная дата назначена через 15 дней от сегодня") 
        end_date = date.today() + timedelta(days=15)
        output_end = end_date.strftime("%d.%m.%Y")
    else:
        output_end = end_date
    print(f"Будет выполнен расчет на период: {output_start} - {output_end}")
    # Выводим значения функции
    return start_date, end_date

# Подсчет количества дней бызовых и повышенных трат
def between(start_date: str, end_date: str) -> int:
    # Вызываем функцию форматирования даты
    start_date, end_date = write_date(start_date, end_date)
    # Прорабатываем исключения
    while True:
        # Если начальная дата больше конечной
        if start_date > end_date:
            print("Начальная дата больше конечной")
            # Вызываем функцию записи новых дат
            start_date, end_date = write_date(None, None)
        # Вычисляем количество дней в диапазоне дат
        delta = end_date - start_date
        delta = delta.days
        # Если диапазон меньше 14 дней
        if delta < 14:
            toggle = input("Введенный диапазон меньше 14 дней. \
                           \nY - продолжить, N - ввести даты заново: ")
            if toggle.lower() == "n":
                start_date, end_date = write_date(None, None)
            else:
                break
        else:
            break
    # Инициализируем счетчики
    base_expence_days = 0
    upper_expence_days = 0
    # Перебираем дни в диапазоне
    current_date = start_date
    while current_date <= end_date :
        weekday = current_date.weekday()
        if weekday in [4,5]: # Пятница, суббота
            upper_expence_days += 1
        else:
            base_expence_days += 1
        current_date += timedelta(days=1) # Переходим к следующему дню
    return base_expence_days, upper_expence_days
