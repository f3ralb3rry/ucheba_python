from abc import ABC, abstractmethod
from typing import List, Any

class Стек(ABC):
    """
    Абстрактный класс, описывающий объект Стек.

    Характеристики:
        - элементы (List[Any]): список элементов в стеке
        - максимальный размер (int)
    """

    def __init__(self, максимальный_размер: int):
        """
        Создание и подготовка объекта "Стек".

        :param максимальный_размер: Максимальное количество элементов в стеке

        Примеры:
        >>> class РеальныйСтек(Стек):
        ...     def добавить(self, элемент: Any) -> None:
        ...         pass
        ...     def удалить(self) -> Any:
        ...         pass
        ...     def описать(self) -> str:
        ...         return "Реализация стека"
        >>> стек = РеальныйСтек(10)
        """
        if not isinstance(максимальный_размер, int):
            raise TypeError("Максимальный размер должен быть целым числом.")
        if максимальный_размер <= 0:
            raise ValueError("Максимальный размер должен быть положительным числом.")
        self.максимальный_размер = максимальный_размер
        self.элементы: List[Any] = []

    @abstractmethod
    def добавить(self, элемент: Any) -> None:
        ...

    @abstractmethod
    def удалить(self) -> Any:
        ...

    @abstractmethod
    def описать(self) -> str:
        ...


class Телефон(ABC):
    """
    Абстрактный класс, описывающий объект Телефон.

    Характеристики:
        - модель (str)
        - ёмкость батареи (int)
    """

    def __init__(self, модель: str, ёмкость_батареи: int):
        """
        Создание и подготовка объекта "Телефон".

        :param модель: Модель телефона
        :param ёмкость_батареи: Ёмкость батареи телефона в мАч

        Примеры:
        >>> class Смартфон(Телефон):
        ...     def позвонить(self, номер: str) -> None:
        ...         pass
        ...     def зарядить(self, процент: int) -> None:
        ...         pass
        ...     def описать(self) -> str:
        ...         return "Реализация телефона"
        >>> телефон = Смартфон("iPhone", 4000)
        """
        if not isinstance(модель, str):
            raise TypeError("Модель должна быть строкой.")
        if not isinstance(ёмкость_батареи, int):
            raise TypeError("Ёмкость батареи должна быть целым числом.")
        if ёмкость_батареи <= 0:
            raise ValueError("Ёмкость батареи должна быть положительным числом.")
        self.модель = модель
        self.ёмкость_батареи = ёмкость_батареи

    @abstractmethod
    def позвонить(self, номер: str) -> None:
        ...

    @abstractmethod
    def зарядить(self, процент: int) -> None:
        ...

    @abstractmethod
    def описать(self) -> str:
        ...


class Книга(ABC):
    """
    Абстрактный класс, описывающий объект Книга.

    Характеристики:
        - название (str)
        - автор (str)
        - количество страниц (int)
    """

    def __init__(self, название: str, автор: str, количество_страниц: int):
        """
        Создание и подготовка объекта "Книга".

        :param название: Название книги
        :param автор: Автор книги
        :param количество_страниц: Количество страниц в книге

        Примеры:
        >>> class Роман(Книга):
        ...     def прочитать(self, страницы: int) -> None:
        ...         pass
        ...     def описать(self) -> str:
        ...         return "Реализация книги"
        ...     def добавить_закладку(self, страница: int) -> None:
        ...         pass
        >>> книга = Роман("1984", "Джордж Оруэлл", 328)
        """
        if not isinstance(название, str):
            raise TypeError("Название должно быть строкой.")
        if not isinstance(автор, str):
            raise TypeError("Автор должен быть строкой.")
        if not isinstance(количество_страниц, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if количество_страниц <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.название = название
        self.автор = автор
        self.количество_страниц = количество_страниц

    @abstractmethod
    def прочитать(self, страницы: int) -> None:
        ...

    @abstractmethod
    def описать(self) -> str:
        ...

    @abstractmethod
    def добавить_закладку(self, страница: int) -> None:
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
