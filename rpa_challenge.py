from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Ler o arquivo Excel
df = pd.read_excel('challenge.xlsx')

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

driver.implicitly_wait(0.5)

start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
start_button.click()

# Localizando os botões dentro do for, pq eles podem mudar a cada refresh da pagina.
for index, row in df.iterrows():
    input_first_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
    input_last_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
    input_email = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
    input_company_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
    input_role_in_company = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
    input_address = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
    input_phone_number = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']")
    
    input_first_name.send_keys(row['First Name'])
    input_last_name.send_keys(row['Last Name '])
    input_email.send_keys(row['Email'])
    input_company_name.send_keys(row['Company Name'])
    input_role_in_company.send_keys(row['Role in Company'])
    input_address.send_keys(row['Address'])
    input_phone_number.send_keys(row['Phone Number'])
    
    submit_button.click()

print("Finalizado")