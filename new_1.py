

# a,b=0,1
# for i in range(0,15):
#     print(a,end=" , ")
#     a,b=b,a+b

# def even():
#     for i in range(10):
#         if i%2==0:
#             print("even",i)
#         else:print("odd",i)
# even()

# def even(n):
#     if n%2==0:
#         print("even",n)
#     else:print("odd",n)
# even(5)
# even(6)
# even(44)


# def add(n):
#     a=6
#     b=n+a
#     print(b)
# add(4)
# add(2)


# class stu:
#     school_name="abc"
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def show(self):
#         print("studient details:",self.name,self.age,self.id,stu.school_name)
#     @classmethod
#     def ch_cls(cls):
#         stu.school_name=
# obj=stu("mani",25,125)
# obj.show()

# class emp:
#     def __init__(self,name,sal,pro):
#         self.name=name
#         self.sal=sal
#         self.pro=pro
#     def show(self):
#         print("name",self.name,"sal",self.sal)
#     def work(self):
#         print(self.name,"is working",self.pro)
# ob=emp("mani",25000,"hcl company")
# ob.show()
# ob.work()
# ob1=emp("kumar",80000,"wipro")
# ob1.work()

# class stu:
#     school_name="vikas school"
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def show(self):
#         print(self.name,self.age,self.id,stu.school_name)
#     def change_age(self,new_age):
#         self.age=new_age
#     @classmethod
#     def modify(cls,new_name):
#         cls.school_name=new_name
# s1=stu("mani",26,45)
# s1.show()
# s1.change_age(28)
# s1.show()
# s1.modify("abc school")
# s1.show()
# s1.id=55
# s1.show()

# class fruit:
#     def __init__(self,name,colour):
#         self.name=name
#         self.colour=colour
#     def show(self):
#         print("fruit is ",self.name,"and colour is ",self.colour)
# obj=fruit("apple","red")
# obj.show()
# obj.name="strabbery"
# obj.show()

# class sbi:
#     def property(self):
#         print("the property is belong to :")
#
# class andhra(sbi):
#     def pro1(self):
#         print("this belong to india property")
# ob=sbi()
# ob.property()
# ob1=andhra()
# ob1.property()
# ob1.pro1()

# a=lambda x:x+5
# print(a(3))
# print(a(4))
# b=lambda x,y:x+y
# print(b(2,3))

# class vehicle:
#     def __init__(self,name,colour,price):
#         self.name=name
#         self.colour=colour
#         self.price=price
#     def show(self):
#         print("details: ",self.name,self.colour,self.price)
#     def max_speed(self):
#         print("vehicle max speed is 150")
#     def chnage_gear(self):
#         print("vehicle change 6th gear")
#
# class car(vehicle):
#     def max_speed(self):
#         print("car max speed is 200")
#     def chnage_gear(self):
#         print("car change is 6th")
# ob=car("maruthi","red",750000)
# ob.show()
# ob.max_speed()
# ob.chnage_gear()
# ob1=vehicle("truct","brown",95000)
# ob1.show()
# ob1.max_speed()
# ob1.chnage_gear()

# s1="aaaabbbcc"
# s2=""
# for i in s1:
#     if i not in s2:
#         s2=s2+i+str(s1.count(i))
# print(s2)
#
# s3="a3b2c1"
# s4=""
# for i in s3:
#     if i.isalpha():
#         d=i
#     else:s4=s4+d*int(i)
# print(s4)

# n=int(input("enter:"))
# if n>1:
    # for i in  range(2,n):
    #     if n%i==0:
    #         print("not prime num",n)
    #         break
    # else:print(" prime")

# class studient:
#     school="vikas school"
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id =id
#     def show(self):
#         print("studuent details:",self.name,self.age,self.id,studient.school)
#     def change(self,new_age,new_id):
#         self.age=new_age
#         self.id=new_id
#     @classmethod
#     def modify(cls,new_school):
#         cls.school=new_school
# ob=studient("mani",25,125)
# ob.show()
# ob.change(29,55)
# ob.show()
# ob.modify("oxford school")
# ob.show()

# import re
# def match(text):
#     pattern="^\w+"
#     if re.search(pattern,text):
#         return("found the match")
#     else:return "not match"
# print(match("everythink is matches 123"))
# print(match("123 "))

