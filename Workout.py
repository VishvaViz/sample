'''for i in range(0,51):
    print(i)'''

'''i=50
while i>=50:
    print(i)    
    i+=1'''
'''for i in range(50,100):
    
    print(i-50)'''
'''i=50
while i<100:
    print(i-50)
    i+=1'''
'''for i in range(891,941):
    i=i-891
    print(i)'''
'''i=891
while i<941:
    print(i-891)
    i=i+1'''
'''for i in range(0,-11,-1):
    print(i)'''
'''i=0
while i>-11:
    print(i)
    i-=1'''

'''for i in range (156,166):
    print(i-156)'''
'''i=156
while i<166:
    
    print(i-156)
    i+=1'''

'''user1=int(input("Enter the Number1:"))
user2=int(input("Enter the Number2:"))
s=0
for i in range(user2):
    s=user1+s
print(s)'''
'''s=0
for i in range(int(input("Enter the Number:"))):
    num1=int(input("Enter the Number:"))
    s=num1+s
print(s)'''
'''user1=int(input("Enter the Number:"))
user2=int(input("Enter the Number:2"))
s=0
for i in range(user2):
    s=user1+s
print(s)'''

'''s=0
c=0
for i in range(10):
    num1=int(input("Enter the table:"))
    s=num1+s
    if s%2==0:
        c=c+1
print(c)'''

'''c=0 #cout the number this line
for i in range(10):
    c=c+1
print(c)'''

'''s=0
c=0
i=0
while i<=10:
    num1=int(input("Enter the Number:"))
    s=num1+s
    if s%2==0:
        c=c+1
    i=i+1
print(s)'''
'''s=0
for i in range(1,11):
    s=s+2
    print(f"2*{i}={s}")'''
'''s=0
user1=int(input("Enter the number:"))
for i in range(1,11):
    s=s+user1
    print(f"{i}*{user1}={s}")'''
'''i=0
while i<11:
    print(f"{i}*2={i*2}")
    i+=1'''

'''user=int(input("Enter the Number"))
for i in range(2,user):
    if user%2==0:
        print(f"{user}is not a prime")
        break
else:
    print(f"{user} is prime")'''
'''num=5
num1=11
num3=8
for i in range(2,num):
    if num%i==0:
        print(f"{num}is not prime")
        break
else:
    print(f"{num}is a prime")

for j in range(2,num1):
    if num1%j==0:
        print(f"{num1}is not prime")
        break
else:
    print(f"{num1}is a prime")

for k in range(2,num3):
    if num3%k==0:
        print(f"{num3}is not prime")
        break
else:
    print(f"{num3}is a prime")'''
c=0
for i in range(100,201):
    for j in range(2,i):
        if i%j==0:
            print(f"{i} is not a prime")
            break
    else:
        print(f"{i}is a prime")
        c=c+1
print(c)

    

    



