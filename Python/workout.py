'''user1=int(input("Enter the Number1:"))
user2=int(input("Enter the Number2:"))

s=0

for i in range(user1):
    s=s+user2
print(s)

user1=int(input("Enter the Number:"))

for i in range(2,user1):
    if user1%i==0:
        print(f"{user1} not a prime")
        break
else:
    print(f"{user1}is a prime")
count=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            print(f"{i}is not a prime")
            break
    else:
        count=count+1
        print(f"{i}a prime")
print(count)
count=0
for i in range(1,100):
    for j in range(1,i):
        if i%j==3:
            print(f"{i}is by three")
            break
    else:
        count=count+1
        print(f"{i}a not by three")
print(count)'''
'''s=0 
for i in range(1,11):
    s=s+2
    print(f"2*{i}={s}")
c=0
for i in range(1,100,2):
    print(i)
    c=c+1
print("count",c)'''

'''user1=int(input("Enter the Number:"))
user2=int(input("Enter the Number:"))
c=0
for i in range(user1,user2):
    for j in range(2,i):
        if i%j==0:
            print(f"{i} not a prime number")
            break
    else:
        c=c+1
        print(f"{i}is a prime number")
print(c)'''
'''#ficbonacii serires
num=4
a=0
b=1
for i in range(num):
    c=a+b
    a=b
    b=c
    print(c)'''

'''for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()'''

'''for row in range(7):
    for col in range(6):
        if (row==0 and col==4) or (col-row==1) or (col-row==3) or row==3 or (col==0 and row==4)or(col==0 and row==5):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()'''

'''for row in range(5):
    for col in range(5):
        print(row*2,end="")
    print()'''

'''row=int(input())
for i in range(row):
    for j in range(0,i+1):
        
        print(i+1,end="")
    print()'''
'''for row in range(5):
    for col in range(5):
        print(row+1,end=" ")
    print()'''

'''row=0
while row<5:
    
    row+=1
    col=0
    while col<5:
        print(col,end=" ")
        col+=1
    print()'''
'''totalweight=0
for i in range(1,11):
    weight=int(input("Enter the Number:"))
    totalweight=totalweight+weight
    average=weight/i
print(average)
print(totalweight)'''
'''e=0

for i in range(1,101,):
    if i%2==0:
        e=e-2
        print(f"{e}",end=" ")
    else:
        
        print(f"{i}")'''
'''a=0
b=1
num=100
for i in range(num):
    c=a+b
    a=b
    b=c
print(c)'''
'''for row in range(5):
    for col in range(row):
        print(row,end="")
    print()'''

'''student=["rishi ammai","vishva","laskmi","sam","hari","rupak","kiruthiv"]
lenght=len(student)
index=0
while index<lenght:
    print(student[index])
    index=index+1'''
student_marks=[23,45,89,90,56,80]
'''length=len(student_marks)
index=0
total_marks=0
while index<len(student_marks):
    total_marks=student_marks[index]+total_marks
    index=index+1
print("Total Marks:"  + str(total_marks))'''
'''print(student_marks[0])
print(student_marks[1])
print(student_marks[2])
s=0
for i in range(6):
    print(student_marks[i])
    s=s+student_marks[i]
print(s)'''

'''data=[20,40,60,70,30,79]
less=[]

if less in data<50:
        data.append(less)
else:
        print(data)'''

'''data=[20,30,40,50,60,70,80,90]
l=0
g=0

for i in range(len(data)):
    
    if data[i]<50:
        l=l+1
    else:
        g=g+1  
print(f"the count of less than:{l}")
print(f"the count of greater than:{g}")'''
'''data=[20,30,40,50,60,70,80,90]
l=0
g=0
for i in range(len(data)):
    if data[i]>=20 and data[i] <=40:
        l=l+1
print(l)'''
'''c=0
e=[]
o=[]
data=[3,4,5,5,6,45,6,7,3,45,5,32]
for i in range(len(data)):
    if data[i]%2==0:
        data.append([e])
    else:
        data.append(o)
print(data)
#print(e)'''
#data=[3,4,5,5,6,45,6,7,3,45,5,32]
#print(min(data))
'''data=[3,4,5,5,6,45,6,7,3,45,5,32]
l=1000
for i in range(len(data)):
    if l>data[i]:
        l=data[i]
print(f"largest number is{l}")'''

'''data=[3,4,5,5,6,45,6,7,3,5,32]
l=0
s=0
for i in range(len(data)):
    if l<data[i]:
        s=l
        l=data[i]
    elif s<data[i]:
        s=data[i]
print(s)
print(l)'''

