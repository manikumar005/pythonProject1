# l=[i*i for i in range(10)];l1=[]
# for i in range(10):
#     l1.append(i*i)
# print(l,l1)

# l=filter(lambda x:x%2==0,range(10))
# print(list(l))
# for i in range(10):
#     if i%2==0:
#         print(i,end=" ")
# l=[1,2,3,4,5,6,7,8,9]

# l=[i for i in range(20) if i%2==0 if i%4==0]
# print(l)
# l=["a","b","c"];l1=[1,2,3]
# l2=[(i,j) for i in l for j in l1]
# print(l2)

# l1=[[n for n in range(10) if n %2==0] for n1 in range(3)]
# print(l1)
# l2=[[i for i in range(10)] for j in range(3)]
# print(l1,l2)
# l=[]
# for i in range(5):
#     for j in range(3):
#         l.append(j)
# print(l)

# l={(i,i*i) for i in range(10) if i%2==0}
# print(l)

# l=["mani","kumar","python"]
# l1=[i for i in l if len(i)>=5]
# l3={i:len(i) for i in l if len(i)>=5}
# print(l1,l3)

# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# l=[1,1,2,3,4,4,5,5,6,1] #write a program to collect dupilcate elements
# s=set();l1=[]
# for i in l:
#     if i not in s:
#         s.add(i)
#     elif i not in l1:
#         l1.append(i)
# print(l1,s)

# import re
# test_string = "1w3e4r5t6y7u7i8i"
# exp="[0-9]+"
# m=re.findall(exp,test_string)
# m1=re.search(exp,test_string)
# print(m,"".join(m),m1.group())
# print(m1.group())

# x,y=input("enetr:").split()
# print(x)
# print(y)

# s="mani is working in python"
# x=s.split()
# print(" ".join(x[::-1]))
# print(x)

# l=[1,2,34,2,3,4,5,4,5,7,8,9,5]
# l1=[];l2=[]
# # for i in l:
# #     if l.count(i)>1 and i not in l1:
# #         l1.append(i)
# #     else:l2.append(i)
# # print(l1,l2)
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print(l1)
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j] :
#             l1.append(l[i])
# print(l1)

# l=[2,3,2,3,4,5,5,6,7,9,8,8]
# l1=[];l2=[]
# for i in l:
#     if l.count(i)>1 and i not in l1:
#         l1.append(i)
#     else:l2.append(i)
# print(l1,l2)

# for i in l:
#     if l.count(i)==1:
#         l1.append(i)
# print(l1)

# l="a a a b b b c c c"
# l1=l.split()
# print(l1)
# d={}
# for i in l1:
#     if i in d:
#         d[i]+=1
#     else:d[i]=1
# print(d)
# for i in d:
#     print(i,"",d[i],end=" ")

# l="a,a,a,c,b,b";l2=[]
# l1=l.split(",")
# print(l1)
# for i in l1:
#     if i not in l2:
#         # print(f"{i}:{l1.count(i)}")
#         l2.append(i)
#         print(i,":",l1.count(i))
# print(l2)

# l=[1,2,3,4]
# l.append(12)
# l.extend([2,3])
# print(l)
# print(l.count(2))
# print(l.index(12))
# print(l.insert(2,"mani"))
# print(l)
# l.insert(2,[10,20,30])
# print(l[2][1])
# l[2].insert(2,"kumar")
# print(l)
# print(l[2].index("kumar"))
# print(l[2].pop(1))
# print(l)

# t=(10,20);t1=(30,40)
# t3=t+t1
# print(t3)
# print(t3.index(20))
# print(t3)
# print(t3.count(20))
# print(len(t3))

# s=set();s1={20,30,40,50};s2={50,60,70,40}
# l1=[10,20,30];l2=[40,50]
# l3=l1+l2
# print(l3)
# print(s2.difference(s1))
# print(s1.discard(90))
# print(s1.remove(20))
# print(s1)

# d1={}
# d1.update({"a":25,"b":45})
# print(d1)
# d1["c"]=55
# print(d1)
# print(list(d1.values()),d1.keys())
# d1["a"]=99
# print(d1)
# print(d1.popitem())
# print(d1)

# s=0
# for i in range(10):
#     s=s+i
# print(s)

# c=5
# def some():
#     global c
#     c=c+1
#     print(c)
# some()
# def s():
#     a=5
#     global c
#     b=a+c
#     print(b)
# s()
# def s1():
#     a=5
#     b=a+c
#     print(b)
# s1()

# def inner():
#     print("inner function is activated")
#     def small_inner():
#         var=5
#         print(var)
#     small_inner()
# inner()

# y=10
# def outer_fun():
#     print("outer function is activated")
#     def inner_fun():
#
#         x=5+y
#         print("inner fuction value",x)
#     inner_fun()
#     print("ok fine",x)
# outer_fun()

# x=5
# def outer(l):
#     print("outer ")
#     def inner():
#         y=5+x
#         print("inner fun",y,x)
#     print(x)
#     inner()
#     print("fine")
# outer(1)

