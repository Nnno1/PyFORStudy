def plus(a,b):
    return a+b,a-b
print(plus(6,4))
def f(x):
    a,b=x
    return a*b
print(f(plus(6,4)))