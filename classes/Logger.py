from classes.Config import Config
from classes.ILogger import ILogger


class Logger(ILogger):
    """
    Класс для работы с консолью
    """

    def log(self, message, end: str | None = None) -> None:
        print(message, end=end)

    def info(self, message, end: str | None = None) -> None:
        print(Config.colors["BLUE"] + str(message) +
              Config.colors["ENDC"], end=end)

    def success(self, message, end: str | None = None) -> None:
        print(Config.colors["GREEN"] + str(message) +
              Config.colors["ENDC"], end=end)

    def warning(self, message, end: str | None = None) -> None:
        print(Config.colors["YELLOW"] + str(message) +
              Config.colors["ENDC"], end=end)

    def error(self, message, end: str | None = None) -> None:
        print(Config.colors["RED"] + str(message) +
              Config.colors["ENDC"], end=end)


logger = Logger()
