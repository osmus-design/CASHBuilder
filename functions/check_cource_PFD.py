# ФУНКЦИЯ ПРОВЕРКИ СООТВЕТСТВИЯ КУРСУ ТРАТ

# Импортируем вспомогательные библиотеки
from functions import count_days
from functions.other_fnc import ex_input, PFD, PFP, end_key, separator_line
from datetime import date


def cource():
    print("Введи плановую сумму ежедневных трат", end="")
    plan_PFD = ex_input(None)

    print("Введи сколько осталось средств на еду и транспорт на данный момент", end="")
    remains = ex_input(None)

    # Подсчет количества дней базовых и повышенных трат
    start_date = date.today()
    start_date = start_date.strftime("%d.%m.%Y")
    base_expence_days, upper_expence_days = count_days.between(
        start_date, None)

    # Вычисляем плановые траты за период
    plan_PFP = PFP(plan_PFD, base_expence_days, upper_expence_days)

    # сравнение полученных данных, подсчет рекомендаций
    if remains >= plan_PFP:
        plan_PFD = round(PFD(remains, base_expence_days, upper_expence_days))
        print("\nТраты в пределах разумного\
            \nМожно организовать траты в день на уровне:", plan_PFD, "руб")
    else:
        balance = plan_PFP - remains
        plan_PFD -= round(PFD(balance, base_expence_days, upper_expence_days))
        print("\nТраты выше плановых\
            \nНужно организовать траты в день на уровне:", plan_PFD, "руб")

    end_key()
    separator_line()
    return None
