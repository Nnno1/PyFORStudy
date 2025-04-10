from random import randint
from random import choice
def grade(result,answer):       #函数用于判断正确，返回bool值，打印反馈
    if result==answer:
        print('Right!\n')
        return True
    else:
        print('Wrong!\n')
        return False
def detect():
    while True:             #函数用于检测输入
        try:
            result=int(input())
            return result
            break
        except ValueError:
            print('请输入整数')
score=0
while True:
    try:
        n=int(input('要练习多少次？ '))
        m=int(input('确定运算范围：'))
        if n==0 or m==0:
            print('不要输入0')
        else:
            break
    except:
        print('请输入数字')
max=10**m       #确定运算范围,输入1为10内的，2为100以内的，以此类推
chioces=[1,2,3,4]
for i in range(n):
    chi=choice(chioces)     #随机四则运算
#加法模块
    if chi==1:
        a,b=randint(0,max),randint(0,max)
        answer=a+b
        print(f'{a}+{b}=?')
        result=detect()
        if grade(result,answer):#记录得分
            score+=1
#减法模块    
    elif chi==2:
        a,b=randint(0,max),randint(0,max)
        if a<b:
            a,b=b,a
        answer=a-b
        print(f'{a}-{b}=?')
        result=detect()
        if grade(result,answer):#记录得分
            score+=1
    elif chi==3:
#乘法模块
        a,b=randint(0,max),randint(0,max)
        answer=a*b
        print(f'{a}*{b}=?')
        result=detect()
        if grade(result,answer):#记录得分
            score+=1
    elif chi==4:
#除法模块
        a,b=randint(1,max),randint(1,max)
        if a<b:
            a,b=b,a
        while a%b!=0:
            a,b=randint(1,max),randint(1,max)
            if a<b:
                a,b=b,a
        answer=a/b
        print(f'{a}/{b}=?')
        result=detect()
        if grade(result,answer):#记录得分
            score+=1
print(f'得分为{score}！正确率为{(score/n)*100:.2f}%')
if score/n<0.6:
    print('正确率还差点，继续加油')
elif score/n==1:
    print('优秀！！！')
else:
    print('及格啦！向满分前进')
print('按任意键退出')
input()