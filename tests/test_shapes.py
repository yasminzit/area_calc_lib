import pytest
import math
from calculator import Circle, Triangle, get_area, make_circle, make_triangle
class TestCircle:
    def test_area(self):
        circle = Circle(5)
        expected = math.pi * 25
        assert math.isclose(circle.area(), expected)

    def test_invalid_radius(self):
        with pytest.raises(ValueError):
            Circle(-1)
        with pytest.raises(ValueError):
            Circle(0)

    def test_circle_never_right(self):
        circle = Circle(10)
        assert not circle.is_right()


class TestTriangle:
    def test_area_known_values(self):
        triangle = Triangle(3, 4, 5)
        assert math.isclose(triangle.area(), 6.0)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.is_right()

    def test_non_right_triangle(self):
        triangle = Triangle(2, 3, 4)
        assert not triangle.is_right()

    def test_invalid_sides(self):
        with pytest.raises(ValueError):
            Triangle(1, 1, 3)  # нарушено неравенство треугольника

    def test_non_positive_sides(self):
        with pytest.raises(ValueError):
            Triangle(-1, 2, 3)
        with pytest.raises(ValueError):
            Triangle(0, 2, 3)


class TestCalculator:
    def test_get_area_circle(self):
        circle = Circle(5)
        result = get_area(circle)
        expected = math.pi * 25
        assert math.isclose(result, expected)

    def test_get_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        result = get_area(triangle)
        assert math.isclose(result, 6.0)

    def test_factory_functions(self):
        circle = make_circle(5)
        triangle = make_triangle(3, 4, 5)

        assert isinstance(circle, Circle)
        assert isinstance(triangle, Triangle)

        assert math.isclose(get_area(circle), math.pi * 25)
        assert math.isclose(get_area(triangle), 6.0)
