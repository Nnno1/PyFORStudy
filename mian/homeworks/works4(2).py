'''
编写一个程序，给小学生生成四则运算计算练习题。
尽可能完善程序，可考虑以下问题：

1、控制运算数范围（例如：可选10以内或100以内）
2、控制数据正确性（例如：除法除数不为零，只生成能够整除的题目）
3、设置关卡升级（例如：先练习单一运算，正确率达到90%以上再进入混合运算练习）


def grade(result,answer):       #判断正确的函数，返回bool值，打印反馈
    if result==answer:
        print('Right!\n')
        return True
    else:
        print('Wrong!\n')
        return False

max=100
a,b=randint(0,max),randint(0,max)
answer=a+b
print(f'{a}+{b}=?')
result=int(input())

a,b=randint(0,max),randint(0,max)
if a<b:
        a,b=b,a
answer=a-b
print(f'{a}-{b}=?')
result=int(input())


print('按任意键退出')
input()
'''
from random import randint

def detect():
    while True:             #函数用于检测输入
        try:
            result=int(input())
            return result
            break
        except ValueError:
            print('请输入整数')

max=100
a,b=randint(0,max),randint(0,max)
answer=a+b
print(f'{a}+{b}=?')