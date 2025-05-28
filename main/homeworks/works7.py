scores=[]
for i in range(5):
    score=input()
    scores.append(score.split())
list=sorted(scores,key=lambda x:int(x[2]),reverse=True)
for i in range(3):
    print(f'学号:{list[i][0]} 姓名:{list[i][1]} 成绩:{list[i][2]}')