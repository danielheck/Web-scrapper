from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = './geckodriver'
options.set_preference("webdriver.gecko.driver","./geckodriver")

driver = webdriver.Firefox(options=op)

driver.get("gttps://realpython.github.io/fake-jobs/")

element = driver.find_element_by_id('element-id')
print(element.text)

driver.quit()