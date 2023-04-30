""" num=436
s=0
while num>0:
    s=s*10+num%10
    num=num//10
    print(s) """
# p=[]
# n=[]
# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#             n.append(i)
#             break
#     else:
#         p.append(i)

# print(p)
# print(n)
""" 
data=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
ss=1
for i in range(len(data)):
    s=0
    for j in range(3):
        s=s+data[i][j]
    ss=s*ss
    print(s)
print(ss) """



    
        


