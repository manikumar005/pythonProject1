
# class com:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def
# c1=com("i5","12gb")
# c2=com("rayazn",25)
# print(c1.com,c2.com)

# n=5
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print(" * ",end=" ")
#     print()

# class A:
#     def __init__(self):
#         print("a is in init method")
#     def fea1(self):
#         print("fea 1 is working")
#     def fea2(self):
#         print("fea 2 is working")
# class B(A):
#     def fea3(self):
#         print("fea 3 is working")
#     def fea4(self):
#         print("fe 4 is working")
# class C(A):
#     def __init__(self):
#         # super().fea2()
#         print("c is init clsaa")
#     def fea5(self):
#         super().fea1()
#         print("fea 5 is working")
#
# c1=C()
# # c1.fea2()
# c1.fea5()

# f1=open("abc","r+")
# r=""
# x=f1.readlines()
# for i in x:
#     r=i+r
# f1.seek(0)
# f1.write(r)
# f1.close()

# f1=open("abc","r+")
# r=""
# x=f1.readlines()
# for i in x:
#     r=i+r
# f1.seek(0)
# f1.write(r)
# f1.close()

# def s(s1):
#     c=0
#     n=s1[0]
#     for i in s1:
#         x=s1.count(i)
#         if x>c:
#             c=x
#             n=i
#     print(c,n)
# s("mani kumar")

# def s(s1):
#     c=0
#     n=s1[0]
#     for i in s1:
#         x=s1.count(i)
#         if x>c:
#             c=x
#             n=i
#     print(n,c)
# s("chennai")

# l=[1,2,3,2,4,5,2,6,7,5,5,5,5,5,5,5]
# c=0
# n=l[0]
# for i in l:
#     x=l.count(i)
#     if x>c:
#         c=x
#         n=l[i]
# print(c,n)

# s1="mani kumar is attending the interview"
# x=s1.split()
# print(x)
# for i in x:
#     if i==3:
#         y=x.index(i[::-1])
# print(x," ".join(x))
# y=x[3][::-1]
# x[3]=y
# print(" ".join(x))

# l=["a",20,30,"b"]
# print({l[i]:l[i+1] for i in range(0,len(l),2)})
# d={}
# for i in range(0,len(l),2):
#     l[i]=l[i+1]
# print(d)

# l=[10,20,30]
# try:
#     print("index of list",l[0])
#     print("index",l[10])
# except:
#     print("error excorter")
# finally:print("the program executed")

# s1="kumar"
# def name(func):
#     print(s1)
#     func()
# @name
# def greet():
#     print(s1.upper())

# s1="kumar"
# def name(func):
#     print(s1)
#     func()
# @name
# def greet():
#     print(s1.upper())
#
# s2="mani kumar"
# def fun(name):
#     print(s2)
#     name()
# @fun
# def change():
#     print(s2.upper())



# l=[10,20,30,40,50,60]
# print(l[1::-1])

# l=[10,20,55,12,33,99];l1=[]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         l[i],l[j]=l[j],l[i]
# print(l)

# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# def mani(l):
#     c=0
#     n=l[0]
#     for i in l:
#         x=l.count(i)
#         if x>c:
#             c=x
#             n=i
#     print(n,c)
# mani([11,22,33,44,11,3,44,55,44,556,44,3])

# s="aabbccdc"
# s1=""
# for i in (s):
#     if i in s1:
#         d=i
#     else: s1=s1+d*s1.count(i)
# print(s1)

# class Person():
#     def __init__(self,name,age,can_vote):
#         self.name=name
#         self.age=age
#         self.can_vote=can_vote
#     @staticmethod
#     def adult(age):
#         if age>=18:
#             return True
#         else:return False
#     @classmethod
#     def vote(cls,name,age):
#         if cls.adult(age)==True:
#             return cls(name,age,"yes")
#         else:return cls(name,age,"no")
# ob1=Person.vote("mani",25)
# ob2=Person.vote("rj",15)
# print(ob1.name,ob1.can_vote)
# print(ob2.name,ob2.can_vote)


# class Stu:
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#     def show(self):
#         return self.name, self.age
# s1=Stu("mani",25)
# print(s1.show())

# class Stu:
#     name="mani"
#     @classmethod
#     def chnage(cls):
#         print(cls.name)
# s1=Stu()
# s1.chnage()

# class stu:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def modif(cls,name,age):
#         return cls(name,age+1)
# s1=stu("mani",26)
# s1=stu.modif("kum",25)
# print(s1.name,s1.age)
# print(s2.name,s2.age)

# class Num:
#     @staticmethod
#     def even(x):
#         if x%2==0:
#             return x,True, " evern "
#         else:return x,False
# ob=Num()
# print(ob.even(22))

# d={" name1 ":22," name2 ":45}
# d1={}
# for k,v in d.items():
#     x=k.replace(" ","")
#     d1[x]=v
# print(d1)

import re
# sen="8500501557"
# exp="[\d][0-9]{9}"
# m=re.match(exp,sen)
# if m:
#     print(m.group()," valid")
# else:print("not valid ")

# s=" hello welcome to world the sentence is 10.5 and 111 and 45.5 hello 11"
# exp="[\d]+[\d\.]+"
# m=re.findall(exp,s)
# print(m)

# s2=" hello welcome to world the sentence is 10.5 and 111 and 45.5 hello 11"
# exp="[a-zA-Z0-9\.\-]+"
# m=re.match(exp,s2)
# if m:
#     print(m.group(),"valid sentence")
# else:print("invalid sentence")

# def find_duplicates(lst):
#     return list(set([item for item in lst if lst.count(item) > 1]))

# Example usage
# my_list = [1, 2, 3, 4, 1, 2, 5, 6, 3,1]
# print(find_duplicates(my_list))
#
# def dup(l):
#     x=set([i for i in l])
#     print(x)
# dup([11,22,1,2,3,11,2,1,22])

# def find_duplicates(lst):
#     duplicates = {}
#     for item in lst:
#         if item in duplicates:
#             duplicates[item] += 1
#         else:
#             duplicates[item] = 1
#     return [item for item, count in duplicates.items() if count > 1]
# # Example usage
# my_list = [1, 2, 3, 4, 1, 2, 5, 6, 3]
# print(find_duplicates(my_list))














