import pytest


@pytest.fixture(autouse=False)
def package_fixture():
    print('PACKAGE FIXTURE SETUP')
    yield
    print('PACKAGE FIXTURE TEARDOWN')