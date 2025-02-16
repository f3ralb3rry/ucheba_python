from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int):
        """
        Конструктор базового класса Animal.
        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name
        self.age = age

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"{self._name}, возраст {self.age} лет"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление животного."""
        return f"Animal(name={self._name}, age={self.age})"

    @abstractmethod
    def make_sound(self) -> str:
        """
        Абстрактный метод, который должен быть реализован в дочерних классах.
        :return: Звук, который издает животное.
        """
        pass

    def sleep(self) -> str:
        """
        Метод, который демонстрирует, что животное спит.
        :return: Сообщение о том, что животное спит.
        """
        return f"{self._name} спит."


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog. Расширяет базовый класс Animal.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        """Возвращает строковое представление собаки."""
        return f"Собака {self._name}, порода {self.breed}, возраст {self.age} лет"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление собаки."""
        return f"Dog(name={self._name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> str:
        """Реализация метода для издания звука собакой."""
        return f"{self._name} говорит: Гав!"

    def fetch(self, item: str) -> str:
        """
        Метод, который демонстрирует, что собака приносит предмет.
        :param item: Название предмета.
        :return: Сообщение о том, что собака принесла предмет.
        """
        return f"{self._name} принес(ла) {item}!"


class Cat(Animal):
    """
    Дочерний класс, представляющий кошку.
    """

    def __init__(self, name: str, age: int, color: str):
        """
        Конструктор класса Cat. Расширяет базовый класс Animal.
        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Окрас кошки.
        """
        super().__init__(name, age)
        self.color = color

    def __str__(self) -> str:
        """Возвращает строковое представление кошки."""
        return f"Кошка {self._name}, окрас {self.color}, возраст {self.age} лет"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление кошки."""
        return f"Cat(name={self._name}, age={self.age}, color={self.color})"

    def make_sound(self) -> str:
        """Реализация метода для издания звука кошкой."""
        return f"{self._name} говорит: Мяу!"

    def purr(self) -> str:
        """
        Метод, который демонстрирует, что кошка мурлычет.
        :return: Сообщение о том, что кошка мурлычет.
        """
        return f"{self._name} мурлычет"


if __name__ == "__main__":
    dog = Dog("Зефир", 3, "Самоед")
    cat = Cat("Компот", 2, "рыжий")

    print(dog)
    print(cat)

    print(dog.make_sound())
    print(cat.make_sound())

    print(dog.fetch("мячик"))
    print(cat.purr())

    print(dog.sleep())
    print(cat.sleep())
