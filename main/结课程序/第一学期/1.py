#引入pandas库与turtle库
import pandas as pd
import turtle as t
#读取数据并且调整绘制速度与隐藏海龟
sample=pd.read_csv('D:\\PyFORStudy\\main\\结课程序\\第一学期\1.csv')
t.speed(0)
t.hideturtle()
#设置初始的数据原点画布大小
t.penup()
t.goto(sample['x'][0], sample['y'][0])
t.pendown()
t.screensize(canvwidth=2000, canvheight=1000)
#画出轴，在中心处（匹配了画布大小）
t.penup()
t.goto(-1000,0)
t.pendown()
t.goto(1000,0)
t.penup()
t.goto(0,-1000)
t.pendown()
t.goto(0,1000)
t.penup()
#利用循环进行划分刻度（步长）
for x1 in range(-1000,1000,50):
    t.goto(x1,-5)
    t.pendown()
    t.goto(x1,5)
    t.penup()
for y1 in range(-1000,1000,50):
    t.goto(-5,y1)
    t.pendown()
    t.goto(5,y1)
    t.penup()
#轴标签
t.goto(300, 20)#标签位置
t.write("X", font=("Arial", 12, "normal"))#字形，字号，不加粗
t.goto(20, 300)
t.write("Y", font=("Arial", 12, "normal"))
#len函数用于输出sample的数据总量，dot函数画出数据点，同时进行数据连线
for i in range(len(sample)):
    #sample['x'][i]    “['x']” 代表读取的数据列为   “[i]”为读取的数据行，注意：第一行数据从0开始
    x,y=sample['x'][i],sample['y'][i]
    t.goto(x,y)
    t.pendown()
    t.dot(5,'red')
t.done()