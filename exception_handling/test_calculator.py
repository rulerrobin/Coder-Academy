from calculator import add
from calculator import subtract
from calculator import division
import pytest
from calculator import convert_into_list
from calculator import get_user_input_double
from calculator import get_user_input_add


def test_basic():
    assert "hello" == "hello"

def test_add():
    assert add(1, 2) == 3

def test_add():
    assert subtract(10, 2) == 8
    assert subtract (-5, -7) == 2

def test_division():
    assert division(10, 5) == 2 #python does type conversion for division implicitly so 2 == 2.0

def test_division_raise_error():
    with pytest.raises(Exception):
        division(10, 0)

def test_convert():
    assert 5 in convert_into_list(3,4,5)
    assert 15 not in convert_into_list(7, 8, 9)

def test_user_input_double(monkeypatch):
    # pytest has (monkeypatch) to test using input from user
    monkeypatch.setattr("builtins.input", lambda _: "3") # lambda is used in places that will only be used once 
    assert get_user_input_double() == 6
    monkeypatch.setattr("builtins.input", lambda _: "6")
    assert get_user_input_double() == 12

def test_get_user_input_add(monkeypatch):
    inputs = iter(["3", "4",])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_user_input_add() == 7