# import array
# def ar(l):
#     s=0
#     for i in l:
#         s=s+i
#     print(s)
# ar(array.array("i",[1,2,3,4,5,-15]))
# ar(array.array("i",[2,3,4]))
# ar(array.array("i",(2,3)))

# import re
# def par(text):
#     pattern="ab{3}.$"
#     if re.search(pattern,text):
#         return "fount the correct match"
#     else:return "no fount"
# par("aabbcccc")
# print(par("aabbcc"))
# print(par("aabbbc"))

import re
# s="greeks.for greeks"
# exp=re.search(".",s)
# print(exp)
# exp1=re.search("\.",s)
# print(exp1)
# string = """Hello my Number is 123456789 and
#             my friend's number is 987654321"""
# exp=re.findall("\d",string)
# exp1=re.search("\d",string)
# print(exp)
# print(exp1)
# p = re.compile('\d+')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# s1=input("enter")
# s2=input("extter")
# if s1==s2:
#     print("enter the password is correct")
# else:print("not correct")

# x=filter(lambda x:x%2==0, [1,2,3,45,5,6])
# print(x,list(x))
# y=map(lambda x:x*2,[1,2,3,4])
# print(y,list(y))
# import functools
# l1=[1,3,4,5,6]
# l2=functools.reduce(lambda x,y:x+y,l1)
# print(l2)

# x=lambda x:x*2+2
# print(x(4))

# l1=[1,2,3]
# l2=["a","b","c"];l3=["1",25,35]
# z=list(zip(l1,l2,l3))
# # print(z,list(z))
# # print(set(zip(l1,l2)))
# a,b,c=list(zip(*z))
# print(a,b,c,z)

# d=dict()
# d["a"]=45
# d["b"]=65
# print(d)
# for i in d:
#     print(i,":",d[i])

# s="greeksforgreeks"
# for i in s:
#     if i=="e" or i=="s":
#         continue
#     print(i,end=" , ")

# fo=open("D:python file.txt","r+")
# x=fo.read()
# fo.write("mani you can do your best")
# fo.write("\n")
# fo.write("today the interviwe will be successful")
# print(x)
# import os
# x=os.getcwd()
# print(x)

# line=4
# fo=open("tup","r")
# cline=1
# for i in fo:
#     if cline==line:
#         print(i)
#         break
#     cline=cline+1

# line=3
# fo=open("D:/python file.txt","r")
# cline=1
# for i in fo:
#     if cline==line:
#         print(i)
#         break
#     cline=cline+1
# print(cline,line)
# fo.close()

import os,sys
# print(os.getcwd())
# os.mkdir("D:\\python")
# os.rmdir("D:\\python")
# os.remove("D:\\python file.txt")
# print(sys.version)
# print(os.path.join("C:\\Users\\admin\\PycharmProjects\\pythonProject1","C:\\Users\\admin\\PycharmProjects\\pythonProject1\\new_1.py"))
# print(os.path.split("C:\\Users\\admin\\PycharmProjects\\pythonProject1\\new_1.py"))
import subprocess

# n=int(input("enetr"))
# d={}
# for i in range(n):
#     k=input("enetr")
#     v=int(input("enetr:"))
#     d[k]=v
# print(d)

# l=[11,22,33,44,55,66,3,5]
# for i in l:
#     if i==3:
#         x=l.index(i)
#         l[x]="mani"
#     if i==5:
#         y=l.index(i)
#         l[y]="m"
# print(l)

# for i in l:
#     if i==3:
#         l[i]="ok"
#     if i==5:
#         l[i]="kk"
# print(l)

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# s1="mani kumar is python"
# s=s1.split()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:d[i]=1
# print(d)
# for i in d:
#     print(i,":",d[i])

# s=143
# r=""
# for i in str(s):
#     r=i+r
# print(r)

# l=[22,33,2,3,55,3,4,3,4,3]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# c=0
# n=l[0]
# for i in l:
#     x=l.count(i)
#     if x>c:
#         c=x
#         n=i
# print(c,n)

# def s(text):
#     return text.upper()
# def s1(text1):
#     return text1.lower()
# # x=s1("MANI ku")
# # print(x)
# def greet(t1):
#     x="hello COME TO THIS WORLD ok fine"
#     return x
# print(greet())









