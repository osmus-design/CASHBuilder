class FinanceCalculator:
    """
    Класс для работы с финансовыми вычислениями
    """

    def __init__(self):
        pass

    def get_payment_for_period(self, value: int, day_base: int, day_upper: int) -> int:
        """
        Рассчитать количество трат за период времени. Payment for period
        """
        return value * (day_base + 2 * day_upper)

    def get_payment_for_day(self, PFP: int, day_base: int, day_upper: int) -> int:
        """
        Рассчитать затраты в день из трат за период. Payment for day
        """
        return PFP / (day_base + 2 * day_upper)

    def get_keys_sum(self, dict: dict, day_base: int, day_upper: int) -> int:
        """
        Показать ключи, значения словаря затрат, посчитать сумму всех затрат

        TODO: создать функцию для вывода в консоль
        """
        summary = 0

        for key, values in dict.items():
            if key != "питание/проезд в день":
                summary += values
            else:
                pay_fp = self.get_payment_for_period(
                    dict[key], day_base, day_upper)

        summary += pay_fp

        return summary


# Объект для работы с фин вычислениями
finance_calculator = FinanceCalculator()
