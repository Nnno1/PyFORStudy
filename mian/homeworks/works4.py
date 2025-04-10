from random import randint
from random import choice
score=0
def grade(result,answer):#判断正确函数
    if result==answer:
        print('Right!')
        return True
    else:
        print('Wrong!')
        return False
def detect():#检测输入函数
    while True:             
        try:
            result=int(input())
            return result
            break
        except ValueError:
            print('请输入整数')
def plus(mode,max):#加乘函数
    a,b=randint(0,max),randint(0,max)
    answer=0
    if mode==1:
        answer=a+b
        print(f'{a}+{b}=?')
    elif mode==2:
        answer=a*b
        print(f'{a}*{b}=?')
    else:
        return None
    result=detect()
    if grade(result,answer):
        return True
    else:
        return False
def substraction(mode,max):#减除函数
    a,b,answer=0,0,0
    if mode==3:
        a,b=randint(0,max),randint(0,max)
        if a<b:
            a,b=b,a
        answer=a-b
        print(f'{a}-{b}=?')
    elif mode==4:
        a,b=randint(1,max),randint(1,max)
        while a%b!=0 or a<b:
            a,b=randint(1,max),randint(1,max)
        answer=a/b
        print(f'{a}/{b}=?')
    else:
        return None
    result=detect()
    if grade(result,answer):
        return True
    else:
        return False
def feedback(score):#评分评价函数
    print(f'得分为{score}！正确率为{(score/n)*100:.2f}%')
    if score/n<0.6:
        print('正确率还差点，继续加油')
    elif score==n:
        print('优秀！！！')
    else:
        print('及格啦！向满分前进')
while True:#参数设置部分
    try:
        n=int(input('要练习多少次？ '))
        m=int(input('确定运算范围：'))
        if n==0 or m==0:
            print('不要输入0')
        else:
            break
    except:
        print('请输入数字')
max=10**m   #确定运算范围,输入1为10内的，2为100以内的，以此类推
chioces=[1,2,3,4]
for i in range(n):#练习主要部分
    chi=choice(chioces)
    x,y=plus(chi,max),substraction(chi,max)
    if x or y:
        score+=1
feedback(score)
print('按任意键退出')
input()