# string=str(input("enter the string:"))
'''a = [1,0,1]
if a==a[::-1]:
    print(a,"is palindrome")
else:
    print(a,"not a palindrome")'''
'''data=[1,2,3,4,5,6,7,8,9,10]
a=[]
for i in range(9,-1,-1):
    a.append(data[i])
print(a)'''
'''data=[1,2,3,4,5,6,7,8,9,10]
data1=[1,2,3,4,5,6,7,8,9,10]
#data1=[11,12,13,14,15,16,17,18,19,20]
e=[]
n=[]
for i in range(len(data)):
    if data[i] ==data1[i]:
        e.append(i)       
    else:
        n.append(i)
#print(e)
#print(n)
if len(n)==0:
    print('equal')
else:
    print('not equal')'''

# data=[1,0,1]
# e=[]

# for i in range(2,-1,-1):
#     e.append(data[i])
# for j in range(3):
'''data=[2,3,4,5]
l=0
for i in range(len(data)):
    if l<data[i]:
        l=data[i]
print(l)'''
marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
]
'''total=0
for i in range(3):
    for j in range(5):
        total=total+marks[i][j]
print(total)'''
#print(marks[2][4])
'''data=[78,76,94,86,88]
l=100
for i in range(len(data)):
    if l<data[i]:
        l=data[i]
print(l)'''
'''data=[78,76,94,86,88,110]

l=0
s=0
for i in range(len(data)):
    if l<data[i]:
        s=l
        l=data[i]      
print(s)'''
'''data=[2,3,4,5,6,7,8,9]
c=0
e=0
for i in range(len(data)):

    num=data[i]
    for k in range(2,num):
        if num%k==0:
            print(num,"not a prime")
            c=c+1
            break
    else:
        e=e+1
        print(num,"Prime num")
print(c,e)'''

'''data=[2,3,4,5,6,7,8,9]
p=0
n=0
for i in range(len(data)):
    num=data[i]
    for j in range(2,num):
        if num%j==0:
            p=p+1
    else:
        n=n+1
print(n,p)'''

# data=[2,3,4,5,6,7,9,8]
# l=0
# s=0
# for i in range(len(data)):
#     if l<data[i]:
#         s=l
#         l=data[i]
#     elif data[i]>s:
#         s=data[i]
# print(s)

# marks=[
#     [78,76,94,86,88],
#     [91,71,98,65,76],
#     [95,45,78,52,49]
# ]

# for i in range(3):
#     total=0
#     for j in range(5):
#         total=total+marks[i][j]
#     average=total//5
#     print("average of",str(i+1),"year","is",average)

    
# data=[78,76,94,86,88]
# l=0
# s=0
# for i in range(len(data)):
#     if l<data[i]:
#         s=l
#         l=data[i]
#     elif s<data[i]:
#         s=data[i]
# print(s)
'''data=[78,76,94,86,88,89]
l=0
s=0
for i in range(len(data)):
    if l<data[i]:
        s=l
        l=data[i]
    elif s<data[i]:
        s=data[i]
print(s)'''
# data=[78,76,94,86,88,89]
# s=1000
# ss=1000

# for i in range(len(data)):
#     if s>data[i]:
#         ss=s
#         s=data[i]
#     elif s>ss:
#         ss=data[i]
# print(ss)
# data=[78,76,94,86,88,89]
# l=0
# s=0
# t=0
# f=0
# for i in range(len(data)):
#     if l<data[i]:
#         s=l
#         t=s
#         f=t
#         l=data[i]
#     elif s<data[i]:
#         t=s
#         s=data[i]    
#     elif t>s:
#         f=t
#         t=data[i]
#     elif f>t:
#         f=t
#         f=data[i]
# print(f)

'''marks=[
    [78,76,94,86,88,91,71,98,65,76],
    [91,71,98,65,76,91,71,98,65,76],
    [95,45,78,52,49,91,71,98,65,76],
    [91,71,98,65,76,91,78,76,94,86],
    [95,45,78,52,49,91,71,98,65,76]
]
for i in range(5):
    total=0
    for j in range(9):
        total=total+marks[i][j]
    average=total//9
    print(int(average))'''

'''data=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(data)):
    for j in range(len(data)):
        if data[i]+data[j]==10:
            print(data[i],"+",data[j],"=10")'''
'''data=[
    [1,2,3],
    [2,3,4],
    [3,4,5]
]

for row in range(len(data)):
    s=0
    for col in range(len(data)):
        s=s+data[row][col]
        
    print(s)'''
# data=[
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
# ]
# for i in range(3):
#     for j in range(3):
#         l=data[i][j]
#         print(l)
s=0
for i in range(1,11):
    s=s+3
    print(f"3*{i}={s}")


        

    
    







