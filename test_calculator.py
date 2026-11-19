from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
	assert add(2,3) == 5

def test_subtract():
	assert subtract(11,8) == 3

def test_multiply():
	assert multiply(4,5) == 20

def test_divide():
	assert divide(6,2) == 3

def test_circleArea():
	assert CircleArea(-4) == "Error"

def test_multiply_zero():
	# Arrange
	a, b = 10, 0
	# Act
	result = multiply(10,0)
	# Assert
	assert result == 0

import pytest

@pytest.mark.parametrize("a, b, expected", [
(2, 3, 5), (-2, -3, -5), (0, 0, 0),
])

def test_add_many(a, b, expected):
	assert add(a, b) == expected

def test_divide_by_zero():
	with pytest.raises(ZeroDivisionError):
		divide(5,0)
