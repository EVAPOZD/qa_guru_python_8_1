from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture(scope="session")
def browser_f():
    browser.driver.set_window_size(800,600)

def test_first(browser_f):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_second(browser_f):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('123123232').press_enter()
    browser.element('[id="search"]').should(have.no.text('123123232'))