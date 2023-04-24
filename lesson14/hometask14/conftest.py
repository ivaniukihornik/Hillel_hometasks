from pytest import fixture
import company_lib


@fixture(scope='class')
def company():
    apple_inc = company_lib.Company()
    yield apple_inc


@fixture(scope='class')
def iphone():
    i14_pro_max_256gb = company_lib.Iphone(
        model='Iphone 14 Pro Max',
        price=899,
        units_sold=15000
    )
    yield i14_pro_max_256gb


