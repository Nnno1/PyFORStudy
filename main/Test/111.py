#输出你好世界
message='Hello World'
print(message)
import turtle as tur
tur.speed(0)
#画30个圆圈，但是我也没明白为啥这个样，细见运行结果，速度已被提升
for a in range(30):
    tur.circle(50)
    tur.penup()
    tur.fd(100)
    tur.left(50)
    tur.pd()
tur.done()