from random import randint
'''
编写一个程序，给小学生生成四则运算计算练习题。
尽可能完善程序，可考虑以下问题：

1、控制运算数范围（例如：可选10以内或100以内）
2、控制数据正确性（例如：除法除数不为零，只生成能够整除的题目）
3、设置关卡升级（例如：先练习单一运算，正确率达到90%以上再进入混合运算练习）
'''
def jia(result):
    a,b=randint(0,100),randint(0,100)
    print(f'{a}+{b}=?')
    answer=a+b
    result=int(result)
    if result==answer:
        return True
    else:
        return False
'''
if result==answer:
    print('Right!\n')
else:
    print('Wrong!\n')
'''