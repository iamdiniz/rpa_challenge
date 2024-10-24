from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

first_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")