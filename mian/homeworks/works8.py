all=[]
def per_sco(name):
    scores,sta=[],[]
    score=input(f'请评委为选手{name}打分\n')
    scores=score.split()
    for i in scores:
        sta.append(float(i))    
    sta.sort()
    del sta[1],sta[-1]
    aver=f'{(sum(sta)/3):.2f}'
    return aver
for i in range(3):
    name=input('请输入选手姓名：')
    a=per_sco(name)
    A=(name,a)
    all.append(list(A))
result=sorted(all,key=lambda x:float(x[1]),reverse=True)
for i in range(3):
    print(f'{result[i][0]} 成绩:{result[i][1]}')