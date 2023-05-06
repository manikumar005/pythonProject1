# from collections import Counter
# # import collections
# x=["a","b","a","a",1,2,3,4]
# y=Counter(x)
# print(y["a"],y[1])

# l=[1,10,20,2,3,2,4,3,1,1,1]
# l1=[];l2=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     elif i not in l2:l2.append(i)
# print(l1,l2)

# for i in l:
#     if l.count(i)>1 and i not in l1:
#         l1.append(i)
# print(l1)

# l1=[10,20,30];l2=[40,50,60]
# l3=[]
# for i,j in zip(l1,l2):
#     # l3.extend([i,j])
#     l3.append(i)
#     l3.append(j)
# print(l3)

# find the positive and negative numbers
# a=10
# print("even num",a) if a%2==0 else print("odd num")
# a=1
# {print("hello"),print("this is evern num")} if a%2==0 else {print("odd"),print("this")}

# n=int(input("enter:"))
# if n==1:
#     print("this monday")
# elif n==2:
#     print("tues")
# elif n==3:
#     print("wed")
# elif n==4:print("thur")
# else:print("invalid num")

# check the largest of 2numbers and 3 numbers
# n1=int(input("enetr the largest num"))
# n2=int(input("enetr the largets num"))
# n3=int(input("enetr the largets num"))
# if n1>n2 and n1>n3:
#     print("largets num",n1)
# elif n2>n1 and n2>n3:
#     print("largest",n2)
# elif n3 > n1 and n3 > n2:
#     print("largest",n3)
# else:print("the numare egual")
# if n1>n2:
#     print("n1 is largest number")
# elif n2>n1:print("n2 is the largest number")
# else:print("gi=ven 2numbers are equal")

# for i in range(10):
#     print(i,end=" ")
# print(list(range(2,5)))
# print(list(range(10)))
# print(list(range(1,10,2)),list(range(2,10,2)))
# print(list(range(10,1,-1)))

# i=1
# while i<10:
#     # print(i)
#     i=i+1
#     print(i)
#     print("done")

# i=1
# while 0:
#     i=i+1
#     print(i)
# print("done")

# i=10
# while i>2:
#     i=i-1
#     print(i)
#
# for i in range(1,18,2):
#     if i==5 :
#         continue
#     print(i)

# print(min("welcome"))
# s="welcome"
# r=""
# for i in s:
#     r=i+r
# print(r)

# d=["mani","kumar","python","machine","fine"]
# d1={i:len(i) if len(i)>5 else "short" for i in d}
# print(d1)
# d2={}
# for i in d:
#     if len(i)>5:
#         d2[i]=len(i)
#     else:d2[i]="short"
# print(d2)

# l=["app","pineapple","orange"]
# l1=[]
# for i in range(len(l)):
#     if l[i]=="app":
#         l[i]="apple"
# print(l)

# l=["a","b","c",55]
# for i in range(len(l)):
#     if l[i]=="a":
#         l[i]="mani"
#     if l[i]==55:
#             l[i]="69"
# print(l)
# l1=["mani" if l[i]=="c" else l[i] for i in range(len(l))]
# l2=["kumar" if i=="a" else i for i in l]
# print(l1,l2)
# for i in l:
#     if i=="b":
#         i="raj"
#
# print(l)
# def modifi(lis,replace_with,replace_in):
#     return [replace_in if i==replace_with else i for i in lis]
# l=["mani","a","b","c"]
# x=modifi(l,"a","kumar")
# print(x)

# l=[[1,2,3],["a","b","c"]]
# print(*l)
# l1=zip(*l)
# print(tuple(l1))


#you no need to appolige the next time onwards you should me careful hey every one make mistake even i make mistake
#if any some one make mistake not a big deal it could not the matter
#last time when i content post
#
#

# class myclass:
#     def mc1(self):
#         print("this is an instance method")
#     @staticmethod
#     def mc2(self,n1,n2):
#         print(self,n1,n2)
# x=myclass()
# x.mc1()
# x.mc2(2,8)
# myclass.mc2(5,4)
# myclass.mc1("mani")
# c=55
# class myclass:
#     a,b=10,20
#     print(a,b,c)
#     def fun1(self):
#         print(self.a+self.b,c)
#     def mul(self):
#         print(self.a*self.b)
# x=myclass()
# x.fun1()


# x.mul()


