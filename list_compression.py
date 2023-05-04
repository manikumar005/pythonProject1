# l=[2,4,6]
# for i in l:
#     print(i*2,end=", ")
# print(l)
#
# l1=[i*i for i in range(1,5)];l2=[]
# print(l1)
# for i in range(1,6):
#     l2.append(i*i)
# print(l2)

# l=filter(lambda x: x%2==0,range(1,11))
# print(l,list(l))
# l=filter(lambda x:x%2==0,range(1,15))
# print(l,list(l))
# l1=[i for i in range(1,15) if i%2==0]
# print(l1)

# l=[[1,2,3],[4,5,6],[7,8,9]];l1=[]
# for i in l:
#     for j in i:
#         a=l1.append(j)
# print(l1)
# l3=[j for i in l for j in i]
# print(l3)

# l1=['red','green','blue']
# l2=[0,1,2]
# l3=[(n1,n2) for n1,n2 in zip(l1,l2)]
# l4=[(i,j) for i,j in zip(l1,l2)]
# l5={i:j for i,j in zip(l1,l2)}
# # print(l3,l4,l5)
# d1={}
# for k,v in zip(l1,l2):
#     d1[k]=v
# print(d1,l3,l4,l5)

# def main():
#     print("hello")
#     print("python is an language")
# main()
# main()
# def main(n):
#     print(n)
# main("mani is a good boy")

# def main(a,*b):
#     print(a,b)
# main(25,55)
# main("mani","python")
# main("ok",1,5,"mani")

# def integer():
#     result=int(input("enter"))
#     print(result)
# integer()
# integer()
# integer()

# def integer():
#     result=int(input("enter:"))
#     return result
# def mani():
#     print("started")
#     output=integer()
#     print(output)
#     print("ok done")
# if __name__=="__main__":
#    mani()

# def inte():
#     res=int(input("enter:"))
#     return res
# def m():
#     print("started the function")
#     out=inte()
#     print(out)
# if __name__=="__main__":
#     m()

# def inter():
#     result=int(input("enter:"))
#     return result
# # inter()
# print(inter())
#
# # def m():
# #     result=int(input("enter:"))
# #     print(result)
# # m()

# def n():
#     result=int(input("enter:"))
#     return result
# def Main():
#    print("Started")
#    output=n()
#    print(output)
# if __name__=="__main__":
#     Main()

# Main()
# def m():
#     result=int(input("enetr: "))
#     return result
# def output():
#     print("started ")
#     enter=m()
#     print(enter)
# if __name__=="__main__":
#     output()
# output()

# num=int(input("enetr num:"))
# if num>55:
#     print("you enter number is correct",num)
# elif num<55:
#     print("you enter numbet is ok ",num)
# else:print("I am ok with any number")

# l=[]
# for i in range(len(l)):
#     n=int(input("enter: "))
#     l.append(n)
#     print(l,n)

# import math
# def fun():
#     num=-85
#     x=math.fabs(num)
#     print(x)
# fun()

# import keyword
# print(keyword.kwlist)

# for i in "greeksfor greeks":
#     print(i,end=" ")
# print("\r")

# for i in range(1,10):
#     print(i,end=" , ")
#     if i ==6:
#         break
#
# for i in range(1,10):
#     if i==8:
#         break
#     print(i,end=" ")

# loop from 1 to 10
# i = 0
# while i < 10:
#     if i == 6:
#         i += 1
#         continue
#     else:
#         # otherwise print the value
#         # of i
#         print(i, end=" ")
#
#     i += 1
#
# i=0
# while i<10:
#     if i==6:
#         i=i+1
#         continue
#     else:
#         print(i,end=" , ")
#     i+=1

# def fun():
#     s=0
#     for i in range(10):
#         s=s+i
#     return s
# x=fun()
# print(x)
# for i in str(fun()):
#     print(i,end=" , ")
#
# def fun():
#     S = 0
#     for i in range(10):
#         S += i
#         yield S
# for i in fun():
#     print(i,end=" , ")

