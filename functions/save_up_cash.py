# ФУНКЦИЯ НАКОПЛЕНИЯ КАПИТАЛА

# Импортируем необходимые библиотеки
from functions import count_days, other_fnc


# Объявляем переменные
def cash():
    # Коэффициент целевого накопления 0,2 (20%), инвестиции
    target_accum, invest_value = 0.2, 0.2
    # Коэффициент минимального целевого накопления 0,1 (10%)
    target_accumulation_MIN = 0.1

    wastes = {  # вывести за пределы функции
        "проживание": 15000,  # Плата за жильё, половина месячной стоимости
        "подарки близким": 0,  # Расходы на подарки
        "коммунальные услуги": 0,  # Коммунальные услуги
        "кредит/рассрочка": 0,  # Месячный расход на кредиты/рассрочку.
        "подписки": 700,  # Общая сумма расходов на подписки
        "питание/проезд в день": 1200  # Целевая минимальная сумма каждодневных расходов
    }

    # Ручной ввод значения полученной зарплаты
    print("Введи сумму твоего аванса", end="")
    income = other_fnc.ex_input(None)
    # Заполнение словаря с затратами
    wastes = other_fnc.dict_cont_write(wastes)

    # Вызов функции вычисления промежутка между датами, введенными пользователем и запись в переменные
    base_expence_days, upper_expence_days = count_days.between(None, None)

    # Вывод на экран значение всех затрат их сумму
    all_wastes = other_fnc.dict_cont_summ(
        wastes, base_expence_days, upper_expence_days)
    other_fnc.separator()
    print("Все траты за период:", all_wastes, "руб")

    # Считаем общую сумму регулярных расходов за период
    payment_for_period = other_fnc.PFP(
        wastes["питание/проезд в день"], base_expence_days, upper_expence_days)
    # Считаем сумму денег оставшихся после вычета всех расходов из зп, кроме ежедневных за период.
    profit = income - (sum(wastes.values()) - wastes["питание/проезд в день"])
    # Вычитаем сумму каждодневных расходов. Получаем чистую сумму доступных накоплений. Выводим на экран
    capital = profit - payment_for_period

    # Выводим расчеты на экран
    print(f"\
    \nВыполняю расчеты...\
    \nДни базовых трат: {base_expence_days}\
    \nДни повышенных трат: {upper_expence_days}\
    \nС вычетом всех расходов остается: {capital} руб")

    # Выводим коэффициенты накоплений
    print("Хочешь отложить: ", target_accum * 100, end="%\n")
    print("Из них инвестировать: ", invest_value * 100, end="%\n\n")

    # РАСЧЕТ РЕКОМЕНДАЦИЙ
    # Находим значение целевого накопления по начальному тарифу
    target_capital = (profit * target_accum)
    # Находим значение минимального целевого накопления по начальному тарифу
    target_capital_MIN = (profit * target_accumulation_MIN)
    # Находим значение инвестиций
    investment = (capital * invest_value)
    # Рекомендованный расход для получения 20% от получки
    recomm_payment = int(profit * (1 - target_accum) /
                         (base_expence_days + 2 * upper_expence_days))
    # Расчет рекомендуемой траты за период для получения 20% от получки
    recomm_paym_for_per = other_fnc.PFP(
        recomm_payment, base_expence_days, upper_expence_days)
    # Расчет рекомендуемой суммы накоплений
    recom_capital = profit - recomm_paym_for_per
    # Расчет рекомендуемых инвестиций
    recom_investment = recom_capital * invest_value

    # Сравниваем чистую сумму доступных накоплений со значением целевого накопления и минимального целевого накопления
    # ВЫВОД ДАННЫХ
    # Если накопления составят менее минимально возможного для цели
    if 0 < capital <= int(target_capital_MIN):
        print(f"\
    \nТы не можешь копить деньги\
    \n\
    \nРекомендовано организовать ежедневные траты на уровне: {recomm_payment} руб\
    \nТогда траты на питание и проезд за период составят: {recomm_paym_for_per} руб\
    \nТы сможешь накопить: {recom_capital} руб\
    \nИз них инвестировать: {recom_investment} руб")
    # Если накопления составят меньше поставленной для цели, но больше минимального
    elif target_capital_MIN < capital < target_capital:
        capital = target_capital
        # Выводим расчеты
        print(f"\
    \nТы можешь накопить: {capital} руб\
    \nИз них инвестировать: {investment} руб\
    \n\
    \nРекомендовано организовать ежедневные траты на уровне: {recomm_payment} руб\
    \nТогда траты на питание и проезд за период составят: {recomm_paym_for_per} руб\
    \nТы сможешь накопить: {round(recom_capital)} руб\
    \nИз них инвестировать: {round(recom_investment)} руб")
    elif capital < 0:  # Если накопления ушли в минус
        # Расчет затрат в день чтобы выйти в ноль
        # Из целевого расхода за период вычитаем отрицательное накопление (недостаток)
        zero_paym_for_period = (payment_for_period + capital)
        zero_paym_for_day = other_fnc.PFD(
            zero_paym_for_period, base_expence_days, upper_expence_days)
        # Выводим расчеты
        print(f"\
    \nТы не можешь копить деньги\
    \nНе хватает: {abs(capital)} руб\
    \n\
    \nРекомендовано организовать ежедневные траты на уровне: {round(zero_paym_for_day)} руб\
    \nТогда траты на питание и проезд за период составят: {round(zero_paym_for_period)} руб\
    \nТы выйдешь в ноль, потратишь всю сумму: {income} руб")
    else:  # Если накопления больше целевых значений
        # Выводим расчеты
        print(f"\nТы можешь накопить: {round(capital)} руб")
        print(f"Из них инвестировать: {round(investment)} руб")

    other_fnc.end_key()
    other_fnc.separator_line()
    return None
