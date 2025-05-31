sco_list,ls=[],[]
file1=open('score.csv','r+',encoding='utf-8')
for line in file1:
    k=line.replace('\n','')
    sco_list.append(k.split(','))
file1.close()   
for i in range(1,6):
    sum=0
    for j in range(1,6):
        sum+=int(sco_list[j][i])
    print(f'{sco_list[0][i]}均分:{sum/5}',end=' ')
students=sco_list[1:]
ls=sorted(students,key=lambda sco_list:int(sco_list[6]),reverse=True)
file2=open('scSort.csv','w',encoding='utf-8')
for student in ls:
    file2.write(','.join(student)+'\n')
file2.close()