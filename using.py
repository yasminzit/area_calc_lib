from calculator import Circle, Triangle, get_area, make_circle, make_triangle

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