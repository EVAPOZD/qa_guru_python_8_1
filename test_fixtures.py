import pytest


@pytest.fixture
def browser():
    print("Выполняюсь перед тестом")
    yield
    print("Напишусь после теста")
@pytest.fixture
def main_page(browser):
    pass

@pytest.fixture(scope="session")
def test_user():
    print("Я тоже выполняюсь перед тестом")
    yield
    print("Напишусь после теста тоже")

def test_first(browser, test_user,main_page):
    pass

def test_second(browser, test_user):
    pass