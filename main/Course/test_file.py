def transform_to_bin(orgin):
    orgin=int(orgin)
    re=[]
    while True:
        w=orgin%2
        orgin=orgin//2
        re.append(w)
        if orgin==0:
            break
    result=''.join(str(i) for i in re)
    return result
a=input()
result=transform_to_bin(a)
print(result)