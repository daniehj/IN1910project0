import calculator
import math
import pytest

def test_add_exercise_1():
    assert calculator.add(1,2) == 3

def test_add_exercise_2():
    assert calculator.add(0.1,0.2) == 0.3

def test_add_exercise_3():
    assert calculator.add("Hello ","World") == "Hello World"

def test_factorial_exercise_4():
    assert calculator.factorial(5) == 1*2*3*4*5


def test_sin_exercise_4():
    x = 1
    assert (calculator.sin(math.pi/2,10) - x) < 1e-12

def test_divide_exercise_4():
    assert calculator.divide(1,2) == .5

def test_multiplicate_exercise_4():
    assert calculator.multiplicate(1,2) == 2

def test_derivative_of_exponential_exercise_4():
    assert calculator.derivative_of_exponential(2) == 14.7781121978613

def test_int_float_addition_with_string_raises_ValueError_exercise_5():
    with pytest.raises(TypeError):
        calculator.add("Hello",1)

def test_zero_division_raises_ZeroDivisionError_exercise_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1,0)
