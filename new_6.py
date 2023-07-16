# from selenium import webdriver
# from selenium.webdriver.common.by import  By
# from selenium.webdriver.common.service import Service
# import time
# # ser_ob=Service("C:\\Drivers\\chromedriver.exe")
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.ID,"email").send_keys("manikumar8484@gmail.com")
# driver.find_element(By.ID,"pass").send_keys("M@ni2525")
# driver.find_element(By.NAME,"login").click()
# time.sleep(5)

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get("https://www.orangehrm.com/en/hris-hr-software-demo/")
# driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
# drop=driver.find_element(By.ID,"Form_getForm_Country").send_keys("India")
# time.sleep(10)
# def select_val(element,value):
#     sel=Select(element)
#     sel.select_by_visible_text(value)
# ele_in=driver.find_element(By.XPATH,"//select[@id='Form_getForm_Country']")
# select_val(ele_in,"India")
# time.sleep(5)
# select_val(ele_in,"Algeria")
# time.sleep(5)

# def sel(element,value):
#     print(len(element))
#     for ele in element:
#         if ele=="India":
#             ele.click()
#             break
# x=driver.find_elements(By.XPATH,"//select[@id='Form_getForm_Country']/option")
# ob1=sel(x,"India")

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(5)
# driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
# driver.maximize_window()
# dropdown=driver.find_element(By.ID,"justAnInputBox").click()
# time.sleep(4)
# dropdown_list=driver.find_elements(By.XPATH,"LLL")
# print(len(dropdown_list))
# for ele in dropdown_list:
#     print(ele.text)
#     if ele=="choice 3":
#         ele.click()
#         break

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(5)
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.maximize_window()
# driver.find_element(By.ID,"select2-billing_country-container").click()
# list_drop=driver.find_elements(By.XPATH,"//span[@aria-label='Country']//span[@role='presentation']")

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Samsung phones")
# driver.find_element(By.XPATH,"//*[@id='p_89/Samsung']/span/a/span").click()
# time.sleep(4)
# driver.quit()


# for ele in list_drop:
#     if ele.text=="Iceland":
#         ele.click()
#         break
# time.sleep(4)

#switching multiple tabs

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(5)
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.maximize_window()
# driver.switch_to.new_window("tab")
# driver.get("https://www.google.com")
# driver.back()
# time.sleep(5)

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2023 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print("Value error occured")
# except ZeroDivisionError:
#     print("zero division error occured")

# class Person:
#     sch="ABC school"
#     def __init__(self,id,name="mani",age=23):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.skills=[]
#     def show(self):
#         print(f" this is the person name: {self.name} and age: {self.age} and id is : {self.id}")
#
#     def add_skill(self,skill):
#         self.skills.append(skill)
# p1=Person(125)
# p1.show()
# p1.add_skill("html")
# p1.add_skill("python")
# print(p1.skills)
# print(Person.sch)
# print(p1.sch)

# class Person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def getemp(self):
#         print(f" the name of the employe : {self.name} and age :{self.id}")
#     def details(self):
#         return False
# class Emp(Person):
#     def details(self):
#         return " the deatisl are correct"
# ob1=Person("mani",26)
# ob2=Emp("kumar",23)
# ob1.getemp()
# print(ob1.details(),ob2.details())

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
# broserdriver="firefox"
# if broserdriver=="chrome":
#     driver=webdriver.Chrome(ChromeDriverManager().install())
# elif broserdriver=="firefox":
#     driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
# elif broserdriver=="safari":
#     driver=webdriver.safari
# else:
#     print(" please choose the correct browser")
#     raise Exception("driver is not found ")
#
# driver.implicitly_wait(5)
# driver.get("http://www.google.com")
# print(driver.title)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# import time
#
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
# driver.implicitly_wait(3)
# driver.find_element(By.ID,"justAnInputBox").click()
# x=driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
# for i in x:
#     print(i.text)
#     if i.text=="choice 2 2":
#         i.click()

# linklist=driver.find_elements(By.TAG_NAME,"a")
# print(len(linklist))
# for ele in linklist:
#     print(ele.text)
#     print(ele.get_attribute("href"))
# time.sleep(2)
# driver.close()

# import requests
#
# url = 'https://gorest.co.in/'
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     # Process the retrieved data
# else:
#     print('Error:', response.status_code)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# import time
#
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.spicejet.com/profile/sign-in")
# driver.implicitly_wait(10)
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.LINK_TEXT,"Sign Up").click()
# list_ele=driver.find_elements(By.TAG_NAME,"form-control form-select ")
# select=driver.find_elements(By.CSS_SELECTOR,"options.form-control form-select ")
# select=Select(list_ele)
# select.select_by_visible_text("Mr")

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get("https://www.orangehrm.com/en/hris-hr-software-demo/")
# driver.maximize_window()
# def select_val(ele,value):
#     select=Select(ele)
#     select.select_by_visible_text(value)
#
# ele_indus=driver.find_element(By.NAME,"Country")
# # select_val(ele_indus,"India")
# # select=Select(ele_indus)
# # select.select_by_visible_text("India")
# select=Select(ele_indus)
# list=select.options
# print(len(list))
# for ele in list:
#     print(ele.text)
#     if ele.text=="India":
#         ele.click()
#         break
# time.sleep(5)
# driver=driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[4]/a").click()
# time.sleep(5)
# driver.quit()

# def sel(option_list,val):
#     for ele in drop_list:
#         print(ele.text)
#         for k in range(len(val)):
#             if ele.text==val[k]:
#                 ele.click()
#                 break

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
# driver.get("https://amazon.in")
# time.sleep(4)
# driver.find_element(By.ID,"justAnInputBox").click()
# time.sleep(4)
# drop_list=driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
# val=["choice 2","choice 3"]
# sel(drop_list,val)
# x=driver.current_window_handle
# print(x)

# l1=[{"a":[1,2],"b":[4,5],"c":[8,9]}]
# l2=[]
# for i in l1:
#     for k,v in i.items():
#         l2.append((k,)+tuple(v))
# print(l2)
# l=[11,22,33,44]
# d1={l[i]:l[i+1] for i in range(len(l))}
# print(d1)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# import time
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"#FirstName").send_keys("shurts")
# time.sleep(3)
# x=driver.find_elements(By.CSS_SELECTOR,"select[name='DateOfBirthDay']")
# select=Select(x)
# select.select_by_visible_text("5")
# # driver.find_element(By.XPATH,"//button[@type='submit']").click()
# print(len(x))
# time.sleep(5)
# for ele in x:
#     print(ele.text)
#     if ele.text==5:
#         ele.click()
#         break

#

# def greetings (name):
#     message = name + ', welcome to Python for Everyone!'
#     return message
#
# print(greetings('Asabeneh'))


# def add(*s):
#     t=0
#     for i in s:
#         t=t+i
#     print(t)
# add(11,22)

# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output=['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# l1=[]
# l2=[ " ".join(i[0]) for i in names]
# print(l2)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import pytest
# import time
#
# def test_t1():
#     option=webdriver.ChromeOptions()
#     option.add_experimental_option("detach",True)
#     driver=webdriver.Chrome(options=option)
#     driver.get("https://www.facebook.com")
#     ele=driver.find_element(By.ID,"email")
#     ele.clear()
#     ele.send_keys("manikumar8484@gmail.com")
#     ele_pass=driver.find_element(By.ID,"pass")
#     ele_pass.clear()
#     ele_pass.send_keys("M@ni2525")
#     ele_login=driver.find_element(By.NAME,"login").click()



















