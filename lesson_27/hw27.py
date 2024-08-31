from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.get('http://localhost:8000/dz.html')

def verify_frame(frame_id, input_id, secret_text):
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))
    input_field = driver.find_element(By.XPATH, f'//input[@id="{input_id}"]')
    input_field.send_keys(secret_text)
    button = driver.find_element(By.XPATH, f'//button[@onclick="verifyInput(\'{input_id}\')"]')
    button.click()

    alert = Alert(driver)
    if "Верифікація пройшла успішно!" == alert.text:
        print(f"Test passed for {frame_id}")
    else:
        print(f"Test failed for {frame_id}")
    alert.accept()
    driver.switch_to.default_content()

verify_frame("frame1", "input1", "Frame1_Secret")
verify_frame("frame2", "input2", "Frame2_Secret")

driver.quit()