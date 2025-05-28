import secrets as se
import random as r
def a1(total,mode=False):
    ls,d=[],{0:0,1:0}
    if mode:
        for i in range(total):
            a=r.randint(0,1)
            ls.append(int(a))
    else:
        for i in range(total):
            a=se.randbelow(2)
            ls.append(int(a))        
    for i in ls:
        if ls[i]==0:
            d[0]+=1
        else:
            d[1]+=1
    print(f'{(d[0]/total)*100:.2f}',end=',')
for i in range(5):
    print(f'{a1(10)}',end=' ')
for i in range(5):
    print(f'{a1(10,True)}',end=' ')