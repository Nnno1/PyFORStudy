password=input('请设置密码：')
shuzi,xiaoxie,daxie,other=0,0,0,0
total=len(password)
if total<8:
    print('密码长度必须大于等于8')
else:
    for i in password:
        if 48<=ord(i)<=57:
            shuzi+=1
        elif 97<=ord(i)<=122:
            xiaoxie+=1
        elif 65<=ord(i)<=90:
            daxie+=1
        else:
            other+=1
    sx1,sx2,sx3,sx4='','','',''
    if shuzi==0:
        sx1='数字'
    if xiaoxie==0:
        sx2='小写'
    if daxie==0:
        sx3='大写'
    if other==0:
        sx4='其他'
    sx=sx1+sx2+sx3+sx4
    if sx=='':
        print('密码设置成功')
    else:
        print(f'缺少{sx}字符')