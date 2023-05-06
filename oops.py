
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














