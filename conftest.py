import pytest


@pytest.fixture(autouse=True)
def project_fixture():
    print('Test started')
    yield
    print('\nTest finished')


# @pytest.fixture(autouse=False)
# def project_fixture():
#     print('\nPROJECT FIXTURE SETUP')
#     yield
#     print('PROJECT FIXTURE TEARDOWN')
#
#
# @pytest.fixture(autouse=False, scope='function')
# def fixture1():
#     print('FUNCTION FIXTURE SETUP')
#     yield
#     print('FUNCTION FIXTURE TEARDOWN')
#
#
# @pytest.fixture(autouse=False, scope='class')
# def fixture2():
#     print('CLASS FIXTURE SETUP')
#     yield
#     print('CLASS FIXTURE TEARDOWN')
#
#
# @pytest.fixture(autouse=False, scope='package')
# def fixture3():
#     print('PACKAGE FIXTURE SETUP')
#     yield
#     print('PACKAGE FIXTURE TEARDOWN')
#
#
# @pytest.fixture(autouse=False, scope='session')
# def fixture4():
#     print('\nSESSION FIXTURE SETUP')
#     yield
#     print('SESSION FIXTURE TEARDOWN')

