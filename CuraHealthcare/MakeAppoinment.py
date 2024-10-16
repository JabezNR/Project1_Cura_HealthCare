import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    ser_obj=Service("C:\Windows\chromedriver.exe")
    driver=webdriver.Chrome(service=ser_obj)
    return driver
def edge_setup():
    from selenium.webdriver.edge.service import Service
    ser_obj=Service("C:\Windows\msedgedriver.exe")
    driver=webdriver.Edge(service=ser_obj)
    return driver
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ser_obj=Service("C:\Windows\geckodriver.exe")
    driver=webdriver.Firefox(service=ser_obj)
    return driver

driver=edge_setup()
driver.maximize_window()
driver.get("https://katalon-demo-cura.herokuapp.com/")
print(driver.title)
driver.find_element(By.ID,"btn-make-appointment").click()
time.sleep(2)

# enter login details // finding the web elements using ID , CSS_SELECTOR and XPATH
driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.CSS_SELECTOR,"#txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.XPATH,"//button[@id='btn-login']").click()
driver.implicitly_wait(10)
time.sleep(2)

# Select any one option from the DropDown
dropdown=Select(driver.find_element(By.XPATH,"//select[@id='combo_facility']"))
dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
driver.implicitly_wait(10)
time.sleep(2)

# Click on check box and Radio button
driver.find_element(By.XPATH,"//input[@id='chk_hospotal_readmission']").click() # Checkbox
driver.find_element(By.XPATH,"//label[normalize-space()='Medicaid']").click()
time.sleep(2)

# Select date from Calender
driver.find_element(By.XPATH,"//input[@id='txt_visit_date']").send_keys("15/10/2024")
time.sleep(2)

# Comment box
driver.find_element(By.XPATH,"//textarea[@id='txt_comment']").send_keys("I want to make a appointment")
driver.find_element(By.XPATH,"//button[@id='btn-book-appointment']").click()
time.sleep(2)

# Take screenshot of Appointment confirmation page
driver.save_screenshot(os.getcwd()+'\\confirmationpage1.jpg')
driver.close()