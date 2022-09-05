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

class directory(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_search_employee_with_job_title_location(self): 
        driver = self.driver
        driver.get ('https://opensource-demo.orangehrmlive.com')
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
    ## LOGIN
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    ## DIRECTORY
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span").click() 
        time.sleep(1)
    ## Job title
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[18]").click()
        time.sleep(1)
    ## Location
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]").click()
        time.sleep(1)
    ## Button search
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(2)
    ## click result
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div/div").click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
