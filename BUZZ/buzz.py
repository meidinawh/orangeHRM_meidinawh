from lib2to3.pgen2 import driver
import unittest
from urllib import response
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class buz(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_buzz_page(self): 
        driver = self.driver
        driver.get ('https://opensource-demo.orangehrmlive.com')
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a").click()
        time.sleep(10)
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()