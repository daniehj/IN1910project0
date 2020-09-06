import calculator
import math
import pytest

@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]]
)
def test_add_exercise_1(arg,expected_output):
    assert calculator.add(arg[0],arg[1]) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output", [[(-.1, -.1), -.2], [(.1, .1), .2], [(.1, .0), .1]]
)
def test_add_exercise_2(arg,expected_output):
    assert calculator.add(arg[0],arg[1]) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output", [[("Hello ", "World"), "Hello World"], [("Python ", "3.0"), "Python 3.0"], [("IN", "1910"), "IN1910"]]
)
def test_add_exercise_3(arg,expected_output):
    assert calculator.add(arg[0],arg[1]) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output", [[1, 1], [5, 1*2*3*4*5], [2, 1*2]]
)
def test_factorial_exercise_4(arg,expected_output):
    assert calculator.factorial(arg) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output", [[(math.pi/2,10, 10), 1],[(-math.pi/2,10, 10), -1],[(0, 10), 0]]
)
def test_sin_exercise_4(arg,expected_output):
    assert (calculator.sin(arg[0],arg[1]) - expected_output) < 1e-12

@pytest.mark.parametrize(
    "arg, expected_output", [[(1, 2), .5], [(1, 1), 1], [(3, 1), 3]]
)
def test_divide_exercise_4(arg,expected_output):
    assert calculator.divide(arg [0],arg[1]) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), 1], [(1, 1), 1], [(1, 1), 0]]
)
def test_multiplicate_exercise_4(arg,expected_output):
    assert calculator.multiplicate(arg[0],arg[1]) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output", [[2, 14.7781121978613], [3, 60.256610769563004], [5, 742.065795512883]]
)
def test_derivative_of_exponential_exercise_4(arg,expected_output):
    assert calculator.derivative_of_exponential(arg) == expected_output

def test_int_float_addition_with_string_raises_ValueError_exercise_5():
    with pytest.raises(TypeError):
        calculator.add("Hello",1)

def test_zero_division_raises_ZeroDivisionError_exercise_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1,0)
