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

class timesheets(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_edit_my_timesheets(self): 
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
    ## TIME
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() 
        time.sleep(1)
    ## submenu timesheets
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span/i").click()
        time.sleep(1)
    ## my timesheets    
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click()
        time.sleep(1)
    ## Click edit
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button").click()
        time.sleep(2)
    ## Edit timesheet
        ## project
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div/input").send_keys("coca")
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div[2]/div/span").click()
        time.sleep(2)
        ## activity
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div[2]/div[9]").click()
        time.sleep(1)
        ## input 5
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[3]/div/div[2]/input").send_keys("9.00")
        time.sleep(1)
        ## input 6
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[4]/div/div[2]/input").send_keys("8.00")
        time.sleep(1)
        ## input 7
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[5]/div/div[2]/input").send_keys("10.00")
        time.sleep(1)
    ## Click save
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[3]").click()
        time.sleep(15)        

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()