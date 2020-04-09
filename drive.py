import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class driverWithDelay:
    def __init__(self, driver, delay: int):
        self.driver = driver
        self.delay = delay

    def click(self, xpath):
        for x in range(5):
            x=x
            try:
                self.driver.find_element_by_xpath(xpath).click()
                time.sleep(self.delay)
                break
            except selenium.common.exceptions.NoSuchElementException as e:
                e=e
                # print('no element found')
                time.sleep(.5)

    def send(self, xpath: str, keys):
        for x in range(5):
            x=x
            try:
                self.driver.find_element_by_xpath(xpath).send_keys(keys)
                time.sleep(self.delay)
                break
            except selenium.common.exceptions.NoSuchElementException as e:
                e=e
                # print('no element found')
                time.sleep(.5)

    def clickid(self, id: str):
        for x in range(5):
            x=x
            try:
                self.driver.find_element_by_id(id).click()
                time.sleep(self.delay)
                break
            except selenium.common.exceptions.NoSuchElementException as e:
                e=e
                # print('no element found')
                time.sleep(.5)