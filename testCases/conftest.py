import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from utilities.readProperty import ReadConfig

@pytest.fixture()
def setup(browser):
    if browser == 'Chrome' or browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox' or browser == 'Firefox':
        options = Options()
        options.binary_location = ReadConfig.getFirefoxPath()
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'safari' or browser == 'Safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):               # this will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):      # this will return the Browser value to setup method
    return request.config.getoption("--browser")


################### Pytest HTML report ###################

# It is hook for Adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Corporate User'
    config._metadata['Module'] = 'Login'
    config._metadata['Tester'] = 'KEEN Tester'


# It is hook for Delete/Modify Environment info to HTML report
@pytest.mark.optonalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('plugins', None)

