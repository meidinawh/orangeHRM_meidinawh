from lib2to3.pgen2 import driver
from pydoc import describe
from re import search
import unittest
from urllib import response
from xml.dom.minidom import Element
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class leave(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_apply_leave(self): 
        driver = self.driver
        driver.get ('https://opensource-demo.orangehrmlive.com')
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
    ## LOGIN
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    ## LEAVE
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click() 
        time.sleep(1)
    ## Click apply
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
        time.sleep(1)
    ## Leave type
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
    ## From date
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[1]/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[19]").click()
        time.sleep(1)
    ## To date 
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[23]").click()
        time.sleep(1)
    ## Apply button
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(15)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()        