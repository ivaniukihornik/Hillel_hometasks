from lesson10.hometask_10 import data_lib


def test_type_get_random_number():
    """Check if value of get_random_number function is in int type"""
    assert type(data_lib.get_random_number()) == int


def test_default_string_type():
    """Check if default value of random_string_generation function is in string type"""
    assert type(data_lib.random_string_generation()) == str


def test_custom_string_type():
    """Check if custom value of random_string_generation function is in string type"""
    assert type(data_lib.random_string_generation(data_lib.digit)) == str


def test_random_string_type():
    """Check if random value of random_string_generation function is in string type"""
    assert type(data_lib.random_string_generation(data_lib.get_random_number())) == str



