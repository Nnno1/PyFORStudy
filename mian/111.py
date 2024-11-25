#输出你好世界
from types import get_original_bases

message='Hello World'
print('Hello World'+message)
import turtle as tur
tur.speed(0)
for a in range(50):
    tur.circle(50)
    tur.penup()
    tur.fd(100)
    tur.left(50)
    tur.pd()