import pandas as pd
import turtle as t

sample=pd.read_csv('date.csv')
t.speed(0)
t.hideturtle()

t.penup()
t.goto(sample['x'][0], sample['y'][0])
t.pendown()
t.screensize(canvwidth=2000, canvheight=1000)

t.penup()
t.goto(-1000,0)
t.pendown()
t.goto(1000,0)
t.penup()
t.goto(0,-1000)
t.pendown()
t.goto(0,1000)
t.penup()

for x1 in range(-500,1000,50):
    t.goto(x1,-5)
    t.pendown()
    t.goto(x1,5)
    t.penup()
for y1 in range(-1000,500,50):
    t.goto(-5,y1)
    t.pendown()
    t.goto(5,y1)
    t.penup()

t.goto(300, 20)
t.write("X", font=("Arial", 12, "normal"))
t.goto(20, 300)
t.write("Y", font=("Arial", 12, "normal"))

for i in range(len(sample)):
    x,y=sample['x'][i],sample['y'][i]
    t.goto(x,y)
    t.pendown()
    t.dot(5,'red')