from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

driver.implicitly_wait(0.5)

first_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")

last_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")

email = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")

company_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")

role_in_company = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")

address = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")

phone_number = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")

time.sleep(2)
first_name.send_keys("RPA Team")

time.sleep(2)
last_name.send_keys("RPA last")

time.sleep(2)
email.send_keys("RPA email")

time.sleep(2)
company_name.send_keys("RPA company")

time.sleep(2)
role_in_company.send_keys("RPA junior")

time.sleep(2)
address.send_keys("RPA EUA")

time.sleep(2)
phone_number.send_keys("RPA 0101010101")

"""
Estrutura do Relative XPath
//: Este prefixo indica que você está procurando o elemento em qualquer lugar do documento, não apenas a partir da raiz.
O Selenium irá buscar todos os elementos <input> que atendem à condição especificada,
independentemente de onde eles estão na estrutura do DOM.

input: Isso especifica que você está procurando por elementos do tipo <input>.
Portanto, a busca será feita apenas entre os elementos <input>.

[@ng-reflect-name='labelPhone']: Este é um filtro que especifica que você deseja encontrar apenas aqueles elementos <input>
que têm um atributo ng-reflect-name com o valor exato 'labelPhone'.
O uso dos colchetes [] permite filtrar elementos com base em seus atributos.
"""