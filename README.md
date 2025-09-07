# Area Calculator

Простая библиотека для вычисления площадей геометрических фигур

## Установка

```bash
pip install .
```

## Использование (в файле using.py)

```bash
from geometry import Circle, Triangle, get_area, make_circle, make_triangle

# Создание фигур напрямую
circle = Circle(5)
triangle = Triangle(3, 4, 5)

print("Площадь круга:", circle.area())
print("Площадь треугольника:", triangle.area())
print("Треугольник прямоугольный?", triangle.is_right())

# Создание фигур через фабричные функции
circle2 = make_circle(10)
triangle2 = make_triangle(6, 8, 10)

print("Площадь круга:", get_area(circle2))  # универсальная функция
print("Площадь треугольника:", get_area(triangle2))
```

## Запуск тестов
```bash
pytest tests/
```

## Добавление новой фигуры

Чтобы расширить библиотеку, нужно:

1) Создать новый класс, унаследованный от Shape, и реализовать метод area()
Например, квадрат:

```bash
class Square(Shape):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def is_right(self) -> bool:
        return True  # квадрат всегда прямоугольный
```

2) Добавить фабричную функцию в calc.py:
```bash
def make_square(side: float) -> Square:
    return Square(side)
```

3) Обновить __init__.py