# a=5.6
# b=int(a)
# print(b,type(b),type(a),a)
# a="hello world"
# print(a,type(a),id(a))
# a="5"
# x=int(a)
# print(int(a),type(a),type(x))
# b=int(a)
# print(b,type(b))

# b=5
# x=float(b)
# print(x)
# k=6
# c=complex(b,k)
# print(c,type(c))
# y=complex(k,b)
# print(y,type(y))

# a=5
# b=9
# c=a<b
# d=a>b
# print(c,type(c))
# print(a>b)
# print(d,type(d))
# print(int(True),int(False))

# s="hello navi\n kumar"
# x=range(10)
# print(x,type(x))
# y=list(range(10))
# print(y)
# print(list(range(2,10,2)))
# print(list(range(1,15,2)))
# z=list(range(1,15,3))
# print(z,type(z))

# d={"a":25,"b":55,"c":99}
# print(d.get("a"),d.get("f"))
# print(d["b"])

# fo=open("tup","w")
#
# fo1=open("abc","r")
# print(fo1.readline(),end="")
# print(fo1.readline())
# print(fo1.readline(),end="")
# print(fo1.readlines())
# for data in fo1.read():
#     print(data,end="")
# for data in fo1.read(15):
#     print(data,end="")
# for data in fo1:
#     print(fo.write(data))

# l=["a",20,"b",38]
# d={};l1=l[0::2];l2=l[1::2]
# for k,v in zip(l1,l2):
#     d[k]=v
# print(d,l1,l2)
# x={l[i]:l[i+1] for i in range(0,len(l),2)}
# print(x)
# for k,v in range(0,len(l),2):
#     d[k]:[v+1]
# print(d)

# for i,j in range(0,len(l),2):
#     d[i]:j
# print(d)
# x={i:j for i,j in enumerate(l)}
# print(x)

# x="mani kumar"
# s=""
# for i in x:
#     s=i+s
# print(s)

# x="mani kumar is attending the interview"
# s=x.split()
# print(s)
# for i in s:
#     if i=="attending":
#         y=i[::-1]
# print(y," ".join(s))
# l=x.split()
# r=l[3][::-1]
# l[3]=r
# print(" ".join(l),l)

# for i in s:
#     if i==3:
#         a=x.index(i[::-1])
#         s[3]=a
# print(x,"".join(x))

# l=[1,2,3,4,5,6]
# l1=[]
# for i in l:
#     if i%2==0:
#         x=l1.append(i*i)
#     else:x=l1.append(i*i*i)
# print(l1)
# s=[i*i if i%2==0 else i*i*i for i in l]
# print(s)

# l1=[2,3,4,5,45,9,45,55,66,45,99,49]
# c=0
# n=l1[0]
# for i in l1:
#     x=l1.count(i)
#     if x>c:
#         c=x
#         n=i
# print(n,c)

# def n(l):
#     # l=[2,3,2,45,3,5,45,2,45,35,45,66,99,69]
#     c=0
#     n=l[0]
#     for i in l:
#         x=l.count(i)
#         if x>c:
#             c=x
#             n=i
#     print(n,c)
# n([33,2,45,3,5,45,2,45,35,45,66,99,69])
# n((33,44,55,44,3,2,44,55,66))

# l=["mani","kumar","machine","learning"]
# d={}
# d1={k:len(k) for k in l}
# print(d1)
# for i in l:
#     d[i]=len(i)
# print(d)

# d={"mani 01":25,"mani 02":35,"mani 03":45}
# d2={}
# for k,v in d.items():
#     x=k.replace(" ","")
#     d2[x]=v
# print(d2)

