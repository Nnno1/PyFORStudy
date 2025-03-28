#方法一
a=input()
a=a.lower()
start,end=str(a[0].upper()),a[1:]
result=start+end
list=result.split(' ')
words=len(list)
print(f'\{result}\n{words}words')

#方法二
'''
words=0
for i in result:
    if i.isspace():
        words+=1
words+=1
print(f'{result}\n{words}words')
'''