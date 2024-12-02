import pandas as pd
import turtle as t
sample=pd.read_csv('date.csv')
t.screensize(canvwidth=0.5,canvheight=0.5)
t.speed(0)
t.hideturtle()
for i in range(len(sample)):
    x,y=sample['1'][i], sample['0'][i]
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(5,'red')