# program illustrates the use of docstrings

# x=[i for i in (input("enetr")).split()]
# print(x)

# s="python"
# x=0
# # for i in s:
# #     x=x+1
# #     print(s[0:x])
# for i in s:
#     x=x-1
#     print(s[0:x])

# x=[]
# y=[[0,1,2],[3,4,5],[6,7,8]]
# x.append([n[i] for n in y for i in range(3)])
# print(x)

# l=[]
# for n in y:
#     for i in range(3):
#         l.append(n[i])
# print(l)

# l1=[]
# for i in range(3):
#     for j in range(10):
#          if j%2==0:
#             l1.append(j)
# print(l1)

# [[n for n in range(10) if n %2==0] for n1 in range(3)]

# l=[1,2,3,4]
# l1=[4,5,6]
# for i in l:
#     if i in l1:
#         print("overlapping")
# else:print("not overlapping")

# print("I am welcome to this world \\n cool you can win")

# x="python"
# n=0
# for i in x:
#     n=n+1
#     print(x[0:-n])

# n=5
# for i in range(n):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# l=[10,20,30,40,50,60,70,80,20,30,20]
# c=0
# n=1
# for i in l:
#     x=l.count(i)
#     if x>c:
#         c=x
#         n=i
# print(c,n)

# def l(s):
#     c=0
#     n=1
#     for i in s:
#         x=s.count(i)
#         if x>c:
#             c=x
#             n=i
#     print(n,c)
# l("chennai maaa na")

# l=[6,1,2,3,1,2,4,5]
# l1=[];c=0
# for i in l:
#     x=l.count(i)
#     if x>1 and i not in l1:
#         l1.append(i)
# print(l1)

# import re
# str1="address:9-645, #road no:09 & mani_id:mani123"
# spl_char=r"[!@&%*&.#-]"
# m=re.findall(spl_char,str1)
# print(m)

# d={"a":25,"b":45,"c":25,"d":55}
# d1={v:k for k,v in d.items()}
# d2={v:k for k,v in d1.items()}
# print(d1,d2)

# d={"a":25,"b":45,"c":25}
# d1={v:k for k,v in d.items()}
# print(d1)
# d2={v:k for k,v in d1.items()}
# print(d2)

# s="python is an interpeter language and python is capuable of scripting"
# d=[];d1=[]
# x=s.split(" ")
# for i in x:
#     if s.count(i)>1 and i not in d:
#         print(d.append(i))
#     else:d1.append(i)
# print(d1," ".join(d))

# import re
# s1="mani kumar is python developer"
# exp="[aeiouAEIOU]"
# m=re.findall(exp,s1)
# print(m,len(m))

# l=[2,3,4,5,2,3,5,55,34,23]
# m=l[0]
# for i in l:
#     if i>m:
#         m=i
# print(m)

# d={"a":25,"b":45,"c":15}
# m=d["a"]
# for k,v in d.items():
#     if v>m:
#         m=v
# print(m)

# l="I am good in python am good in computer"
# l1=l.split()
# l2={i:len(i) for i in l1}
# print(l2)

# s1="I am good in python"
# x=s1.split()
# for i in x:
#     print(i[::-1],end=" ")
# y=x[::-1]
# print(y," ".join(y))
# for i in x:
#     print(i[::-1],end=" ")

# s="""mani is attending the interview having
#   he is attend
#   of fine """
# x,y,z=s.splitlines()
# a=y.split()[::-1]
# print(len(x),x,"".join(a),z)

# s="malay"
# if s==s[::-1]:
#     print("paladrom")
# else:print("not palandrom")
# print("".join(reversed(s)))
# r=""
# for i in s:
#     r=i+r
# print(r)

# def sqr(n):
#     for i in range(1,n+1):
#         yield i*i
# ob=sqr(5)
# print(next(ob))
# print(next(ob))

# def even():
#     n=0
#     while True:
#         n=n+2
#         yield n
# x=even()
# print(next(x))
# print(next(x))

# l=[25,55,66,88]
# l1=["mani" if i==55 else i for i in l]
# print(l1)
# l2=["m" if i==88 else i for i in l]
# print(l2)

# d1={"a":25,"b":45}
# d2={"c":55,"d":99}
# d3={**d1,**d2}
# print(d3)
# (d1.update(d2))
# print(d1,d2)

# l1=[1,2,3]
# l2=[3,4,5]
# l4=list(set(l1+l2))
# print(l4)

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y
# print("enetr the option:")
# print("a. add")
# print("b. sub")
# print("c. mul")
# print("d. div")
# choice=(input("select the option"))
# n1=int(input("enetr:"))
# n2=int(input("enter:"))
# if choice=="a":
#     print(n1,"+",n2,add(n1,n2))
# elif choice=="b":
#     print(n1,"-",n2,sub(n1,n2))
# elif choice=="c":
#     print(n1,"*",n2,mul(n1,n2))
# elif choice=="d":
#     print(n1,"/",n2,div(n1,n2))










