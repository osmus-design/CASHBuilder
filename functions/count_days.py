# Вычисление количества дней недели в периоде начальной и конечной даты обозначенной пользователем.
from datetime import datetime, timedelta

def write_date():
    # Ввод даты
    start_date_input = input("\nВведите начальную дату в формате дд.мм.гггг: ") 
    end_date_input = input("Введите конечную дату в формате дд.мм.гггг: ")
    # Преобразуем значения, проработаем исключения
    try:
        start_date = datetime.strptime(start_date_input,"%d.%m.%Y").date()
        end_date = datetime.strptime(end_date_input, "%d.%m.%Y").date()
    # Если значения не получены (None)
    except ValueError:
        print("Даты введены неверно. Будет использован период по умолчанию")   
        # Присваиваем значение старт = сегодня, конец = сегодня + 15 дней
        now = datetime.now()
        start_date = now.date()
        end_date = now.date() + timedelta(days=15)
        # Вытащить данные. перетасовать. (Y.m.d) -> (d.m.Y)
        print(f"Будет выполнен расчет на период: {start_date} - {end_date}")
    # Выводим значения функции
    return start_date, end_date

def between():
    # Вызываем функцию ввода даты
    start_date, end_date = write_date()
    # Прорабатываем исключения
    while True:
        # Если начальная дата больше конечной
        if start_date > end_date:
            print("Начальная дата больше конечной")
            # Вызываем функцию записи новых дат
            start_date, end_date = write_date()
        # Вычисляем количество дней в диапазоне дат
        delta = end_date - start_date
        delta = delta.days
        # Если диапазон меньше 14 дней
        if delta < 14:
            print("Введенный диапазон меньше 14 дней, расчет будет неверным")
            start_date, end_date = write_date()
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