from lib2to3.pgen2 import driver
from pydoc import describe
import unittest
from urllib import response
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class employee(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_add_employee(self): 
        driver = self.driver
        driver.get ('https://opensource-demo.orangehrmlive.com')
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
    ## LOGIN
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)
    ## Add employee
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
        time.sleep(1)
    ## First name
        driver.find_element(By.NAME, "firstName").send_keys("Jang")
        time.sleep(1)
    ## Middle name
        driver.find_element(By.NAME, "middleName").send_keys("Won")
        time.sleep(1)
    ## Last name
        driver.find_element(By.NAME, "lastName").send_keys("Young")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys("06521")
        time.sleep(1)
    ## Save
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(15)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()