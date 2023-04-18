import PIL as Image
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def testing_links():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path=r'chromedriver.exe')
    driver.get('http://127.0.0.1:8000/')
    links = driver.find_elements(By.CSS_SELECTOR, 'a')

    print("Testing links...")
    start = time.time()

    working_links = 0
    bad_links = 0
    bad_links_list = []
    for link in links:
        r = requests.head(link.get_attribute('href'))
        if r.status_code != 400:
            working_links += 1
        else:
            bad_links += 1
            bad_links_list.append((link.get_attribute('href'),
                                   r.status_code))
    context = {"working_links": working_links,
               "bad_links_list": bad_links_list, "bad_links": bad_links,
               "links_len": len(links), "time_links": round((time.time() - start), 3)}
    print(context)
    return context


def testing_link():
    print("Testing links...")
    context = {"working_links": 23,
               "bad_links_list": 0, "bad_links": 0,
               "links_len": 32, "time_links": 0.572}
    print(context)
    return context


def testing_imgs():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path=r'chromedriver.exe')
    driver.get('http://127.0.0.1:8000/')
    links = driver.find_elements(By.CSS_SELECTOR, 'img')

    print("Testing Images...")
    start = time.time()

    working_links = 0
    bad_links = 0
    bad_links_list = []
    for link in links:
        r = requests.head(link.get_attribute('src'))
        if r.status_code != 400:
            working_links += 1
        else:
            bad_links += 1
            bad_links_list.append((link.get_attribute('href'),
                                   r.status_code))
    context = {"working_links": working_links,
               "bad_links_list": bad_links_list, "bad_links": bad_links,
               "links_len": len(links), "time_links": round((time.time() - start), 3)}
    print(context)
    return context


# print(str(testing_links()))
print(str(testing_imgs()))
