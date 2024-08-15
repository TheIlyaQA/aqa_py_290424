from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def work_with_cookies():
    driver = webdriver.Chrome()

    # Navigate to url
    driver.get("http://www.example.com")

    # Adds the cookie into current browser context
    driver.add_cookie({"name": "foo", "value": "bar"})

    # Get cookie details with named cookie 'foo'
    print("по ключу", driver.get_cookie("name"))  # повертає None
    print("по значеню", driver.get_cookie("foo"))  # повертає весь словник
    cookies = driver.get_cookies()[0]
    print("всі кукі", cookies)
    print("по ключу з усіх", cookies["name"])

# work_with_cookies()


def file_uploader(folder: Path, filename: str = 'some-file.txt'):
    driver = webdriver.Firefox()
    file = str(folder / filename)
    driver.get('http://the-internet.herokuapp.com/upload')
    driver.find_element(By.ID, 'file-upload').send_keys(file)
    driver.find_element(By.ID,'file-submit').click()
    # driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()

    uploaded_file = driver.find_element(By.ID, 'uploaded-files').text
    assert uploaded_file == filename, "uploaded file should be %s" % filename

# folder = Path(__file__).parent
# file_uploader(folder)


def work_with_windows():
    driver = webdriver.Firefox()
    driver.get('http://the-internet.herokuapp.com/upload')
    driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()
    driver.switch_to.new_window()  # нова пуста вкладка
    driver.switch_to.default_content()  # повинно повертати на перший таб, але не працює
    # time.sleep(2)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)  # перебір табів
    # print(driver.window_handles)
    main_window = driver.window_handles[0]
    driver.switch_to.window(main_window)
    # driver.switch_to.frame("frameName")
    # driver.forward()
    # driver.back()

work_with_windows()
