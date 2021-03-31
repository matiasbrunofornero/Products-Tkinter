from main import add, write
import pytest


def test_add():
    assert add(2, 2) == 4


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3, 2, 5),
        (2, 3, 5),
        (add(3, 2), 5, 10),
        (3, add(2, 5), 10)
    ]
)
def test_add_param(input_a, input_b, expected):
    assert add(input_a, input_b) == expected


def test_tmp_dir(tmpdir):
    data_in = 'coding example'
    f_path = f'{tmpdir}/test.txt'
    write(f_path, data_in)

    with open(f_path) as file_out:
        data_out = file_out.read()

    assert data_in == data_out