# d1={"raj":"mani 01","raj1":"mani 02","raj3":"mani 03"}
# d4={}
# for k,v in d1.items():
#     y=v.replace(" ","")
#     d4[k]=y
# # print(d4,d4["raj"],d4.values(),d4.keys())
# d4["python"]="good"
# print(d4)
# d4[(1,2)]="mani"
# print(d4)
# d4["i"]={"wow":"play","nice":"good"}
# print(d4)
# print(d4["i"]["nice"])

# l1=[2,5,3,4,5,6,7,5,6,6]
# for i in l1:
#     if i==5:
#         x=l1.index(i)
#         l1[x]="mani"
# print(l1)

# for i in l1:
#     if i==6:
#         x=l1.index(i)
#         l1[x]="raj"
# print(l1)

# n=int(input("enter num"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime",n)
#             break
#     else:print("prime",n)

# if "s" in "greeks for greeks":
#     print("s id part of greeks for greeks")
# else:print("s is not part of greeksfor greeks")

# for i in "greeks for greeks":
#     print(i,end="")
# print("\r")

# for i in range(10):
#     print(i,end=" ")
#     if i==6:
#         break
# print()
#
# for i in range(10):
#     if i==6:
#         break
#     print(i,end=" ")
# for i in range(10):
#     print(i,end=" ")

# l=[2,3,4,5,5,3,6,7,8,5,9,5,6,3,5,6,3,5]
# c=0
# m=l[0]
# for i in l:
#     x=l.count(i)
#     if x>i:
#         c=x
#         m=i
# print(m,c)
#
# def n(l):
#     c=0
#     m=l[0]
#     for i in l:
#         x=l.count(i)
#         if x>c:
#             c=x
#             m=i
#     print(c,m)
# n([6,6,6,6,6,6,6,6,4,45,3,4,5,6,3,4,5,6,5,7,69])
# n((1,2,3,4,5,6,2,3,4,2,3,2,5,6,2,7,8,2,9))

# d={"mani 01":25,"mani 02":45,"mani 03":55}
# d1={}
# for k,v in d.items():
#     x=k.replace(" ","#")
#     d1[x]=v
# print(d1)
#
# def di(dii):
#     d2={}
#     for k,v in dii.items():
#         x=k.replace(" ","%$")
#         d2[x]=v
#     print(d2)
# di({"rai 01":25,"raj 02":45,"raj 03":99})

# s1="malayalam"
# s2=""
# for i in range(len(s1)):
#     for j in range(i+1,len(s1)):
#         x=s1[i:j]
#         y="".join(reversed(x))
#         if x==y:
#             print(x,end=" ")
# def mal(s1):
#     for i in range(len(s1)):
#         for j in range(i+1,len(s1)):
#             x=s1[i:j]
#             r="".join(reversed(x))
#             if x==r:
#                 print(x,end=" ")
# # mal("malayalam")
# mal("mani")

# def fun():
#     s=0
#     for i in range(10):
#         s=s+i
#     return s
# x=fun()
# print(x)


# def fun():
#     s=0
#     for i in range(10):
#         s=s+i
#         yield s
# for i in fun():
#     print(i)
# def fun():
#     S = 0
#     for i in range(10):
#         S += i
#         yield S
# for i in fun():
#     print(i)

# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)

# a, b = input("Enter two values: ").split()
# print("First number is {} and second number is {}".format(a, b))
# x,y =[int(i) for i in input("enter : the num").split()]
# print(x,y)
# a,b=[int(i) for i in input("enter the numbet:").split()]
# print("enetr the a value",a)
# print("enter the b value ",b)

# x=[int(i) for i in input("enetr ").split()]
# print(x)

# import os
# # print(os.path)
# path=input("enter the path:")
# if os.path.isfile(path):
#     print(f"the pathis is {path} is a file")
# elif os.path.isdir(path):
#     print(f"the path is {path } is a directory")
# else:print(f"the pathe is {path} is not exixts ")

# l1=["a","b"];l2=[1,2]
# l3=[]
# for i in l1:
#     for j in l2:
#         x=i+str(j)
#         l3.append(x)
# print(l3)
# l4=[i+str(j) for i in l1 for j in l2]
# print(l4)

