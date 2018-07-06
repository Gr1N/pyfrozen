import pytest

from pyfrozen import FrozenList


def test_manipulate_and_freeze():
    fl = FrozenList()

    fl.extend(["value_1", "value_2"])
    assert "value_1" in fl
    assert "value_2" in fl
    assert len(fl) == 2

    fl.pop()
    assert "value_2" not in fl
    assert len(fl) == 1

    fl[0] = "value_3"
    assert "value_1" not in fl
    assert "value_3" in fl

    fl.freeze()
    assert fl.frozen

    with pytest.raises(RuntimeError):
        fl.pop()

    with pytest.raises(RuntimeError):
        fl.append("value_3")

    with pytest.raises(RuntimeError):
        fl[0] = "value_3"


def test_reverse():
    fl = FrozenList(items=["value_1", "value_2"])

    rt = tuple(reversed(fl))
    assert FrozenList(items=rt) == FrozenList(items=("value_2", "value_1"))


def test_eq_lt():
    assert FrozenList() == FrozenList()
    assert FrozenList() < FrozenList(items=("value_1", "value_2"))
