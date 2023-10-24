from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Рисуем круг"

class Square(Shape):
    def draw(self):
        return "Рисуем квадрат"

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()

class SquareFactory(ShapeFactory):
    def create_shape(self):
        return Square()

import unittest

class TestAbstractFactory(unittest.TestCase):
    def test_create_circle(self):
        circle_factory = CircleFactory()
        circle = circle_factory.create_shape()
        self.assertIsInstance(circle, Circle)
        self.assertEqual(circle.draw(), "Рисуем круг")

    def test_create_square(self):
        square_factory = SquareFactory()
        square = square_factory.create_shape()
        self.assertIsInstance(square, Square)
        self.assertEqual(square.draw(), "Рисуем квадрат")

if __name__ == '__main__':
    unittest.main()