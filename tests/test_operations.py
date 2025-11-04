from app.operations import OPERATIONS


def test_basic_operations():
    ops = OPERATIONS
    assert ops["add"](1, 2) == 3
    assert ops["sub"](5, 3) == 2
    assert ops["mul"](2, 4) == 8
    assert abs(ops["div"](9, 3) - 3.0) < 1e-9


def test_divide_by_zero_raises():
    try:
        OPERATIONS["div"](1, 0)
        assert False, "expected ZeroDivisionError"
    except ZeroDivisionError:
        assert True
