from week_5.test_fuel.fuel import convert, gauge
import pytest

def test_conversion_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_error_convert():
    with pytest.raises( ZeroDivisionError):
       convert("4/0")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("-1/2")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(20) == "20%"

