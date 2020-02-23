import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("./driver/chromedriver.exe")


username = str(sys.argv[1])  # Insert your github username here
password = str(sys.argv[2])  # Insert your github password here
path = str(sys.argv[3])


def create():
    folderName = str(sys.argv[4])
    os.makedirs(path + '\\' + str(folderName))
    driver.get("https://github.com/new")
    time.sleep(1)

    driver.find_element_by_name("login").send_keys(username)

    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("commit").click()
    time.sleep(1)
    driver.find_element_by_id("repository_name").send_keys(f"{folderName}")
    driver.find_element_by_id(
        "repository_description").send_keys("It's Description")
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="new_repository"]/div[3]/button').click()
    time.sleep(1)
    print("Succesfully created repository {}".format(folderName))
    driver.quit()


if __name__ == "__main__":
    create()
