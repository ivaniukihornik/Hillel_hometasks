import pytest


@pytest.fixture(autouse=False)
def folder_fixture():
    print('FOLDER FIXTURE SETUP')
    yield
    print('FOLDER FIXTURE TEARDOWN')