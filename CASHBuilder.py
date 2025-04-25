# start

from functions import save_up_cash, check_cource_PFD, other_fnc

print("Привет! Давай посчитаем твои денежки ($_$)")

while True:
    print("Выбери что хочешь сделать: \
          \n1. Отложить деньги и посчитать траты\
          \n2. Проверить моё соответствие курсу трат\
          \n\nВведи цифру, нажми Enter", end="")
    toggle = other_fnc.ex_input()
    if toggle == 1:
        other_fnc.separator_line()
        save_up_cash.cash()
    elif toggle == 2:
        other_fnc.separator_line()
        check_cource_PFD.cource()
    else:
        print("Введена неправильная цифра, попробуй ещё раз!\n")    