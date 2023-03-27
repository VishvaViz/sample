""" num=436
s=0
while num>0:
    s=s*10+num%10
    num=num//10
    print(s) """
p=[]
n=[]
for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
            n.append(i)
            break
    else:
        p.append(i)

print(p)
print(n)
   
    



