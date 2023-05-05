import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# @pytest.fixture()
# def chrome(request):
#     # options = webdriver.ChromeOptions()
#     # # options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     # # options.add_experimental_option('useAutomationExtension', False)
#     # # options.add_argument('--disable-cache')
#     # # options.add_argument('--disable-extensions')
#     # # options.add_argument('--disable-infobars')
#     # # options.add_argument('--disable-browser-side-navigation')
#     # # options.add_argument('--disable-gpu')
#     # # options.add_argument('--no-sandbox')
#     # # options.add_argument('--disable-dev-shm-usage')
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     # driver.set_page_load_timeout(30)
#     if request.cls:
#         request.cls.driver = driver
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(autouse=False)
# def project_fixture():
#     print('Test started')
#     yield
#     print('\nTest finished')


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

