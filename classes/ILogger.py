class ILogger:
    """
    Абстрактный класс (интерфейс) для логгера
    """

    def log(self, message: str, end: str | None = None) -> None:
        pass

    def info(self, message: str, end: str | None = None) -> None:
        pass

    def success(self, message: str, end: str | None = None) -> None:
        pass

    def warning(self, message: str, end: str | None = None) -> None:
        pass

    def error(self, message: str, end: str | None = None) -> None:
        pass
