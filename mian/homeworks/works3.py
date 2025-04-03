i=1
base=1
pi=1
c=0
while True:
    base+=2
    c=((-1)**i)*(1/base)
    i+=1
    pi+=c
    if abs(c)<10**(-6):
        break
print(pi*4)