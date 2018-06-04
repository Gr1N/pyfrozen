import pytest

from pyfrozen import FrozenDict


def test_manipulate_and_freeze():
    fd = FrozenDict()

    fd.update({
        'key_1': 'value_1',
        'key_2': 'value_2',
    })
    assert fd['key_1'] == 'value_1'
    assert fd['key_2'] == 'value_2'
    assert len(fd) == 2

    fd.pop('key_1')
    assert 'key_1' not in fd
    assert len(fd) == 1

    fd['key_3'] = 'value_3'
    assert fd['key_3'] == 'value_3'

    fd.freeze()
    assert fd.frozen

    with pytest.raises(RuntimeError):
        fd.pop('key_2')

    with pytest.raises(RuntimeError):
        fd['key_4'] = 'value_4'

    keys = [k for k in fd]
    assert keys == [
        'key_2',
        'key_3',
    ]


def test_no_args_to_update():
    fd = FrozenDict()

    with pytest.raises(TypeError):
        fd.update()


def test_more_that_one_arg_to_update():
    fd = FrozenDict()

    with pytest.raises(TypeError):
        fd.update({}, {})


def test_update_using_tuple_arg():
    fd = FrozenDict()

    fd.update((
        ('key_1', 'value_1'),
        ('key_2', 'value_2'),
    ))

    assert fd['key_1'] == 'value_1'
    assert fd['key_2'] == 'value_2'
    assert len(fd) == 2


def test_update_using_kwargs():
    fd = FrozenDict()

    fd.update({
        'key_1': 'value_1',
        'key_2': 'value_2',
    }, key_3='value_3')

    assert fd['key_1'] == 'value_1'
    assert fd['key_2'] == 'value_2'
    assert fd['key_3'] == 'value_3'
    assert len(fd) == 3
