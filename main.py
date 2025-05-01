from classes.Logger import logger
from classes.UserInterface import UserInterface

if __name__ == '__main__':
    logger.info("Привет! Давай посчитаем твои денежки ($_$)")

    ui = UserInterface(logger)

    while True:
        logger.log("Выбери что хочешь сделать: \
            \n1. Отложить деньги и посчитать траты\
            \n2. Проверить моё соответствие курсу трат\
            \n\nВведи цифру, нажми Enter", end="")

        toggle = ui.ex_input()

        if toggle == 1:
            # other_fnc.separator_line()
            # save_up_cash.cash()
            logger.success("Is one")
        elif toggle == 2:
            # other_fnc.separator_line()
            # check_cource_PFD.cource()
            logger.success("Is two")
        else:
            logger.error("Введена неправильная цифра, попробуй ещё раз!\n")
