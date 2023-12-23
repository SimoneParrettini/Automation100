from selenium.webdriver import Chrome
from Library import ConfigReader
from selenium.webdriver import Firefox
def startBrowser():
    global driver

    if (ConfigReader.readConfigData('Details','Browser')=="Chrome"):
        driver = Chrome()
    elif (ConfigReader.readConfigData('Details','Browser')=="Firefox"):
        driver = Firefox()
    else:
        driver = Chrome()
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()