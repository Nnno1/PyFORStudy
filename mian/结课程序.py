import pandas as pd
import turtle as t
sample=pd.read_csv('date.csv')
t.speed(0)
t.hideturtle()
t.penup()
t.goto(sample['x'][0], sample['y'][0])
t.pendown()
def draw(cw,ch,steplength):
    t.screensize(canvwidth=cw, canvheight=ch)
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.goto(300, 0)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.goto(0, 300)
    t.penup()
    for x1 in range(-250,300,steplength):
        t.goto(x1, -5)
        t.pendown()
        t.goto(x1, 5)
        t.penup()
    for y1 in range(-250,300,steplength):
        t.goto(-5, y1)
        t.pendown()
        t.goto(5,y1)
        t.penup()
    t.penup()
    t.goto(300, 20)
    t.write("X", font=("Arial", 12, "normal"))
    t.goto(20, 300)
    t.write("Y", font=("Arial", 12, "normal"))

    for i in range(len(sample)):
        x,y=sample['x'][i], sample['y'][i]
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.dot(5,'red')
t.done()