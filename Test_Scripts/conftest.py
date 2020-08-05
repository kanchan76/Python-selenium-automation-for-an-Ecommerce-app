import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setUpClass(cls):
    print("This will get executed only once before the  setUp method for the first test")

    yield
    print("This will get executed only once after the  tearDown method for the last test")

@pytest.fixture()
def setUp(request):
    driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources\ChromeDriver83\chromedriver.exe")
    driver.maximize_window()
    request.instance.driver = driver
    yield
    driver.quit()