# import random
# l=[]
# x=random.choices(range(1,15),k=5)
# print(x)
# for i in range(1,5):
#     y=random.randint(1,20)
#     l.append(y)
# print(l)
# i=1
# while i<10:
#     x=random.randint(1,20)
#     i=i+1
#     l.append(x)
# print(l)
# while i<10:
#     x=random.randint(11,25)
#     i=i+1
#     l.append(x)
# print(l,len(l))

# l=[1,"a","b",2]
# l1=[];l2=[]
# for i in l:
#     if type(i)==str:
#         l1.append(i)
#     else:l2.append(i)
# print(l1,l2)
# for i in l:
#     if type(i)==int:
#         l1.append(i)
#     else:l2.append(i)
# print(l1,l2)

# d={"mani 01":25,"mano 02":35,"mani 03 ":45}
# d1={}
# for k,v in d.items():
#     x=k.replace(" ","$$")
#     d1[x]=v
# print(d1)

# l=[2,3,2,3,4,5,6,22,33,2,3,45]
# l1=[];l2=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:l2.append(i)
# print(l1,l2)

# s1="aaaabbbccd"
# s2=""
# for i in s1:
#     x=i.count(i)
#     d=int(x)

# s="malayalam"
# s1=""
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         x=s[i:j]
#         y=x.replace(i)
#     if x==y:
#         print(i)

# import re
# txt="Pyton is we good language"
# exp=re.search("^P*",txt)
# if exp :
#     print("mathced")
# else:print("not matched")

# def pattern(n):
#     x=0
#     for i in range(0,n):
#         x=x+1
#         for j in range(0,i+1):
#             x=x+1
#             print(x,end=" ")
#         print()
# pattern(5)

# x=5
# def add():
#     x=3
#     x=x+5
#     print(x)
# add()
# print(x)

# def add(a,b):
#     return a+5,b+5
# x=add(3,2)
# print(x)

# def add(a,b):
#     return a+5,b+2
# x=add(2,3)
# print(x)

# s1={1,2,3,int("4"),5}
# print(s1)
# s2={3,str(4),5}
# print(s1.union(s2))
# x,y="12"
# y,z="34"
# print(x+y+z,x,y,z)
# x,y="mai"
# print(x,y)

# class Stu:
#     schoolname="abc school"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print("studient:",self.name,self.age,Stu.schoolname)
# s1=Stu("mani",25)
# s1.show()

# class stu:
#     schoolname="vikas school"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print("studient:",self.name,self.age,stu.schoolname)
# s1=stu("mani",26)
# s2=stu("raj",55)
# s1.show(),s2.show()

# class stu:
#     schoolname="vikas school"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print("studient",self.name,self.age,stu.schoolname)
#     def chg_age(self,new_age):
#         self.age=new_age
#     @classmethod
#     def modi(cls,new_name):
#         cls.schoolname=new_name
# s1=stu("mani",26)
# s1.show()
# s1.chg_age(29)
# # stu.modi("abc school")
# s1.show()

# class stu:
#     schoolname="abc_school"
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def show(self):
#         print("Studient:",self.name,self.age,stu.schoolname)
#     def chg(self,new_age,new_id):
#         self.age=new_age
#         self.id=new_id
#     @classmethod
#     def modi(cls,new_name):
#         cls.schoolname=new_name
# s1=stu("mani",26,25)
# s1.show()
# s1.chg(55,59)
# stu.modi("vikas sckool")
# s1.show()

# class fruit:
#     def __init__(self,name,colour):
#         self.name=name
#         self.colour=colour
#     def show(self):
#         print("fruit is ",self.name,"and colour is ",self.colour)
# s1=fruit("apple","red")
# s1.show()
# s1.colour="white"
# s1.show()
# s1.name="bananna"
# s1.show()



















