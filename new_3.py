# import re
# ip="192.121.52.63"
# exp=("(25[0-5]|1[0-9][0-9]|1[1-9]?[0-9]\.{3})(25[0-5]|1[0-9][0-9]|1[1-9]?[0-9])")
# m=re.match(exp,ip)
# if m:
#     print(m.group(),"valip ip")
# else:print("not valid ip")

# string = "Today is monday"
# #"yadoT si yadnom"
# # s=str[::-1]
# s1=string.split()
# # print(s1)
# x=(" ".join(s1[::-1]))
# print(x[::-1])

# l=[10,20,30]
# try:
#     print("the index is",l[0])
#     print("the index is ",l[5])
#     print("the index is ",l[1])
# except Exception as e:
#     print(e)
# finally:print("atleast the program is executed")

# filename=input("enter the file name:")
# with open(filename,mode="r") as f:
#     data=f.read()
#     print(data)

# file=input("enter filename")
# with open(file,"r") as f:
#     data=f.read()
#     print(data)

# file=input("enetr:")
# with open(file,"r") as f:
#     data=f.readline()
#     while data!="":
#         print(data,end=" ")
#         data=f.readline()

# file=input("enetr file")
# with open(file,"r") as f:
#     data=f.readlines()
#     for i in data:
#         print(i,end="")

# file=input("enetr")
# try:
#     with open(file,"r") as f:
#         data=f.read()
#         print(data)
# except Exception as obj:
#     print(obj)
# finally:print("file is executed if found")

# import re
# mobile=input("enetr mailid:")
# exp="[a-zA-Z0-9_\-\.]+[@][a-z][\.[a-z]{2,3}"
# m=re.match(exp,mobile)
# if m:print(m.group())
# else:print("invalid")

# def start(b):
#     l=[]
#     for i in b:
#         c=i
#         x=c.lower().split()
#         for j in x:
#             l.append(j)
#             print(l)
# x=["mani is good in python"]
# start(x)

# def s(x):
#     x[0]=20
# lst=[1,2,3,4,5]
# s(lst)
# print(lst)

# x=5
# def func():
#     a=9
#     print(a)
# func()
# print(a)

# x=5
# def outer():
#     a=9
#     print(a)
#     def inner():
#         b=10
#         c=a+b+x
#         print(c)
#     inner()
#     print(a)
# outer()

# import pytube
# link=input("enetr link:")
# yt=pytube.YouTube(link)
# yt.streams.first().download()
# print("downloaded",link)

# class math:
#     sum=0
#     def __init__(self,a,b):
#         self.sum=a+b
#     def show(self):
#         print(self.sum)
# ob=math(2,5)
# ob.show()

# class mul(math):
#     mul=0
#     def __init__(self,c,d):
#         self.mul=c*d
#     def show1(self):
#         print(self.mul)
# ob1=mul(5,5)
# ob1.show1()
# ob1.show()

# class stu:
#     school="abc"
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def show(self):
#         print("studient details:",self.name,self.age,self.id,self.school)
#     def change(self,new_age):
#         self.age=new_age
#     @classmethod
#     def modify(cls,new_name):
#         cls.school=new_name
# ob=stu("mani",25,69)
# ob.show()
# ob.id=55
# ob.show()
# ob.change(28)
# stu.modify("oxford")
# ob.show()


# x=list("python")
# print(x)
# for i in enumerate(x):
#     print(i,end=" ")
# a,b,c=1,3,5
# if a>0:
#     if b<2:
#         print("hello")
#     elif c>3:
#         print("hi")
# else:print("prohr")

# x,y,z=5,7,2
# if x>1:
#     if y<3:
#         print("welcome")
#     elif z>1:
#         print("done")
# else:print("executed")

# l=[1,2,[3,4,5],6,7,8]
# l1=[];l2=[]
# for i in l:
#     if type(i)==list:
#         l1.extend(i)
#     else:l1.append(i)
# print(l1)
# for i in l:
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
#     else:l2.append(i)
# print(l2)

# l1=[[1,2,3],[4,5,6],[7,8,9]]
# l2=[]
# for i in l1:
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
# print(l2)
# l3=[j for i in l1 for j in i]
# print(l3)

# l1=["a","b",1,2]
# l2=[];l3=[]
# for i in l1:
#     if type(i)==int:
#         l2.append(i)
#     elif type(i)==str:
#         l3.append(i)
# print(l2,l3)

# d1={"a":1,"b":24,"c":{"mani":25,"d":55}}
# print(d1["c"]["d"])
# d1.update({"n":66})
# print(d1)
# d1["c"].update({"f":59})
# print(d1)
# print(d1.get("z","not found"))

# f1=open("test.txt","r+")
# f2=open("tup","r+")
# x=f1.readlines()
# f2.write(x)
# f1.close()
# f2.close()
# for i in x:
#     print(i)

# f1=open("tup","r+") #7338677142
# x=f1.readlines()
# r=""
# for i in x:
#     r=i+r
# print(r)
# f1.close()

# l=[10,20,30,10,10,15]
# l1=[];s=set()
# for ind,val in enumerate(l):
#     if val not in s:
#         s.add(val)
#     else:l1.append(ind)
# print(s,l1)

# l1=[10,20,30,10,20,3]
# l2=[];l3=[]
# for i in l1:
#     if l1.count(i)>1 and i not in l2:
#         l2.append(i)
# print(l2)
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]==l1[j]:
#             l2.append(l1[i])
# print(l2)
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1,l1[-2])
























