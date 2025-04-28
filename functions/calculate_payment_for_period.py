def calculate_payment_for_period(value: int, day_base: int, day_upper: int) -> int:
    """
    Рассчитать количество трат за период времени. Payment for period
    """
    payment = value * (day_base + 3 * day_upper)
    return payment