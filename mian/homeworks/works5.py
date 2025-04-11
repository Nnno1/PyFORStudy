def huiwen(n):
    if n[::-1]==n:
        return True
    else:
        return False    
def sushu(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
a=input()
b=int(a)
for i in range(b):
    if sushu(i) and huiwen(str(i)):
        print(f'{i}',end=' ')