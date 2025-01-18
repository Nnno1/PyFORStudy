import random as ra
print('生成随机数的小程序')
try:
    a=int(input())
except ValueError:
    print('Invalid input, please enter an integer.')
if a==1:
    origin,ending=int(input('随机数起点是：')),int(input('随机数末尾是：'))
    RandomNumber=ra.randint(origin,ending)
    print(RandomNumber)
elif a==2:
    origin,ending=int(input('随机数起点是：')),int(input('随机数末尾是：'))
    RandomNumber=ra.randint(origin,ending)
    RandomLittleNumber=ra.random()
    print(RandomNumber*RandomLittleNumber)
elif a==3:
    origin,ending=int(input('随机数起点是：')),int(input('随机数末尾是：'))
    RandomNumber=ra.uniform(origin, ending)
    print(RandomNumber)
else:
    print('False')