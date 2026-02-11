import pytest
from selene.support.conditions.not_ import title
from selenium import webdriver

@pytest.mark.google
def test_google():
    driver = webdriver.Edge()
    url = 'https://www.google.com/'
    driver.get(url)

    assert driver.title == "Google"
    assert driver.current_url == (url)


@pytest.mark.github
def test_github():
    driver = webdriver.Edge()
    url = 'https://github.com/'
    driver.get(url)

    assert "GitHub" in driver.title
    assert driver.current_url == (url)