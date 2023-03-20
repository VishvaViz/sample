'''diti=[1,2,3,4,5,6]
l=0
s=0
for i in ringe(len(diti)):
    if l<diti[i]:
        s=l
        l=diti[i]
    elif s<diti[i]:
        s=diti[i]
print(s)/'''
# diti=[1,2,3,4,5,6]
# e=[]
# o=[]
# for i in ringe(len(diti)):
#     if diti[i]%2==0:
#         e.ippend(diti[i])
#         print("even numbers ire",e)
#     else:
#         o.ippend(diti[i])
#         print("odd number ire",o)

# diti=[1,2,3,4,5,6]
# l=0
# for i in ringe(len(diti)):
#     if l<diti[i]:
#         l=diti[i]
# print(l)

'''i=11
b=100
c=90
d=i,b,c
l=0
s=0'''
# for i in ringe(len(d)):
#     if l<d[i]:
#         s=l
#         l=d[i]
#     elif s<d[i]:
#         s=d[i]
# print(s)
# a=153
# s=0
# aa=0
# while(a>0):
#     a=a//10
#     s=s+a%10
#     aa=(s+a%10)**3
# print(s)
# print(aa)
# #     if s==aa:
# #         print("true")
# # else:
# #         print("f")

# user=int(input("num:"))
num = [12, 75, 150, 180, 145, 525, 50]

# for i in range(len(num)):
#     if num[i]%5==0:
#         # if num[i]>150:
#         #     break
#         # continue
#     # elif num[i]>500:
#     #     break
#         print(num[i])
# user1=int(input("Enter the Number:"))
# user2=int(input("Enter the Number:"))
# c=0
# for i in range(user1,user2):
#     for j in range(2,i):
#         if i%j==0:
#             #print(f"{i} not a prime number")
#             break
#     else:
#         c=c+1
#         print(f"{i}is a prime number")
# print(c)
data=[
    [1,2,3],
    [5,6,7]
]
# print(data[0][0]+data[0][1]+data[0][2])
# print(data[1][0]+data[1][1],data[1][2])

'''print(data[0][0]+data[1][0])
print(data[0][1]+data[1][1])
print(data[0][2]+data[1][2])'''
'''
k=0
for i in range(6):
    k=k+1
print(k)
k=0
for i in range(5):
    k=k+1
print(k)
k=0
for i in range(4):
    k=k+1
print(k)
k=0
for i in range(3):
    k=k+1
print(k)
k=0
for i in range(2):
    k=k+1
print(k)
k=0
for i in range(1):
    k=k+1
print(k)'''

'''data=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
for row in range(3):
    a=0
    for col in range(3):
        a=a+data[row][col]
    print(a)

for row in range(3):
    b=0
    for col in range(3):
        b=b+data[col][row]
    print(b)'''
'''lis1=[1,2,3,4,5,6]
lis2=[2,3,1,0,6,7]
a=[]

for i in range(len(lis1)):
    if lis1[i] not in lis2:
        a.append(lis1[i])
print(a)'''
'''lis1=[1,2,3,4,5,6]
lis2=[2,3,1,0,6,7]

diff=set(lis1)-set(lis2)
print(diff)'''
marks=[
    [78,76,94,86,88],
    [91,71,98,65],
    [95,45,78]
]
'''s=0
for row in range(len(marks)):
    
    for col in range(len(marks[row])):
        s=s+marks[row][col]
    #av=s//5
    print(s)
# print(av)'''
'''a=[]
n=[10,11,12,13,14,17,18,19]
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i]+n[j]==30:
            a.append([n[i],n[j]])
print(a)
a=[1,2,3,4]
b=["a","b","c","d"]
c=0
while c<4:
    print(str(a[c])+b[c])
    c=c+1'''
'''data1=[1,2,3,4,5,6,7,8,9,10]
e=0
o=0
s1=0
s2=0
ev=[]
od=[]
for i in range(len(data1)):
    if data1[i]%2==0:
        ev.append(data1[i])
        s1=s1+data1[i]
        e=e+1

    else:
        od.append(data1[i])
        s2=s2+data1[i]
        o=o+1


print(ev)
print(od)
print(s1//e)
print(s2//o)
print(e)
print(o)'''
'''c=0
l=0
d=0
net=[1000,100,10,5,1,999,1500,1399,131,151,201]
for i in range(len(net)):
    if net[i]>=1000 :
        c=c+1
    elif net[i]>=100:
        l=l+1
    else:
        d=d+1
print(c,l,d)'''
""" dd=[]
s=[]
char=["a","n","t","a","a","t","n","n","a"]
for i in range(len(char)):
    a=0
    for j in range(i,len(char)):
        if char[i]==char[j]:
            a=a+1
    dd.append([char[i],a])
print(dd)"""
u=[]
data=[19,17,17,18,10,17,14,12,19,17,12,13,11]

for i in range(len(data)):
    a=0
    for j in range(len(data)):
        if data[j]==17:
            a=a+1
print(a)        



    






