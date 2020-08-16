from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:\\Users\\ramug\\PycharmProjects\\E_commerce\\Drivers\\chromedriver.exe")
    return driver