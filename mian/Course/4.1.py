def transform_to_bin(orgin):
    orgin=int(orgin)
    re=[]
    while True:
        w=orgin%2
        orgin=orgin//2
        re.append(w)
        if orgin==0:
            break
        result=''.join(str(i) for i in re)
    return result
print('程序为转化十进制数值为相应进制数值\n输入举例:5，2\n其中5为需要转化的十进制数字，“2”代表转化为二进制数字')
print('只能转化为二、八、十六进制数字')
a=eval(input())
num,aim=a
if aim==2:
    result=transform_to_bin(num)
    print(f'{num}的二进制为{result}')
elif aim==8:
    result=str(oct(num))
    print(f'{num}的八进制为{result}')
elif aim==16:
    result=str(hex(num))
    print(f'{num}的十六进制为{result}')
else:
    print("无法转化为相应进制")