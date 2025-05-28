shuzi,xiaoxie,daxie,other=0,0,0,0
def detect(password):
    global shuzi,xiaoxie,daxie,other
    for i in password:
        if 48<=ord(i)<=57:
            shuzi+=1
        elif 97<=ord(i)<=122:
            xiaoxie+=1
        elif 65<=ord(i)<=90:
            daxie+=1
        else:
            other+=1
def feedback(shuzi,xiaoxie,daxie,other):
    sx1,sx2,sx3,sx4='','','',''
    if shuzi==0:
        sx1='数字'
    if xiaoxie==0:
        sx2='小写' 
    if daxie==0:
        sx3='大写' 
    if other==0:
        sx4='其他' 
    return sx1+sx2+sx3+sx4
#主程序
while True:
    password=input('请设置密码：')
    if len(password)<8:
        print('密码至少应该8个字符')
    else:
        detect(password)
        if feedback(shuzi,xiaoxie,daxie,other)=='':
            print('密码符合要求')
            break
        else:
            print(f'缺少{feedback(shuzi,xiaoxie,daxie,other)}字符')