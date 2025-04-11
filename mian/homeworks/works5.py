def huiwen(n):
    if n[::-1]==n:
        return True
    return False
def sushu(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=input()
b=int(a)
for i in range(b):
    if sushu(i) and huiwen(str(i)):
        print(f'{i}',end=' ')