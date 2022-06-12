
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




class Google():
    def __init__(self, driver = webdriver.Chrome(executable_path=r'C:\Users\Nazbeen\Documents\Projects\Python\Games\Automation\chromedriver.exe')):
        self.driver = driver
        self.driver.get("http://www.google.com")
     


    def firstPage(self):
        elem = self.driver.find_element(By.NAME, "q")
        searchbox=input('What you Want Search  From Googe ? : ')
        elem.send_keys(searchbox)
        elem.send_keys(Keys.RETURN)

        self.driver.quit()


run=Google()
run.firstPage()