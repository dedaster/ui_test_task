import pytest
from selenium import webdriver

link = "http://localhost:5000/signup"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()