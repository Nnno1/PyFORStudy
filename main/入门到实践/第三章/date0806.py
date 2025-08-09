from numpy import random

ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_list=list(ALPHA)
new_list=''

for i in range(26):
    res=random.choice(alpha_list)
    new_list+=res

print(new_list)