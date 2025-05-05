import datetime as dt
import turtle as t
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def DrawLine(draw):
    t.pensize(3)
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)
def Drawdigit(d): #d=distance
    DrawLine(True) if d in [2,3,4,5,6,8,9] else DrawLine(False)
    DrawLine(True) if d in [0,1,3,4,5,6,7,8,9] else DrawLine(False)
    DrawLine(True) if d in [0,2,3,5,6,8,9] else DrawLine(False)
    DrawLine(True) if d in [0,2,6,8] else DrawLine(False)
    t.left(90)
    DrawLine(True) if d in [0,4,5,6,8,9] else DrawLine(False)
    DrawLine(True) if d in [0,2,3,5,6,7,8,9] else DrawLine(False)
    DrawLine(True) if d in [0,1,2,3,4,7,8,9] else DrawLine(False)
def draw(content,x,y): #content->str  x,y->int
    goto(x,y)
    for i in content:
        Drawdigit(int(i))
        t.right(180)
        t.penup()
        t.forward(10)
        t.pendown()
def result(content1,content2,x,y):
    goto(x-200,y)
    t.write(content1,font=('楷体',16,'bold'))
    draw('20',x-100,y)
    A,B,C='年月日',range(x,x+301,125),range(4,9,2)
    for i,j,k in zip(A,B,C):
        draw(content2[k-2:k],j,y)
        t.write(i,font=('楷体',16,'bold'))
def daygap():  #intput->startdate    output->int
    global Y,M,D
    Y,M,D=eval(input('纪念日是？\n输入示例：2000,1,1\n'))
    date=dt.datetime(Y,M,D)
    today=dt.datetime.now()
    gap=today-date
    return gap.days
def main():
    days=daygap()
    today=dt.datetime.now().strftime('%Y%m%d')
    t.speed(0)
    t.hideturtle()
    result('今天是',today,-100,200)
    result('纪念日',str(Y)+f'{M:02d}'+f'{D:02d}',-100,100)
    goto(-300,-125)
    t.write('距离纪念日已经有',font=('楷体',22,'bold'))
    draw(str(days),-50,-125)
    t.write('天了',font=('楷体',22,'bold'))
    t.done()
main()