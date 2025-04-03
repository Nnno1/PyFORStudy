import random as ra
names=['李润','张艺潇','张恒益','杨智文','李院']
#print(names)
names.append('一无是处')#末尾插入一无是处
#print(names)
del names[3]#删除第三个元素
#print(names)
for i in range(5):
    print(f'{names[ra.randint(0,4)]},你最好有点东西')

if __name__ == "__main__":
    print('Good')