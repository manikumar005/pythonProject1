# from selenium import webdriver
# driver=webdriver.Chrome()
# # driver.get("https://www.facebook.com/home.php")
# driver.get("https://www.facebook.com/login.php")
# driver.find_element("email").send_keys("manikumar8484@gmail.com")
# driver.find_element("password").send_keys("M@ni2525")

from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://www.ajio.com/shop/men")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='appContainer']/div[1]/div/header/div[3]/div[2]/form/div/div/input").send_keys("Jeans")
driver.find_element(By.XPATH,"//*[@id='appContainer']/div[1]/div/header/div[3]/div[2]/form/div/div/input").click()





