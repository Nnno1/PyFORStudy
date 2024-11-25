#输出你好世界
message='Hello World'
print(message)
#引入海龟库，奇怪的是首次引入会出现全灰，运行后恢复正常引入库的状态
import turtle as tur
tur.speed(0)
#画50个圆圈，但是我也没明白为啥这个样，细见运行结果，速度已被提升
for a in range(50):
    tur.circle(50)
    tur.penup()
    tur.fd(100)
    tur.left(50)
    tur.pd()