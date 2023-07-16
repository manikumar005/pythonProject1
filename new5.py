
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# ser_obj=Service("C:\Drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https://www.ajio.com/shop/men")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='appContainer']/div[1]/div/header/div[3]/div[2]/form/div/div/input").send_keys("Jeans")
# driver.find_element(By.XPATH,"//*[@id='appContainer']/div[1]/div/header/div[3]/div[2]/form/div/div/input").click()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time
# ser_obj=Service("C:\Drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https:\\www.google.com")
# driver.find_element(By.ID=="input").send_keys("naveen automation")
# time.sleep(3)

# class stu:
#     x=2
#     @classmethod
#     def modify(cls):
#         x=5
#         print(x)
# ob=stu
#
# print(ob.x)
# ob.modify()
# print(ob.x)
# stu.modify()

# class stu:
#     x=2
#     @staticmethod
#     def modify():
#         x=5
#         print(x)
# ob=stu
# print(ob.x)
# ob.modify()

# class A():
#     def method1(self):
#         print("this is the first method")
#     def method2(self):
#         print("this is the second method")

# class B(A):
#     def method3(self):
#         print(" this is the third method")
#     def method1(self):
#         super().method1()
#         print(" this is new one so continue the working")
# ob=A()
# ob.method1()
# ob1=B()
# ob1.method1()

# n=5
# for i in range(n):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# def fib(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else:return fib(n-1)+fib(n-2)
# for i in range(10):
#     print(fib(i),end=" ")

# fib=[0,1]
# for i in range(10):
#     s=fib[i]+fib[i+1]
#     fib.append(s)
# print(fib)

# def fib(l):
#     for i in range(10):
#         s=l[i]+l[i+1]
#         l.append(s)
#     print(l)
# fib([1,2])






















