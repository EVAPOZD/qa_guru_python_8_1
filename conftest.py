import pytest


@pytest.fixture
def main_page():
    pass

pytest.fixture
def browser():
    print("Выполняюсь перед тестом")
    yield
    print("Напишусь после теста")

@pytest.fixture(scope="session")
def test_user():
    print("Я тоже выполняюсь перед тестом")
    yield
    print("Напишусь после теста тоже")