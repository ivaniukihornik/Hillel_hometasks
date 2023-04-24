from pytest import fixture


@fixture(autouse=True, scope='class')
def fixture_for_part_1():
    print('\nTests started')
    yield
    print('\nTests finished')
