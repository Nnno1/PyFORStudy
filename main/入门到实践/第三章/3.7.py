name=['张恒溢','杨智文','张艺潇']
name.insert(0,'A')
name.insert(2,'B')
name.append('C')
while len(name)>2:
    who=name.pop()
    print(who)
print(name)

del name[0],name[0]
print(name)