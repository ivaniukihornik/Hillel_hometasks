from lesson10.hometask_10 import data_lib


def test_default_string_type():
    assert type(data_lib.random_string_generation()) == str


def test_custom_string_type():
    assert type(data_lib.random_string_generation(data_lib.digit)) == str


def test_random_string_type():
    assert type(data_lib.random_string_generation(data_lib.get_random_number())) == str

