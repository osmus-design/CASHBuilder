from classes.ILogger import ILogger


class UserInterface:
    """
    Класс для работы с пользовательским интерфейсом (только вход)

    Для работы с выводом используйте Logger
    """

    def __init__(self, logger: ILogger):
        pass

    def ex_input(self, value: int | None = None) -> int:
        """
        Обработка исключения неправильного ввода данных
        """

        while True:
            try:
                if value == None:
                    value = int(input(": "))
                else:
                    value = int(value)
            except ValueError:
                print(
                    "Введены неправильные данные. Введи число без сторонних символов", end="")
                value = self.ex_input()
            else:
                break

        return value

    def dict_cont_write(self, dict: dict) -> dict:
        """
        Заполнение значений словаря затрат
        """
        for key, values in dict.items():
            if key == "проживание":
                toggle = input(f"\nДобавить плановое накопление на проживание за следющий период? \
                            \nЗначение по умолчанию = {values} (половина от суммы месячной платы) \
                            \nВведи другое значение или нажми Enter: ")
                if toggle != '':
                    dict[key] = self.ex_input(toggle)
                else:
                    continue
            elif key == "кредит/рассрочка":
                toggle = input(f"\nДобавить плановое накопление на кредит или рассрочку за следющий период? \
                            \nЗначение по умолчанию = {values} (половина от суммы месячной платы) \
                            \nВведи другое значение или нажми Enter: ")
                if toggle != '':
                    dict[key] = self.ex_input(toggle)
                else:
                    continue
            else:
                toggle = input(f"\nДобавить плановый расход на {key} за следющий период? \
                            \nЗначение по умолчанию = {values} \
                            \nВведи другое значение или нажми Enter: ")
                if toggle != '':
                    dict[key] = self.ex_input(toggle)
                else:
                    continue
        return dict
