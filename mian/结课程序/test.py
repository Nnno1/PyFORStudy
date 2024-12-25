import random as ra
print('生成随机数的小程序')
try:
    a=int(input())
except:print('Flase')
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
    RandomNumber=ra.random(origin,ending)import os
file_path = 'your_file_path.csv'
if os.path.exists(file_path):
# 文件存在，可以进行读取操作
df = pd.read_csv(file_path)
else:
print('文件不存在')