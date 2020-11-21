class StackError(Exception):
    def __init__(self, *args) -> None:
        self.__message: str = args[0] if args else ''

    def __str__(self) -> str:
        return f'StackError occurred: {self.__message}.'
