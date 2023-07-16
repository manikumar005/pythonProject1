# Print the commom repaited thing in two stings
# def comm():
#     s1=input("enetr:")
#     s2=input("enetr:")
#     l1=set(s1)
#     l2=set(s2)
#     l3=l1 & l2
#     print(l3)
# comm()

# print the no.of charaters in a srting
# def st():
#     s1=input("enetr:")
#     s2=s1.split()
#     d={}
#     for i in s2:
#         if i in d:
#             d[i]+=1
#         else:d[i]=1
#     print(d)
# st()

# s1="basically the san envirenment is good san is using block level san using the iscsi protocol"
# s2=s1.split()
# d={i:s2.count(i) for i in s2}
# print(d)
# d={}
# for i in s2:
#   d[i]=d.get(i,0)+1
# print(d)
# for i in s2:
#     if i not in d.keys():
#         d[i]=0
#     d[i]+=1
# print(s2,d)

# d1={'color','shape','fruit'}
# d2={'red','circle','apple'}
# d3={k:v for k,v in zip(d1,d2)}
# print(d3)

# l1=[11,22,33]
# l2=[44,55,66]
# d={i:j*2 for i,j in zip(l1,l2)}
# print(d)

# class classexp:
#     x=2
#     @classmethod
#     def modif(cls):
#         cls.x=5
#         print(cls.x)
# ob=classexp
# print(ob.x)
# ob.modif()
# print(ob.x)

# class static:
#     y=20
#     @staticmethod
#     def change():
#         y=49
#         print(y)
# s1=static
# print(s1.y)
# s1.change()
# print(s1.y)

# l=[11,22,33,[10,5,55,21],[45,25,64],69,99]
# l2=[]
# for i in l:
#     if type(i)==list:
#         l2.extend(i)
#     else:l2.append(i)
# print(l2)
# for i in l:
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
#     else:l2.append(i)
# print(l2)

# l1=[i for i in range(10) if i%2==0]
# print(l1)
# l2=["mani","mk","kumar","ani"]
# l3=[len(i) for i in l2]
# print(l3)
# l4={i:len(i) for i in l2}
# print(max(l4.values()))
# print(sum(l4.values()))
# print(min(l4.keys()))
# print(l4,max(l4.keys()))
# print(l4)
# l5={};s=0
# for i in l2:
#     l5[i]=len(i)
# print(l5)
# for k,v in l4.items():
#     s=s+v
# print(s)
# m=l4["mani"]
# for i in l4:
#     s=s+l4[i]
# print(s)
# for k,v in l4.items():
#     if v>s:
#         s=v
# print(v)

# l=[11,22,5,34,21,55]
# for i in range(2,len(l)+1):
#     i=i+1
#     if i%3==1:
#         l[i-2]="a"
# print(l)
#
# for i in range(2,len(l)+1):
#     i=i+1
#     if i%3==1:
#         l[i-2]="b"
# print(l)

# import re
# n="85005015572"
# exp="[6-9]{1}[0-9]{9}$"
# m=re.match(exp,n)
# if m:
#     print(f'{m.group()} is valid number')


# def hello():
#     """"This function prints
#        message on the screen"""
#     print('Hello, World!')
# hello()

# a=5
# def add():
#     b=4
#     c=a+b
#     print(c)
# add()

# a=5
# def add(*l):
#     s=0
#     for i in l:
#         s=i+s
#     return s
# y=add(2,3,4,5)
# print(y)
#
# l=[11,22,1]
# s=0
# for i in l:
#     s=s+i
# print(s)

# class Vehicle:
#     def description(self):
#         print(" here is going to print the vechicle  class")
# class Car(Vehicle):
#     def speed(self):
#         print(" the vehicvle speed is good ")
# v=Vehicle()
# c=Car()
# v.description()
# c.description()
# c.speed()

# class Vehicle:
#     def __init__(self,color):
#         self.color=color
#     def dec(self):
#         print(" I am the", self.color, " and a vehicle")
# class Car(Vehicle):
#     def __init__(self,color,style):
#         super().__init__(color)
#         self.color=color
#         self.style=style
#     def dec(self):
#         print("I'm a", self.color, self.style)
# v=Vehicle("red")
# c=Car("green","rvg")
# # v.dec()
# c.dec()

# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# l = [];d={}
# for f, v in zip(fruits, vegetables):
#     l.append({'fruit':f, 'veg':v})
# print(l)
# for k,v in zip(fruits,vegetables):
#     d[k]=v
# print(d)

# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# *a,b,c=names
# print(a,b,c)
# *a,b,c=names
# print(f' the value a :{a} and the b : {b}')
d={"a":25,"b":45,"c":[11,22,33,44],"d":["mani","kumar"]}
d1={};l1=[]
for k in d:
    print(k,d[k])


















