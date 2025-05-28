'''
有一个存放学生课程成绩的文件score.csv, 存有5名学生5门课程的成绩和总分，读取文件并显示文件的内容，并对成绩进行分析：

1、计算每门课程的平均分。

2、输出总分最高的同学和最低的同学的成绩。

3、拓展：将按照总分降序排序后的结果输出到一个新文件：scSort.csv中，并显示文件的内容。
'''
sco_list=[]
ls=[]
file=open('score.csv','r+',encoding='utf-8')
for line in file:
    k=line.replace('\n','')
    sco_list.append(k.split(','))
for i in range(1,6):
    sum=0
    for j in range(1,6):
        sum+=int(sco_list[j][i])
    print(f'{sco_list[0][i]}均分:{sum/5}',end=' ')
del sco_list[0]
ls=sorted(sco_list,key=lambda x:x=int(sco_list[6]),reverse=True)
file.close()