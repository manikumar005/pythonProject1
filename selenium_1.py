# from selenium import webdriver
# from selenium.webdriver.common.by import  By
# from selenium.webdriver.common.service import Service
# import time
# # ser_ob=Service("C:\\Drivers\\chromedriver.exe")
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.ID=="email").send_keys("manikumar8484@gmail.com")
# driver.find_element(By.ID=="pass").send_keys("M@ni2525")
# driver.find_element(By.NAME=="login").click()
# time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element().clear()
driver.find_element(By.CLASS_NAME=="inputtext _55r1 _6luy").send_keys("manikumar848@gmail.com")
driver.find_element(By.ID=="pass").send_keys("M@ni2525")
driver.find_element(By.NAME=="login").click()









