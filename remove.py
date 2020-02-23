import sys
from selenium import webdriver


username = sys.argv[1]
password = sys.argv[2]
reponame = sys.argv[3]

browser = webdriver.Chrome("./driver/chromedriver.exe")
browser.get('http://github.com/login')


def remove():
    browser.find_elements_by_xpath(
        "//input[@name='login']")[0].send_keys(username)
    browser.find_elements_by_xpath(
        "//input[@name='password']")[0].send_keys(password)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get(f'https://github.com/{username}/' + reponame + '/settings')
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(f"{username}/{reponame}")
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    browser.get("https://github.com/" + username)


if __name__ == "__main__":
    remove()
