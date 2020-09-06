import calculator

def test_add_exercise_1():
    assert calculator.add(1,2) == 3

def test_add_exercise_2():
    assert calculator.add(0.1,0.2) == 0.3

def test_add_exercise_3():
    assert calculator.add("Hello ","World") == "Hello World"
