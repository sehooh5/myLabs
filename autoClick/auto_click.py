from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import threading
import random

driver = webdriver.Chrome('/home/keti0/chromedriver')
url = 'https://uplibra.io'


def random_sec():
    rsec = random.randrange(2, 6)
    return rsec


def auto_click():
    print("Program start....")
    driver.get(url)            # url 오픈해라
    driver.implicitly_wait(3)

    try:
        id = driver.find_element_by_xpath(
            '//*[@id="sliver_sign_user_name"]')
        id.send_keys('sehooh5')
    except NoSuchElementException:
        print("ID Not Found")

    try:
        pwd = driver.find_element_by_xpath(
            '//*[@id="sliver_sign_user_password"]')
        pwd.send_keys('@Ecarut1234')
    except NoSuchElementException:
        print("PWD Not Found")

    try:
        submit = driver.find_element_by_xpath(
            '//*[@id="kt_login_signin_submit"]')
        submit.click()
    except NoSuchElementException:
        print("Submit btn Not Found")

    driver.implicitly_wait(random_sec())
    try:
        lbr = driver.find_element_by_xpath(
            '//*[@id="kt_subheader"]/div/div[1]/a[1]/img')
        lbr.click()
    except NoSuchElementException:
        print("LBR btn Not Found")

    driver.implicitly_wait(random_sec())
    try:
        element = driver.find_element_by_xpath(
            '//*[@id="yj_lottery_btn_open"]')
        element.click()


    except NoSuchElementException:
        print("Btn1 Not Found")


    driver.implicitly_wait(random_sec())
    driver.refresh()
    driver.implicitly_wait(random_sec())
    driver.refresh()
    driver.implicitly_wait(random_sec())
    try:
        element = driver.find_element_by_xpath(
            '//*[@id="yj_lottery_btn_open"]')
        element.click()
    except NoSuchElementException:
        print("Btn2 Not Found")
    threading.Timer(3600, auto_click).start()


auto_click()
